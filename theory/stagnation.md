# Stagnation properties

In the last chapter, we derived the general equation for energy conservation in steady adiabatic quasi-1D flow of a calorically perfect gas:

$$T_1 + \frac{u_1^2}{2 c_p} = T_2 + \frac{u_2^2}{2 c_p}$$

In this chapter, we will derive the so-called stagnation properties, which are useful reference quantities that stay constant throughout an isentropic flow. They are derived by imagining what happens when a flow slows down to zero speed from some other speed upstream (of course this wouldn't actually be possible in a real pipe; it is just a mathematical trick). To accomplish this, we set $u_2 = $ and solve for $T_2$, which we rename to $T_0$ to specify that it is the _stagnation temperature_. We also remove the 1 subscript:

$$T + \frac{u^2}{2 c_p} = T_0 + \frac{0^2}{2 c_p} \Rightarrow$$
$$\boxed{T_0 = T + \frac{u^2}{2 c_p}}$$

Thinking about what this means in terms of enthalpy, we see that the stagnation temperature is the temperature that the gas would reach if all energy in the flow was converted to enthalpy (since there is no kinetic energy when the gas is still).

If we assume that the flow is not just adiabatic, but also isentropic, we can relate the stagnation temperature to the _stagnation density_ and _stagnation pressure_ through the isentropic relations. To do this, we first transform the stagnation temperature above into a ratio so it fits better into the relations:

$$1 = \frac{T}{T_0} + \frac{u^2}{2 c_p T_0} \Rightarrow$$
$$\frac{T}{T_0} = 1 - \frac{u^2}{2 c_p T_0} \Rightarrow$
$$\frac{T_0}{T} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^{-1}$$

Then we substitute that into the relevant isentropic relations, replacing the subscript 1 with 0, and removing subscript 2:

$$\boxed{\frac{\rho_0}{\rho} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma}}$$
$$\boxed{\frac{p_0}{p} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma}}$$

The $\rho$, $p$ and $T$ without subscripts are known as the _static density_, _static pressure_ and _static temperature_ respectively.

The stagnation properties stay constant throughout an adiabatic flow - one could consider them a kind of "global constants", and if they are known they can be used to relate the speed and pressure/temperature/density at any point in the flow. There is an area of a rocket engine where the exhaust gasses are moving relatively slow compared to the rest of the flow: the combusion chamber. Thus the values of pressure, temeprature and density here can reasonably be used as stagnation values.

## Next step

With that down, we are now ready to move on to one of the last steps: deriving the [area-Mach number relation](./area-relation.md).
