# NozzleMate

This is NozzleMate, a little program for calculating flow in and performance of rocket nozzles (converging-diverging nozzles).

NO CLAIMS ARE MADE ABOUT THE ACCURACY OF THIS PROGRAM

## Requirements

You wil need Python 3 with the `numpy`, `scipy` and `matplotlib` packages to run NozzleMate. Running `codegen.py` also requires `sympy`.

## Using

Input your nozzle and exhaust gas parameters in the top of `nozzlemate.py` and execute the file with Python:

```sh
python nozzlemate.py
```

### Interpreting results

A rocket nozzle operates in a few different regimes, here listed from high ambient pressure to low:

- No flow - ambient pressure is equal to the chamber pressure
- Unchoked - flow is locally subsonic throughout the nozzle, pressure is lowest at the throat and the exit pressure is equal to ambient pressure. Thrust will be very low and exhaust hot since the internal energy hasn't been converted to kinetic energy (speed).
- Choked and overexpanded - flow is locally sonic at the throat and supersonic after. The pressure and speed continue to respectively fall and rise in the diverging section. At higher ambient pressures (back pressures) a shock wave will occur inside the expanding part of the nozzle such that the exit pressure is equal to ambient pressure. This causes exit speed to drop to subsonic and performance will be bad. If the ambient pressure is low enough, this shockwave will occur outside the nozzle and exit flow will be supersonic and _lower pressure_ than ambient.
- Choked and matched - flow is locally sonic at the throat and supersonic after, exit pressure is equal to ambient pressure with no shock waves in the nozzles. This is the optimal condition for the nozzle.
- Choked and underexpanded - flow is locally sonic at the throat and supersonic after, exit pressure is higher than ambient. The exhaust plume will expand after leaving the nozzle. Performance is potentially left on the table.

NozzleMate will print to the terminal whether the flow is choked or not, and whether it is overexpanded, underexpanded or matched as well as where the shockwave ocurs in case of overexpanded flow. The thrust will also be calculated using the mass flow rate and exit speed.

The graphs show a cross-section of the nozzle (the displayed cross-section is used to generate the rest of the graphs, but only the throat and exit areas really matter) as well as how the pressure, Mach number, flow speed, temperature and density vary throughout the nozzle. The ambient pressure is marked with a horizontal dashed line.

## Planned features and todo

Future planned features in no particular order

- Load nozzle and gas parameters from files
- Iterative solution of actual stagnation/stagnation properties
- Calculation of nozzle geometry from defined flow conditions
- Clean up flow/thermodynamics related functions
- Calculation of exhaust gas temperature and properties from reactants

## Development

Certain flow-related functions are derived ahead-of-time with SymPy and used to generate Python functions. The derivation and generation happens in `codegen.py` and the generated functions end up in `relations.py`. These functions ar egenerally wrapped in other files to provide type hinting a bit nicer interface. (Some flow-related functions implemented directly in Python are also strewn about other files. This needs some cleanup.)
