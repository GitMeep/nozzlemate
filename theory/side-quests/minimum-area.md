# Side quest: Speed at the minimum area

This section is not strictly necessary in understanding the model, but it helps motivate why we want to look at the Mach number. A lot of the mathy derivations are hidden in dropdowns and while there are explanations for each step, it is usually somewhat confusing to follow such derivations step by step. Readers are encouraged to try and derive the final expression themselves, using the steps in the dropdowns as a guide in case they get stuck.

In the [area-Mach number chapter](../area-relation.md) we saw that the area as a function of speed first decreases and then increases again after reaching a minimum. To see at which speed this minimal area occurs (or perhaps more naturally the other way around, what speed occurs at the minimal area) it is time to break out the calculus to differentiate the area function with respect to speed and find the speed where this equals zero.

First we rewrite the expression a little bit and drop the constant $\frac{\dot m}{\rho_0}$ since this only scales the area and doesn't change the location of  the minimum. Let us use $\alpha$ instead of $A$ since this techinically isn't the area anymore:

$$\alpha = u^{-1} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma}$$

Then we differentiate by $u$:

<details>

<summary>Full differentiation</summary>

The outermost operation is a product, so using the product rule, we get

$$\frac{d\alpha}{du} = \left(\frac{d}{du}u^{-1}\right) \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} + u^{-1} \left(\frac{d}{du} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma}\right)$$

The left derivative is simple:

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} + u^{-1} \left(\frac{d}{du} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma}\right)$$

For the other one we apply the chain rule:

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} + u^{-1} \left(\left(\frac{d}{dx} x^\frac{\gamma}{1 - \gamma} \right) \circ \left(1 - \frac{u^2}{2 c_p T_0}\right) \left(\frac{d}{du} \left(1 - \frac{u^2}{2 c_p T_0}\right)\right)\right)$$

Evaluating the left derivative:

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} + u^{-1} \left(\left(\frac{1}{1 - \gamma} x^\frac{\gamma}{1 - \gamma} \right) \circ \left(1 - \frac{u^2}{2 c_p T_0}\right) \left(\frac{d}{du} \left(1 - \frac{u^2}{2 c_p T_0}\right)\right)\right)$$

And composing the functions:

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} + u^{-1} \left(\frac{1}{1 - \gamma} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma} \left(\frac{d}{du} \left(1 - \frac{u^2}{2 c_p T_0}\right)\right)\right)$$

Then evaluating the last derivative:

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} - u^{-1} \frac{1}{1 - \gamma} \left(1- \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma} \frac{u}{c_p T_0}$$

The $u$'s cancel, and we get:

</details>

$$\frac{d\alpha}{du} = -u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} - \frac{1}{1 - \gamma} \left(1- \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma} \frac{1}{c_p T_0}$$

This is not a particularly pleasant formula, but let us see what we can do when we set it equal to zero:

$$-u^{-2} \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} - \frac{1}{1 - \gamma} \left(1- \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma} \frac{1}{c_p T_0} = 0$$

<details>

<summary>Full derivation</summary>

We start by moving one term to the other side and multiplying by $u^2$:

$$-\frac{1}{1 - \gamma} \left(1- \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{1 - \gamma} \frac{u^2}{c_p T_0} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma}$$

We then move the factors on the left-hand side that contain $u$ to the right by negating the exponent and flipping the fraction, respectively:

$$-\frac{1}{1 - \gamma} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^\frac{1}{1 - \gamma} \left(1- \frac{u^2}{2 c_p T_0}\right)^\frac{\gamma}{\gamma - 1} \frac{c_p T_0}{u^2}$$

We now have the product of two exponent with the same base, so we can instead add the exponents:

$$-\frac{1}{1 - \gamma} = \left(1 - \frac{u^2}{2 c_p T_0}\right)^{\frac{1}{1 - \gamma} + \frac{\gamma}{\gamma - 1}} \frac{c_p T_0}{u^2}$$

We then simplify the exponent:

$$\frac{1}{1 - \gamma} + \frac{\gamma}{\gamma - 1} \Rightarrow$$
$$\frac{1}{1 - \gamma} - \frac{\gamma}{1 - \gamma} \Rightarrow$$
$$\frac{1 - \gamma}{1 - \gamma} \Rightarrow$$
$$1$$

