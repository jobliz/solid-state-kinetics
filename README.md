*This is a work in progress, in a very alpha stage*.

SSK: The Solid State Kinetics Toolbox.
===========

The Solid State Kinetics toolbox provides a collection of functions for numerical 
work in solid state kinetics. It currently features:

* Common general reaction models (Avrami, Geometrical, etc)
* Temperature integral evaluation and approximations (Senum-Yang)
* Easy single-step reaction simulation (just set model, Ea and A)
* Isoconversional analysis methods (Ozawa-Flynn-Wall, Nonlinear (Vyazovkin), etc).

Dependencies are just the python numerical stack (numpy, scipy and matplotlib). 
The code was developed directly from the formulae on the literature:

* [Basics and applications of solid-state kinetics: A pharmaceutical perspective](http://onlinelibrary.wiley.com/doi/10.1002/jps.20559/abstract)
* [ICTAC Kinetics Committee recommendations for performing kinetic computations on thermal analysis data](http://www.sciencedirect.com/science/article/pii/S0040603111002152)

Emails regarding this topic will be very appreciated. For full disclosure: I'm
an "information engineering" (fancy name for computer science) student, not a 
physics or materials science specialist. If you find errors or have suggestions
pertaining the code, please let me know.

TODO List:
* Clean code up (parts are messy)
* Fix multiple isoconversional method implementations.
* Test nonisothermal simulation code with more examples.
* Do a proper setup.py for uploading module to PyPi.
