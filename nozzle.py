import numpy as np
from scipy.optimize import root_scalar

from relations import postshock_p_impl, pres_to_mach_impl, mach_to_pres_impl, area_imp, massflow_imp, postshock_p0_impl

class NozzleGeometry:
    def __init__(self, chamber_radius: float, chamber_length: float, throat_length: float, diverging_length: float, exit_radius: float, expansion_ratio: float):
        self.chamber_length = chamber_length
        self.throat_length = throat_length
        self.diverging_length = diverging_length
        self.nozzle_length = chamber_length + throat_length + diverging_length

        self.chamber_radius = chamber_radius
        self.chamber_area = np.pi*chamber_radius**2
        
        self.exit_area = np.pi*exit_radius**2
        self.exit_radius = exit_radius

        self.throat_area = self.exit_area / expansion_ratio
        self.throat_radius = np.sqrt(self.throat_area/np.pi)

class Gas:
    def __init__(self, molar_mass: float, isobaric_specific_heat_capacity: float, heat_capacity_ratio: float):
        universal_gas_constant = 8.31446261815324 # J*K⁻¹*mol⁻¹

        self.M = molar_mass
        self.R = universal_gas_constant/molar_mass
        self.cp = isobaric_specific_heat_capacity
        self.gamma = heat_capacity_ratio

class Flow:
    def __init__(self, gas: Gas, stagnation_pressure: float, stagnation_temperature: float):
        self.gas = gas
        self.stagnation_pressure = stagnation_pressure
        self.stagnation_temperature = stagnation_temperature
        self.stagnation_density  = stagnation_pressure/(gas.R*stagnation_temperature)

        critical_pressure_ratio = (2/(gas.gamma+1))**(gas.gamma/(1-gas.gamma))
        self.critical_pressure = stagnation_pressure/critical_pressure_ratio # Pa

    def area(self, mach: float, massflow: float) -> float:
        return area_imp(mach, massflow, self.stagnation_density, self.stagnation_temperature, self.gas.cp, self.gas.gamma)

    def massflow(self, area: float, mach: float) -> float:
        return massflow_imp(mach, area, self.stagnation_density, self.stagnation_temperature, self.gas.cp, self.gas.gamma)

    def mach_sup(self, flow_area: float, massflow: float) -> float:
        closure = lambda mach: self.area(mach, massflow) - flow_area
        result = root_scalar(closure, method='newton', x0=2)
        return result.root

    def mach_sub(self, flow_area: float, massflow: float) -> float:
        closure = lambda mach: self.area(mach, massflow) - flow_area
        result = root_scalar(closure, method='bisect', bracket=(0.0000001, 1), x0=0.5)
        return result.root

    def pressure(self, mach: float):
        return mach_to_pres_impl(mach, self.stagnation_pressure, self.gas.gamma)
    
    def mach(self, pressure: float):
        return pres_to_mach_impl(pressure, self.stagnation_pressure, self.gas.gamma)

    def speed(self, pressure: float) -> float:
        return np.sqrt(2*self.gas.cp*self.stagnation_temperature*(1-(self.stagnation_pressure/pressure)**((1-self.gas.gamma)/self.gas.gamma)))

    def temperature(self, pressure: float) -> float:
        return self.stagnation_temperature*(pressure/self.stagnation_pressure)**((self.gas.gamma-1)/self.gas.gamma)
    
    # shock relations
    def postshock_stagnation_presure(self, preshock_mach: float) -> float:
        return postshock_p0_impl(self.stagnation_pressure, preshock_mach, self.gas.gamma)
    
    def postshock_pressure(self, preshock_mach: float, preshock_pressure: float) -> float:
        return postshock_p_impl(preshock_pressure, preshock_mach, self.gas.gamma)
    
    def post_shock_flow(self, preshock_mach: float):
        new_stagnation_pressure = self.postshock_stagnation_presure(preshock_mach)
        return Flow(self.gas, new_stagnation_pressure, self.stagnation_temperature)

class Shock:
    def __init__(self, shock_mach: float, exit_mach: float, postshock_flow: Flow):
        self.shock_mach = shock_mach
        self.exit_mach = exit_mach
        self.postshock_flow = postshock_flow