We see that the exponent is $1$, so we can just remove it to get:

$$-\frac{1}{1 - \gamma} = \left(1 - \frac{u^2}{2 c_p T_0}\right) \frac{c_p T_0}{u^2}$$

Almost there now. Distributing the fraction into the parentheses gets:

$$-\frac{1}{1 - \gamma} = \frac{c_p T_0}{u^2} - \frac{c_p T_0}{u^2} \frac{u^2}{2 c_p T_0}$$

A bunch of things cancel:

$$-\frac{1}{1 - \gamma} = \frac{c_p T_0}{u^2} - \frac{1}{2}$$

We move all the constant terms to the left side:

$$\frac{1}{2} - \frac{1}{1 - \gamma} = \frac{c_p T_0}{u^2}$$

Find a common denominator:

$$\frac{1 - \gamma - 2}{2 - 2\gamma} = \frac{c_p T_0}{u^2}$$

Simplify:

$$\frac{1}{2} \frac{\gamma + 1}{\gamma - 1} = \frac{c_p T_0}{u^2}$$

We then move $u^2$ to the left and the constants to the right:

$$u^2 = 2 c_p T_0 \frac{\gamma - 1}{\gamma + 1}$$

</details>

After rewriting a bit, we get:

$$u^2 = 2 c_p T_0 \frac{\gamma - 1}{\gamma + 1}$$

This is the speed (or well, the positive square root of this is) that the gas will have at the minimum area in the flow. As we see, it depends only on stagnation temperature and some constants.

Now just for fun and totally not because something remarkable happens (_wink, wink_), let us replace the stagnation temperature by its definition $T_0 = T + \frac{u^2}{2 c_p}$ (if you know anything about CD-nozzles already you might know where this is going):

$$u^2 = 2 c_p \left(T + \frac{u^2}{2 c_p}\right) \frac{\gamma - 1}{\gamma + 1}$$

<details>

<summary>All steps</summary>

Multiplying out the first parentheses we get:

$$u^2 = \left(2 c_p T + u^2\right) \frac{\gamma - 1}{\gamma + 1}$$

Then distributing the fraction into the pratheses:

$$u^{2} =2c_{p} T\frac{\gamma -1}{\gamma +1} +u^{2}\frac{\gamma -1}{\gamma +1}$$

And bringing all $u^2$ terms to the left-hand side:

$$u^{2} -u^{2}\frac{\gamma -1}{\gamma +1} =2c_{p} T\frac{\gamma -1}{\gamma +1}$$

We then collect terms:

$$u^{2}\left( 1-\frac{\gamma -1}{\gamma +1}\right) =2c_{p} T\frac{\gamma -1}{\gamma +1}$$

Simplify the fraction:

$$u^{2}\frac{2}{\gamma +1} =2c_{p} T\frac{\gamma -1}{\gamma +1}$$

And send it back to the other side:

$$u^{2} =2c_{p} T\frac{\gamma -1}{\gamma +1}\frac{\gamma +1}{2}$$

Some things cancel, and

</details>

After a bit of algebra, we get a nice and simple expression:

$$u^{2} = c_{p} T( \gamma - 1)$$

We can do a little bit better though. First, we distribute $c_p$ into the parentheses:

$$u^{2} = T (c_{p} \gamma -c_{p})$$

And now we do something seemingly uncalled for and pull a $\gamma$ out of the parentheses by simultaneously dividing each term inside by $\gamma$:

$$u^{2} =\gamma T\left( c_{p} -\frac{c_{p}}{\gamma }\right)$$

By the definition of gamma, $\gamma = \frac{c_p}{c_v}$, that reduces to:

$$u^{2} = \gamma T (c_{p} - c_{v})$$

This then lets us use Mayer's relation, which says that $c_p - c_v = R$, and in the end we get:

$$u^{2} = \gamma R T$$

This is the remarkable thing. The speed of sound in a gas $a$, is given by:

$$a^2 = \gamma R T$$

We see that it is exactly the same! The gas is traveling at the speed of sound at the minimum area! It is important to note that this is the _local_ speed of sound, because as we can see, the speed of sound depends on the temperature which falls when the speed rises.