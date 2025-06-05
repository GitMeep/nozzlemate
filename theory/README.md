# Nozzle theory

DISCLAIMER: THIS THEORY WRITEUP IS STILL WORK-IN-PROGRESS. ADJUST YOUR EXPECTATIONS ACCORDINGLY.

This program is based on the steady quasi-1D isentropic flow theory of nozzles. This theory writeup will attempt to explain what that means, while explaining how NozzleMate uses the resulting equations to solve the flow in rocket nozzles. You are of course free to read in any order you want, but the "guided path" will start kind of in the middle with the quasi-1D mass and energy conservation equations and isentropic relations, and derive the various flow-related relations from there. (If you didn't understand any of that, don't worry and just keep reading). Derivation of these starting equations from more fundamental equations will be optional reading afterwards.

This writeup is mostly based on the first few chapters of [The International Student Edition of Modern Compressible Flow by John D. Anderson](https://isbnsearch.org/isbn/9781260570823) and the excellent [Compressible Flow playlist](https://www.youtube.com/playlist?list=PLxT-itJ3HGuVt4A8cwi4WdUudTbh1TQVV) by JoshTheEngineer.

It is assumed that the reader has a decent understanding of _force_, _pressure_, _absolute temperature_, _density_, _amount of substance_, _molar mass_, and the _ideal gas law_ as well as _derivatives_. If you don't, there are lots of great resources online, I'm sure you can find them.

## Theory overview

With that out of the way, let us get an overview of the theory.

### The function of a nozzle

The nozzles used on most rocket engines are so-called converging-diverging nozzles - also known as CD-nozzles or de Laval nozzles. The desired function of such a rocket nozzle is to convert the thermal energy (heat, temperature) of the high-pressure gas in the combustion chamber to directed kinetic energy (that is, speed), since we want to accelerate this gas as much as possible to get a reaction force (thrust) that is as large as possible. While mostly round in cross-section, they can also be square or have other shapes (for example in wind-tunnels) - though it doesn't really matter since we will mostly be considering the cross-sectional area.

A little terminology: the narrowest part of a CD-nozzle is called the throat and the opening to the surroundings is called the exit. The nozzle consists of two sections: the converging (meaning narrowing) section upstream of the throat, and the diverging (meaning widening) section downstream of the throat. Most rocket engines will have a combustion chamber upstream of the converging section where the propellants (fuel and oxidizer) are burnt to produce the exhaust gas.

A nozzle will try to match the pressure of the exhaust gas at the exit (called the _exit pressure_) to the _ambient pressure_ (the pressure of the atmosphere for example), but as we will see, this is not always possible, and under certain conditions a CD-nozzle may have an exit pressure that is higher or lower than the ambient pressure.

### Quasi-1D

Quasi-one-dimensional sounds scary, but it is really quite simple. A CD-nozzle is usually one-dimensional in the sense the radius - or really, cross-sectional area - can be seen as varying with distance along the nozzle. Imagine slicing the nozzle perpendicular to its axis in different places - the crosssectional area may be different in different places. In this way we know that the nozzle is really three-dimensional, but we can describe it as a 2D-quantity (cross-sectional area) varying along a 1D axis, thus quasi-1D. It doesn't even matter what shape the cross-section is (in reality it probably would make a little difference, but not in this model).

Furthermore, all flow variables are also assumed to only be a function of distance along the nozzle (let us call this $x$ from now on), and the velocity is assumed to only be in the $x$-direction. This is, of course, a simplification. In reality the flow variables can vary with the radius and even radially around the nozzle, but this simplification will allow us to come up with a simpler model which is relatively easy to work with and can still give some insights into how the nozzle works.

### Steady flow

Another assumption that is made is that the flow is _steady_ or _constant_. This means that no values are changing with time - all derivatives with respect to time are zero. Of course, this doesn't mean that the gas is thought to be standing still, but that the speed (or any other property) of the gas at any point in space isn't changing.

This is actually an important point. We are looking at the fluid while standing still relative to the nozzle, and describing how the fluid is acting at certain points in space. Thus we can say that, for example, the density isn't changing with time, because the fluid passing through any one point in space will always have the same density. This is called the Eulerian view of flow. The counterpart is called the Lagrangian view, where we imagine that we are a particle following the fluid velocity at all times and looking at how the flow variables change. In this case we obviously can't say that the properties are constant, since, for example, the pressure changes through the nozzle and we are ourselves moving through the nozzle and would thus observe a changing pressure over time.[^material_derivative]

Steady flow means that we are not considering how a rocket engine starts up and reaches a stable operating condition. We are only deriving a set of equations that the flow must fulfil once the flow in the nozzle has reached a steady state, and then assume that time-dependent processes will bring the flow to this state once the engine has started up and we are providing a steady flow of propellants. The process of "simulating" the nozzle is then one of figuring out a flow which satisfies these equations.[^wrap_your_head]

### Isentropic flow and conservation equations

Now that we have the framework of the model down, let us go through a quick overview of how we will derive the final equations.

We mainly care about the following variables:

- $p$: pressure
- $T$: absolute temperature
- $\rho$: density (this greek letter is called "rho", pronounced like "row")
- $u$: speed
- $A$: area

Pressure, temperature and density are related through the ideal gas law.[^intensive_gas_law] We know that the pressure should decrease through the nozzle, but this still leaves the temperature and density undetermined since there are infinite combinations of the two that would satisfy the gas law (you can reach the same pressure with high temperature and low density or low temperature and high density). This is fixed by assuming that the flow is isentropic, which means that we assume that the fluid doesn't exchange heat with the surroundings and no other irreversible processes, like mixing, happen (no turbulence). This gives us an equation directly relating the pressure and density at one point in the flow to the pressure and density at another point in the flow - thus, if we know at least two of pressure, density or temperature at some point, we can calculate them for all other points (the temperature and pressure in the combustion chamber are usually known).

Now we need to relate all of this to speed. We realize that energy can exist in two forms in a flow: kinetic energy of the flow and internal energy. The kinetic energy is related to speed and internal energy to temperature. Since the sum of these two energies (really energy densities) must be constant at all points in the flow, we can now relate speed to pressure, temperature and density.

The last piece of the puzzle is area. Since the flow is steady we realize that the amount of mass flowing through any cross-section of the nozzle per time must be the same everywhere (if mass is flowing into an area of the nozzle faster than it is flowing out, the density would increase over time which we have explicitly forbidden). Since the mass flowing perpendicularly through a surface per time is the product of speed, density and area ($\rho u A$) - try to convince yourself of this - this product must be the same anywhere along the nozzle. This finally gives us a way to relate area to all the other variables.

## Next step

Before we can really get into the details we need a quick excursion to talk about intensive and extensive variables, [see you there](./intensive.md).

[^material_derivative]: The Eulerian and Lagrangian views are related via the so-called [material derivative](https://en.wikipedia.org/wiki/Material_derivative) (which is also known under many other names). Some things are easier to describe in one view and other things in the other view, and this allows translating between the two.

[^wrap_your_head]: If you're like me and initially thought that modelling flow would have to involve tracking how little bits of fluid move over time, this might take a little while to wrap your head around. It certainly did for me 😅.

[^intensive_gas_law]: You might know the ideal gas law as relating pressure, temperature, amount of substance and volume (pV = nRT) but since density is related directly to volume and amount of substance we can rewrite the equation to relate pressure, temperature and density. We will do this in the next chapter.
