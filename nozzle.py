from math import isnan
import numpy as np
from scipy.optimize import root_scalar

from relations import pres_to_mach_impl, mach_to_pres_impl, area_imp, massflow_imp, postshock_p0_impl

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
        result = root_scalar(closure, method='bisect', bracket=(0.0000001, 1), x0=0.00001)
        return result.root

    def pressure(self, mach: float):
        return mach_to_pres_impl(mach, self.stagnation_pressure, self.gas.gamma)
    
    def mach(self, pressure: float):
        return pres_to_mach_impl(pressure, self.stagnation_pressure, self.gas.gamma)

    def speed(self, pressure: float) -> float:
        return np.sqrt(2*self.gas.cp*self.stagnation_temperature*(1-(self.stagnation_pressure/pressure)**((1-self.gas.gamma)/self.gas.gamma)))

    def temperature(self, pressure: float) -> float:
        return self.stagnation_temperature*(pressure/self.stagnation_pressure)**((self.gas.gamma-1)/self.gas.gamma)

class Shock:
    def __init__(self, shock_mach: float, exit_mach: float, postshock_flow: Flow):
        self.shock_mach = shock_mach
        self.exit_mach = exit_mach
        self.postshock_flow = postshock_flow

class FlowSolution:
    def __init__(self, flow: Flow, geometry: NozzleGeometry, massflow: float, isentropic_exit_mach: float, isentropic_exit_pressure: float, exit_pressure: float, ambient_pressure: float, choked: bool, shock: Shock):
        self.flow = flow
        self.geometry = geometry
        self.massflow = massflow
        self.isentropic_exit_mach = isentropic_exit_mach
        self.isentropic_exit_pressure = isentropic_exit_pressure
        self.exit_pressure = exit_pressure
        self.choked = choked
        self.ambient_pressure = ambient_pressure
        self.shock = shock

def postshock_stagnation_presure(preshock_mach: float, preshock_flow: Flow) -> float:
    return postshock_p0_impl(preshock_flow.stagnation_pressure, preshock_mach, preshock_flow.gas.gamma)

def post_shock_flow(preshock_mach: float, preshock_flow: Flow) -> Flow:
    new_stagnation_pressure = postshock_stagnation_presure(preshock_mach, preshock_flow)
    return Flow(preshock_flow.gas, new_stagnation_pressure, preshock_flow.stagnation_temperature)

def shock_mach_to_exit_area(mach: float, flow: Flow, ambient_pressure: float, massflow: float) -> float:
    post_flow = post_shock_flow(mach, flow)
    exit_mach = post_flow.mach(ambient_pressure)
    return post_flow.area(exit_mach, massflow)

def find_shock_mach(ambient_pressure: float, massflow: float, nozzle: NozzleGeometry, flow: Flow) -> tuple[float, float, Flow]:
    tol = 0.000000001
    mach = 1
    stepsize = 1
    while True:
        postshock_flow = post_shock_flow(mach, flow)
        exit_mach = postshock_flow.mach(ambient_pressure)
        area = postshock_flow.area(exit_mach, massflow)

        nan_area = isnan(area)
        if not nan_area and abs(area - nozzle.exit_area) < tol:
            break

        if nan_area or area > nozzle.exit_area:
            mach -= stepsize
            stepsize /= 3

        mach += stepsize

    return mach, exit_mach, postshock_flow

def solve_nozzle_flow(nozzle: NozzleGeometry, flow: Flow, ambient_pressure: float):
    critical_massflow = flow.massflow(nozzle.throat_area, 1)
    critical_exit_mach = flow.mach_sub(nozzle.exit_area, critical_massflow)
    critical_exit_pressure = flow.pressure(critical_exit_mach)

    shock = None
    choked = ambient_pressure <= critical_exit_pressure
    if choked:
        final_massflow = critical_massflow
        isentropic_exit_mach = flow.mach_sup(nozzle.exit_area, critical_massflow)
        isentropic_exit_pressure = flow.pressure(isentropic_exit_mach)
        
        exit_mach = isentropic_exit_mach
        exit_pressure = isentropic_exit_pressure

        if isentropic_exit_pressure < ambient_pressure: # flow is overexpanded
            shock_mach, postshock_exit_mach, postshock_flow = find_shock_mach(ambient_pressure, final_massflow, nozzle, flow)

            # when the backpressure is just a little higher than the isentropic exit pressure
            # there sometimes seems to be some shockwave soltions that, followed by supersonic
            # flow results in a matched pressure at the exit. Shockwaves should always make to
            # downstream flow subsonic, so ignore any such "solutions".
            if postshock_exit_mach < 1:
                shock = Shock(shock_mach, postshock_exit_mach, postshock_flow)
                if shock_mach < isentropic_exit_mach: # shock is inside the nozzle, calculate exit conditions with post-shock flow
                    exit_pressure = ambient_pressure
    else:
        exit_pressure = ambient_pressure
        final_massflow = flow.massflow(nozzle.exit_area, exit_pressure)
        exit_mach = flow.mach_sub(nozzle.exit_area, final_massflow)
        isentropic_exit_mach = exit_mach

    return FlowSolution(
        flow=flow,
        geometry=nozzle,
        massflow=final_massflow,
        isentropic_exit_mach=isentropic_exit_mach,
        isentropic_exit_pressure=isentropic_exit_pressure,
        exit_pressure=exit_pressure,
        ambient_pressure=ambient_pressure,
        choked=choked,
        shock=shock
    )
