from __future__ import division
import numpy as np
from scipy.constants import R
from scipy.integrate import quad

__all__ = [
    'temp_integral', 
    'time_integral', 
    'senumyang', 
    'timeint'
]

def temp_integral(E, T):
    """Evaluates the temperature integral with numerical quadrature.
    
    Params
    ------
        E: Activation Energy (Joule/mol)
        T: Absolute Temperature (Kelvin)
    """
    x = E / (R*T)
    return E/R * quad(_inner_integral, np.inf, x)

def _inner_integral(x):
    """temp_integral's inner function"""
    return np.exp(x) / x**2

def time_integral():
    """A time version of the temperature integral for use in
       Vyazovkin's Method"""
    pass
        
def timeint(t, Ea, T):
    """Integral for vkin_iso"""
    return np.exp(-Ea / (R*T))

def senumyang(x):
    """Senum-Yang temperature integral approximation. x = Ea / (R*T)"""
    t1 = np.exp(-x) / x
    return t1 * (x**3 + 18*x**2 + 86*x + 96) / (x**4 + 20*x**3 + 120*x**2 + 240*x + 120) 
