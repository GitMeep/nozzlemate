# Steady quasi-1D conservation equations

We imagine a steady flow of gas through a section of a pipe with varying cross-sectional area. Since the flow is steady, neither mass nor energy can build up in this section over time and conservation of mass and energy thus dictate that the rate of mass and energy flowing into the section must equal the rate of the two flowing out.

## Conservation of mass

Let us first look closer at the conservation of mass. This one is the simplest of the two, and simply states that the product of density, area and speed must be the same at the two ends of the section (called the control volume):

$$\rho_1 u_1 A_1 = \rho_2 u_2 A_2 = \dot m$$

Here the subscripts 1 and 2 refer to the two ends of the control volume, the entrance and exit.

This product is called the mass flow rate, and is denoted by $\dot m$. It is how much mass is flowing through the system per time.

## Conservation of energy

Energy can be exchanged between the control volume and the rest of the pipe in two ways:

- Energy in the form of directed kinetic energy and internal energy can flow into the control volume with flow of fluid
- The pressure at the boundary of the control volume does work on the fluid as it flows in/out

We have assumed that no heat is generated or removed (or conducted in or out - meaning adiabatic) inside the control volume, and that there are no body forces like gravity or acceleration doing work on the fluid as it moves. This is obviously not quite true for a rocket engine where heat escapes through the nozzle walls and we obviously have gravity and are accelerating, but these effects are small enough that we can reasonably ignore them.

This leads us to the following general energy conservation equation for quasi-1D flow:

$$\left(e_1 + \frac{u_1^2}{2}\right)\rho_1 A_1 u_1 + p_1 A_1 u_1 = \left(e_2 + \frac{u_2^2}{2}\right)\rho_2 A_2 u_2 + p_2 A_2 u_2$$

$e$ is the specific internal energy, $\frac{u^2}{2}$ is the specific kinetic energy and $\rho A u$ is the mass flow rate. Thus the $\left(e + \frac{u^2}{2}\right)\rho A u$ terms describe the rate of kinetic and internal energy being carried by the mass flowing across the boundary.

The $p A u$ terms describe the rate of work being done on the fluid crossing the boundary by the environment. $p A$ is the force on the boundary, and $u$ is the speed. The product of speed and force is power (rate of work). Of course, the actual work done on the fluid particles, say, entering the control volume, is going to be lower, since there is a pressure just on the other side of the boundary doing work in the opposite direction. The key here is to imagine the control volume being split into lots of little control volumes: the pressure and area at the boundary between any of these two control volumes is going to be equal, thus the negative work done on the fluid leaving one control volume by the next control volume, is the same as the positive work done on the fluid by the control volume that the fluid is leaving as it enters the next control volume (you might have to read that a few times), thus the work done at all the internal boundaries cancel out and we are left with only the work done at the outer boundaries $p_1 A_1 u_1$ and $p_2 A_2 u_2$.

From conservation of mass we know that $\rho_1 u_1 A_1 = \rho_2 u_2 A_2$, so let us try simplifying a bit by dividing by this on both sides (using the respective subscripts for each side):

$$e_1 + \frac{u_1^2}{2} + \frac{p_1}{\rho_1} = e_2 + \frac{u_2^2}{2} + \frac{p_2}{\rho_2}$$

$\frac{1}{\rho}$ is the same as specific volume $v$, so we get:

$$e_1 + \frac{u_1^2}{2} + p_1 v_1 = e_2 + \frac{u_2^2}{2} + p_2 v_2$$

We now have $e + pv$ on both sides. Remember, this is the definition of specific enthalpy, $h$, so we can write:

$$h_1 + \frac{u_1^2}{2} = h_2 + \frac{u_2^2}{2}$$

From this we can see that energy can exists either as enthalpy (internal energy + pressure-volume energy) or kinetic energy.

In an calorically perfect gas, the heat capacities are constant, so the specific enthalpy is simply given by $h = c_p T$ where $c_p$ is the specific heat capacity at constant pressure. Thus, we can substitute the enthalpy on each side and simplify to arrive at our final equation relating temperature and speed:

$$
c_p T_1 + \frac{u_1^2}{2} = c_p T_2 + \frac{u_2^2}{2} \Rightarrow \\
\boxed{T_1 + \frac{u_1^2}{2 c_p} = T_2 + \frac{u_2^2}{2 c_p}}
$$

This equation is true for general steady adiabatic quasi-1D flow of calorically perfect gas with no body forces.

## Next step

By assuming that the flow is also isentropic and using the isentropic relations derived earlier, we can replace the temperatures by pressure and density, ther latter of which we will need to finally relate all this to area through mass conservation. Before we do that though, we are going to have a look at the so-called [stagnation properties](./stagnation.md), which are useful reference quantities that stay constant throughout an isentropic flow.
