import numpy as np
import matplotlib.pyplot as plt

from nozzle import Flow, FlowSolution, NozzleGeometry

def nozzle_radius(x: float, geo: NozzleGeometry) -> float:
    return np.interp(x,
        [0,                  geo.chamber_length, geo.chamber_length+geo.throat_length, geo.nozzle_length],
        [geo.chamber_radius, geo.throat_radius,  geo.throat_radius,                    geo.exit_radius]
    )

def speed(mach: float, flow: Flow):
    return mach * np.sqrt((flow.gas.gamma*flow.gas.R*flow.stagnation_temperature)/(1+(flow.gas.gamma-1)/2*mach**2))

def temperature(mach: float, flow: Flow):
    return flow.stagnation_temperature*(1+(flow.gas.gamma-1)/2*mach**2)**-1

def density(mach: float, flow: Flow):
    return flow.stagnation_density*(1+(flow.gas.gamma-1)/2*mach**2)**(1/(1-flow.gas.gamma))

def pressure(mach: float, flow: Flow):
    return flow.stagnation_pressure*(1+(flow.gas.gamma-1)/2*mach**2)**(flow.gas.gamma/(1-flow.gas.gamma))

def visualize_solution(sol: FlowSolution, nozzle_ax: plt.Axes, pressure_ax: plt.Axes, mach_ax: plt.Axes, speed_ax: plt.Axes, temp_ax: plt.Axes, density_ax: plt.Axes, resolution: int):
    flow = sol.flow
    geo = sol.geometry

    x = np.linspace(0, geo.nozzle_length, resolution, endpoint=True, dtype=float)
    r = nozzle_radius(x, geo)
    a = np.pi*r**2

    throat_index = int(resolution/geo.nozzle_length*(geo.chamber_length+geo.throat_length))

    mach_sup_vector = np.vectorize(lambda a: flow.mach_sup(a, sol.massflow))
    mach_sub_vector = np.vectorize(lambda a: flow.mach_sub(a, sol.massflow))

    if sol.ambient_pressure == sol.flow.stagnation_pressure: # no flow if ambient pressure is equal to stagnation pressure
        M = np.zeros_like(x)
    elif sol.ambient_pressure >= sol.critical_exit_pressure: # subsonic flow if ambient pressure is above or equal to critical exit pressure
        M = mach_sub_vector(a)
    if sol.ambient_pressure < sol.critical_exit_pressure: # supersonic flow after nozzle if ambient pressure is below critical exit pressure
        M_sub = mach_sub_vector(a[:throat_index])
        M_sup = mach_sup_vector(a[throat_index:])
        M = np.concatenate((M_sub, M_sup))
        

    # if there is no shock inside the nozzle or at the exit, calculate values with the normal isentropic flow
    if sol.shock is None:
        p = pressure(M, flow)
        u = speed(M, flow)
        t = temperature(M, flow)
        rho = density(M, flow)
    else: # if there is a shock inside the nozzle, calculate the values downstream of the shock with the post-shock flow
        shock_index = np.argmin(np.abs(M-sol.shock.shock_mach))
        M_postshock = np.vectorize(lambda a: sol.shock.postshock_flow.mach_sub(a, sol.massflow))(a[shock_index:])
        p = np.append(pressure(M[:shock_index], flow), pressure(M_postshock, sol.shock.postshock_flow))
        u = np.append(speed(M[:shock_index], flow), speed(M_postshock, sol.shock.postshock_flow))
        t = np.append(temperature(M[:shock_index], flow), temperature(M_postshock, sol.shock.postshock_flow))
        rho = np.append(density(M[:shock_index], flow), density(M_postshock, sol.shock.postshock_flow))
        M = np.append(M[:shock_index], M_postshock)
    

    nozzle_ax.plot(x,r, color='black')
    nozzle_ax.plot(x,-r, color='black')

    pressure_ax.set_ylabel('Pressure [Pa]')
    pressure_ax.plot(x, p)
    pressure_ax.axhline(y=sol.ambient_pressure, color='black', ls='--', label='Ambient pressure')
    pressure_ax.legend()

    mach_ax.set_ylabel('Mach number')
    mach_ax.plot(x, M)

    speed_ax.set_ylabel('Flow speed [m/s]')
    speed_ax.plot(x, u)

    temp_ax.set_ylabel('Temperature [K]')
    temp_ax.plot(x, t)

    density_ax.set_ylabel('Density [kg/m³]')
    density_ax.plot(x, rho)
