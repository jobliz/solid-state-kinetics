"""
The Solid State Kinetics (ssk) toolbox.

Submodules:

* ti: The temperature integral itself and some approximations.
    - Senum-Yang
    - Doyle
  
* alpha: Functions for getting transformed fraction values from experimental
  data.
    - Simple thermogravimetric formula.
    - Area Under Curve (AUC)
  
* models: Kinetic models, including:
    - Reaction order (F)
    - Nucleation/Growth (A)
    - Geometrical contraction (R)
    - Diffusion (D)
    - Sestak-Berggren
    - Kolmogorov-Johnson-Mehl-Avrami 
    
* isoconversional: Isoconversional methods:
    - Standard (Isothermal, Integral)
    - Ozawa-Flynn-Wall (Non-isothermal, Integral)
    - Nonlinear (Vyazovkin)

* simulation: Single-step reaction simulation.

* helpers: Miscellaneous functions.
"""

# Submodule imports
import ti
import alpha
import models
import helpers
import simulation
import isoconversional