class FlowSolution:
    def __init__(self, flow: Flow, geometry: NozzleGeometry, massflow: float, critical_exit_pressure: float, isentropic_exit_pressure: float, exit_shock_exit_pressure: float, exit_pressure: float, ambient_pressure: float, shock: Shock):
        self.flow = flow
        self.geometry = geometry
        self.massflow = massflow
        self.critical_exit_pressure = critical_exit_pressure
        self.isentropic_exit_pressure = isentropic_exit_pressure
        self.exit_shock_exit_pressure = exit_shock_exit_pressure
        self.exit_pressure = exit_pressure
        self.ambient_pressure = ambient_pressure
        self.shock = shock

def shock_mach_to_exit_area(mach: float, flow: Flow, ambient_pressure: float, massflow: float) -> float:
    post_flow = flow.post_shock_flow(mach)
    exit_mach = post_flow.mach(ambient_pressure)
    return post_flow.area(exit_mach, massflow)

def find_shock_mach(ambient_pressure: float, isentropic_exit_mach: float, massflow: float, nozzle: NozzleGeometry, flow: Flow) -> tuple[float, float, Flow]:
    # max_mach might be outside the domain of the postshock_flow.mach function which will cause numpy to complain about taking the square root of a negative number.
    np.seterr(invalid='ignore')
    max_mach = isentropic_exit_mach
    min_mach = 1
    mach = (max_mach+min_mach)/2

    tolerance = 0.000000001
    while True:
        postshock_flow = flow.post_shock_flow(mach)
        exit_mach = postshock_flow.mach(ambient_pressure)
        area_diff = postshock_flow.area(exit_mach, massflow) - nozzle.exit_area

        if abs(area_diff) < tolerance:
            break

        # area_diff might be NaN, but since comparing with NaN is always false, the next guess will be lower which moves back towards defined territory
        # so it works out in our favor :D
        # (this could be avoided by setting max_mach inside the domain of postshock_flow.mach, but I can't be bothered to work out what the upper bound
        # of this function is right now (it will probably require some numerical root finding anyways so this seems like a fine way to do it))
        if area_diff < 0:
            min_mach = mach
        else:
            max_mach = mach
        
        mach = (min_mach + max_mach)/2

    return mach, exit_mach, postshock_flow

def solve_nozzle_flow(nozzle: NozzleGeometry, flow: Flow, ambient_pressure: float):
    critical_massflow = flow.massflow(nozzle.throat_area, 1) # mass flow rate when flow is choked
    critical_exit_mach = flow.mach_sub(nozzle.exit_area, critical_massflow)
    critical_exit_pressure = flow.pressure(critical_exit_mach) # the exit pressure below which flow will be choked

    isentropic_exit_mach = flow.mach_sup(nozzle.exit_area, critical_massflow)
    # the exit pressure at which and below which flow will be isentropic throughout the nozzle (the optimal exit pressure)
    isentropic_exit_pressure = flow.pressure(isentropic_exit_mach)

    # the exit pressure at which and above which (while below the isentropic exit pressure) shockwaves will occur inside the nozzle
    exit_shock_exit_pressure = flow.postshock_pressure(isentropic_exit_mach, isentropic_exit_pressure)

    # we assume the final massflow to be the critical (choked) mass flow rate. This is overwritten in case flow isn't choked.
    final_massflow = critical_massflow
    # also assume that exit pressure is ambient. This will be overwritten in case of underexpanded flow
    exit_pressure = ambient_pressure

    shock = None
    if ambient_pressure >= critical_exit_pressure: # subsonic flow throughout nozzle, not choked
        subsonic_exit_mach = flow.mach(ambient_pressure)
        final_massflow = flow.massflow(nozzle.exit_area, subsonic_exit_mach) # override mass flow rate
    elif ambient_pressure < critical_exit_pressure and ambient_pressure >= exit_shock_exit_pressure: # there is a shock is inside or at nozzle exit
        shock_mach, postshock_exit_mach, postshock_flow = find_shock_mach(ambient_pressure, isentropic_exit_mach, final_massflow, nozzle, flow)
        shock = Shock(shock_mach, postshock_exit_mach, postshock_flow)
    else: # there is no shock wave in nozzle and flow is overexpanded, matched or underexpanded
        exit_pressure = isentropic_exit_pressure

    return FlowSolution(
        flow=flow,
        geometry=nozzle,
        massflow=final_massflow,
        critical_exit_pressure=critical_exit_pressure,
        isentropic_exit_pressure=isentropic_exit_pressure,
        exit_shock_exit_pressure=exit_shock_exit_pressure,
        exit_pressure=exit_pressure,
        ambient_pressure=ambient_pressure,
        shock=shock
    )
