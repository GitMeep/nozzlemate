# Intensive and extensive properties

When first learning about thermodynamics, it is common to consider cylinders of gas being compressed, expanded, heated and cooled. Such a cylinder of gas has a defined volume, amount of substance and mass. When looking at flows of fluid though, there is no defined mass or volume or amount of substance. All the variables are varying continuosly along the flow. We need variables that are independent of the size of the system - so-called intensive properties.

Examples of intensive properties are density, pressure and temperature. These can be defined at single points in space. On the other hand, it doesn't make sense to ask "what is the volume of this point in space?". One can look at it through the lens of limits; the intensive properties are the properties that don't approach zero as the size of the system approaches zero. As an example of this, let us consider density. Density is defined as:
$$\rho = \frac{m}{V}$$

When the size of the system is made to approach zero, the volume will decrease, but the amount of mass in that volume will also decrease, so the density approaches a non-zero value (unless of course there is no mass present). Important to note is that in this case, letting the size of the system approach zero doesn't mean compressing the system! This would mean that the mass in the volume stayed the same, increasing density. If you think about a cylinder of gas, it is like considering a certain volume of gas around some point in the cylinder, and asking what happens when we consider smaller and smaller volumes around said point, approaching just the point itself in the limit. The properties that do depend on size are called _extensive_ properties.

Intensive properties can often be made by dividing two extensive properties by each other. This gives us the following quantities:

- Density: $\rho = \frac{m}{V}$
- Specific volume: $v = \frac{V}{m} = \frac{1}{\rho}$
- Specific internal energy: $e = \frac{U}{m}$
- Specific enthalpy: $h = \frac{H}{m} = e + pv$
- Specific heat capacity: $c = \frac{C}{m}$

As can be seen, when dividing an extensive property by mass we get a "specific" version. The symbol for these is often the lower-case of the symbol of the extensive counterpart. Note that we use $e$ for the specific internal energy instead of $u$, to avoid confusing it with the $x$-component of velocity!

## Intensive ideal gas law

We can now re-formulate the ideal gas law in terms of only intensive properties, such that we can apply it to flows. Let us start by stating the usual form:

$$pV = n\bar{R}T$$

Here $\bar{R}$ is just the normal gas constant - we will see the reason for the bar shortly.
The two extensive properties here are volume $V$ and amount of substance $n$, so let us divide both sides by volume to get rid of these:

$$p = \frac{n}{V}\bar{R}T$$

$\frac{n}{V}$ is the molar concentration (or _molarity_) $c$, not to be confused with specific heat capacity. This is related to density through the molar mass. While we could use molarity, it is more common to look at density, so to do this, we multiply and divide the right-hand side by the molar mass of the gas, $M$:

$$p = \frac{nM}{V}\frac{\bar{R}}{M}T$$

The first fraction becomes density. Furthermore, we define the _specific gas constant_ to be the ratio of the universal gas constant and the molar mass.
$$R = \frac{\bar R}{M}$$
Note that the "specific" here doesn't mean "per mass", but refers to the fact that this property is specific to each gas (as different gasses have different molar masses). Thus the second fraction becomes the specific gas constant, and we can write the ideal gas law as:

$$\boxed{p = \rho R T}$$

Nice and simple.

Of course one could rewrite the ideal gas law in many ways, but this it the form that we will be using.

## Next step

We are now ready to learn about [isentropic processes](./isentropic.md).
