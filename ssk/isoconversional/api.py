"""
isoconversional module implementation notes.

* nonlinear depends on _vkin_multiple.

* linear methods use helpers.returnarray for automatically transforming
  generators into ndarrays. 
"""

from __future__ import division
import functools
import itertools
import numpy as np
from scipy.constants import R
from scipy.stats import linregress
from scipy.optimize import minimize
from scipy.integrate import quad

from ..helpers import returnarray
from ..ti import senumyang, timeint # doyle

__all__ = [
    'ii_standard',
    'ni_ofw',
    'nonlinear'
]

@returnarray
def ii_standard(times, temps):
    """
    Isothermal, Integral: Standard isoconversional method
    """
    x = [1/T for T in temps]
    for n in range(len(times[0])):
        y = [-np.log(t[n]) for t in times]
        s, i, r, p, e = linregress(x, y)
        yield -s * R, i, r, p, e

@returnarray
def ni_ofw(rates, temps):
    """
    Non-isothermal, Integral: Ozawa-Flynn-Wall isoconversional method.
    It uses Doyle's approximation.
    """
    y = np.log(rates)
    for n in range(len(temps[0])):
        x = [1/T[n] for T in temps]
        s, i, r, p, e = linregress(x, y)
        yield -s * R / .457, i, r, p, e
 
def nonlinear(eas, t1, t2, kind="First", optimizer="Powell", verbose=False):
    """
    Non-linear isoconversional method (Vyazovkin's Method).
    
    First: Linear heating using Senum & Yang's approximation.
    Isothermal: The modified method, adapted for isothermal conditions.
    """
    if kind == "First":
        return minimize(_vkin_fast, eas, args=(t1, t2), method=optimizer)
    elif kind == "Isothermal":
        return minimize(_vkin_mod_iso, eas, args(t1, t2), method=optimizer)
    else:
        raise NotImplementedError("kind parameter not recognized")
 
def _vkin_multiple(eas, t1, t2, kind="Fast", verbose=False):
    total = 0
    
    for n, Ea in enumerate(eas):
        for i, j in itertools.permutations(range(len(t1)), 2):
            
            if kind == "Fast":
                b = t1; T = t2
                Iai = senumyang(Ea / (R * T[i][n]))
                Iaj = senumyang(Ea / (R * T[j][n]))
                total += (b[j] * Iai) / (b[i] * Iaj)
            
            elif kind == "Isothermal":
                times = t1; temps = t2
                Jai = quad(timeint, 0, times[i][n], args=(Ea, temps[i]))
                Jaj = quad(timeint, 0, times[j][n], args=(Ea, temps[j]))
                total += Jai[0] / Jaj[0]
            
            else:
                raise NotImplementedError
    
    if verbose:
        print total, eas
    
    return total
 
def _vkin_fast(eas, b, T):
    """
    Vyazovkin's first isoconventional method (objective function) for linear
    non-isothermal reactions. Uses Senum-Yang's approximation.
    """
    total = 0
    for n, Ea in enumerate(eas):
        for i, j in itertools.permutations(range(len(b)), 2):
            Iai = senumyang(Ea / (R * T[i][n]))
            Iaj = senumyang(Ea / (R * T[j][n]))
            total += (b[j] * Iai) / (b[i] * Iaj)
    return total

def _timeint(t, Ea, T):
    """Integral for vkin_iso"""
    return np.exp(-Ea / (R*T))

def _vkin_mod_iso(eas, times, temps):
    total = 0
    for n, Ea in enumerate(eas):
        for i, j in itertools.permutations(range(len(temps)), 2):
            Jai = quad(timeint, 0, times[i][n], args=(Ea, temps[i]))
            Jaj = quad(timeint, 0, times[j][n], args=(Ea, temps[j]))
            total += Jai[0] / Jaj[0]
    print total, eas
    return total            

def _vkin_mod_iso2(eas, times, temps):
    total = 0
    for n, Ea in enumerate(eas):
        for i, j in itertools.permutations(range(len(temps)), 2):
            Jai = quad(timeint, 0, times[i][n], args=(Ea, temps[i]))
            Jaj = quad(timeint, 0, times[j][n], args=(Ea, temps[j]))
            total += Jai[0] / Jaj[0]
    print total, eas
    return total
