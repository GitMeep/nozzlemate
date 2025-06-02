import matplotlib.pyplot as plt

from nozzle import NozzleGeometry, Gas, Flow, solve_nozzle_flow
from vis import visualize_solution

g = 9.80665 # m*s⁻²

# TODO: load gas and nozzle parameters from JSON files given as command line arguments

# operating conditions
chamber_pressure = 20640000 # Pa
chamber_temperature = 3573.15 # K
ambient_pressure = 500000 # Pa

# mechanical parameters
exit_radius = 1.2192 # m
expansion_ratio = 78 # RS-25

chamber_radius = 0.3 # m
chamber_length = 0.1 # m
throat_length = 0.0 # m
diverging_length = 0.2 # m

# fluid parameters
heat_cap_ratio = 1.33 # γ (gamma)
isobar_spec_heat_cap = 2000 # J*kg⁻¹*K⁻¹
molar_mass = 0.01801528 # kg*mol⁻¹

def solve():
    nozzle = NozzleGeometry(
        chamber_radius=chamber_radius,
        chamber_length=chamber_length,
        throat_length=throat_length,
        diverging_length=diverging_length,
        exit_radius=exit_radius,
        expansion_ratio=expansion_ratio
    )

    flow = Flow(
        gas=Gas(
            molar_mass=molar_mass,
            isobaric_specific_heat_capacity=isobar_spec_heat_cap,
            heat_capacity_ratio=heat_cap_ratio
        ),
        # We assume that the stagnation conditions are equal to chamber conditions. This is not quite correct, but since the flow in the flow in the chamber
        # should be moving relatively slow it is a good approximation.
        # TODO: iteratively refine the stagnation conditions based on the previous solutions with this assumption as the initial guess
        stagnation_pressure=chamber_pressure,
        stagnation_temperature=chamber_temperature
    )

    sol = solve_nozzle_flow(nozzle, flow, ambient_pressure=ambient_pressure)
    flow = sol.flow

    if sol.choked:
        print('Flow is choked')
        if sol.isentropic_exit_pressure < ambient_pressure:
            print('Flow is overexpanded')
            if sol.shock is not None:
                flow = sol.shock.postshock_flow
                if sol.shock.shock_mach < sol.isentropic_exit_mach: # Shock is inside nozzle
                    print('Warning, shock inside nozzle.')
                elif sol.shock.shock_mach == sol.isentropic_exit_mach:
                    print('Shock is at the nozzle exit')
                else:
                    print('Shock is outside nozzle')
        elif sol.isentropic_exit_pressure > ambient_pressure:
            print('Flow is underexpanded. You\'re loosing performance')
        else: # very unlikely
            print('Nozzle is perfectly matched!')
    else:
        print('Warning, your flow is not choked!')

    exit_speed = flow.speed(sol.exit_pressure)
    exit_temperature = flow.temperature(sol.exit_pressure)

    thrust = sol.massflow * exit_speed # N

    print(f'Mass flow rate: {sol.massflow} kg/s')
    print(f'Exit pressure: {sol.exit_pressure} Pa')
    print(f'Exit speed (specific impulse): {exit_speed} m/s ({exit_speed / g} s)')
    print(f'Exit temperature: {exit_temperature} K')
    print(f'Thrust: {thrust/1000} kN')

    fig, (nozzle_ax, pressure_ax, mach_ax, speed_ax, temp_ax, density_ax) = plt.subplots(6,1, sharex=True)

    fig.set_figheight(10)

    visualize_solution(
        sol=sol,
        nozzle_ax=nozzle_ax,
        pressure_ax=pressure_ax,
        mach_ax=mach_ax,
        speed_ax=speed_ax,
        temp_ax=temp_ax,
        density_ax=density_ax,
        resolution=1000
    )

    density_ax.set_xlabel('Length [m]')

    plt.show()


def main():
    solve()

if __name__ == '__main__':
    main()
