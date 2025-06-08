# Isentropic processes

As established in the introduction, the ideal gas law gives us a relation between pressure, density and temperature, which any ideal gas must obey at all points, at all times:

$$p = \rho R T$$

But it doesn't tell us how a change in one variable will change the two other variables. Some people say things like "the temperature of a gas increases when compressed because of the ideal gas law", but for all we know, the pressure might decrease so much when compressing a gas that the temperature drops too! While the temperature generally _does_ increase when a gas is compressed, it is not because of the ideal gas law! We need some more assumptions to constrain exactly which solution of the ideal gas law is the correct one!

These assumptions are the idealized thermodynamic processes, which in general specify how some variable changes (or usually _doesn't_ change) during the process. A non-exhaustive list is:

- Isobaric process: the pressure is constant
- Isochoric process: the volume is constant
- Isothermal process: the temperature is constant
- Adiabatic process: no heat is exchanged with the environment
- Isentropic process: no irreversible processes happen (adiabatic with no diffusion, mixing, etc)

As you can probably guess from the title, the one we will be using is the isentropic process.

## Isentropic relations

As stated above, an isentropic process is one where no irreversible processes happen. An irreversible process is something that "spreads out" energy, or in general, increases entropy (we won't get into what that means here). The important thing for us is that it puts the following constraint on pressure and volume throughout the process:

$$\frac{p_2}{p_1} = \left(\frac{V_1}{V_2}\right)^\gamma$$

This power $\gamma$ is the so-called "ratio of specific heats"[^heat_cap_ratio]. It is the ratio between the heat capacity of the gas at constant pressure and at constant volume. What that all means is not too important right now, and we will just treat $\gamma$ as a constant value that can be looked up for different gasses.

Of course, volume is an extensive property. Let us rewrite it in terms of density by multiplying the volume fraction by $\frac{m}{m}$:

$$\frac{p_2}{p_1} = \left(\frac{V_1}{V_2}\frac{m}{m}\right)^\gamma \Rightarrow$$
$$\boxed{\frac{p_2}{p_1} = \left(\frac{\rho_2}{\rho_1}\right)^\gamma}$$

Later, we will be relating the temperature and speed, so let us see how density and pressure depend on temperature. Let us solve for density in the intensive ideal gas law:

$$\rho = \frac{p}{RT}$$

And use that to replace the densities in the relation above:

$$\frac{p_2}{p_1} = \left(\frac{p_2RT_1}{RT_2p_1}\right)^\gamma$$

The gas constants cancel, and we then separate the temperature ratio and pressure ratio into their own fractions:

$$\frac{p_2}{p_1} = \left(\frac{T_1}{T_2}\right)^\gamma \left(\frac{p_2}{p_1}\right)^\gamma$$

And then move the pressure ratio on the right-hand side to the left and combine it with the other pressure ratio:

$$\frac{p_2}{p_1} \left(\frac{p_2}{p_1}\right)^{-\gamma} = \left(\frac{T_1}{T_2}\right)^\gamma \Rightarrow$$
$$\left(\frac{p_2}{p_1}\right)^{1-\gamma} = \left(\frac{T_1}{T_2}\right)^\gamma$$

We then raise both sides to the $\frac{1}{1 - \gamma}$ power to free the pressure ratio from its exponent prison:

$$\frac{p_2}{p_1} = \left(\frac{T_1}{T_2}\right)^\frac{\gamma}{1 - \gamma}$$

And lastly, just so the variables with subscript 2 are in the enumerator of each fraction, we flip the temperature ratio while negating the exponent:

$$\boxed{\frac{p_2}{p_1} = \left(\frac{T_2}{T_1}\right)^\frac{\gamma}{\gamma - 1}}$$

Now we also want to see how the density depends on temperature. To do this we substitute the expression that we just derived for the pressure ratio into the pressure-density relation from before:

$$\left(\frac{T_2}{T_1}\right)^\frac{\gamma}{\gamma - 1} = \left(\frac{\rho_2}{\rho_1}\right)^\gamma$$

We raise both sides to the $\frac{1}{\gamma}$ power to free the density ratio, and then switch the sides:

$$\boxed{\frac{\rho_2}{\rho_1} = \left(\frac{T_2}{T_1}\right)^\frac{1}{\gamma - 1}}$$

And with that we can now calculate any of the three variables at any point in the flow as long as we know the value of one of the other variables at that point, and two of the variables at some other point.

## Next step

We are now ready to put these relatios to use when we relate temperature to speed in the next section using [conservation of mass and energy](./conservation.md).

[^heat_cap_ratio]: The ratio of specific heats is also known as the "heat capacity ratio" or the "adiabatic index".
