"""
There's nothing here as of yet.
"""

from __future__ import division
import functools
import numpy as np
from scipy.constants import R
from scipy.optimize import minimize

from ..ti import senumyang

__all__ = [
    'psi',
    'single_isothermal',
    'single_nonisothermal'
]

def psi(T, alphas, rate, A, Ea, g=None):
    """
    Objetive function for a single-step linear nonisothermal simulation.
    
    Parameters
    ----------
    T : int or float
        Absolute temperature (this will be the optimized value)
    alphas : ndarray
        Transformed fraction values.
    rate : float or int
        Linear heating rate.
    A : float or int
        Pre-exponential factor.
    E : float or int
        Activation energy (J/mol)
    
    Returns
    -------
    Single numerical value to be optimized. The closer this value is to zero, 
    the better.
    
    Notes
    -----
    Uses the Senum-Yang approximation for calculating the temperature 
    integral. Set g keyword argument with functools.partial.
    """
    x = Ea/(R*T)
    return np.abs((g(alphas) * (rate*R)/(A*Ea)) - senumyang(x))
   
def single_isothermal(model, A, E, alphas, T):
    """
    Simulates isothermal curves from a single model and given parameters
    
    Parameters
    ----------
    model : callable
        Integral form of a kinetic model.
    A : float or int
        Pre-exponential factor.
    E : float or int
        Activation energy (J/mol)
    alphas : ndarray
        Transformed fraction values.
    T : int or float
        Absolute temperature.
    
    Returns
    -------
    A list of simulated time steps sequentially associated with given
    trasformation fraction values.
    """
    return model(alphas) / A * np.exp(Ea/(R*T))

def single_nonisothermal(model, A, E, alphas, rate, T0=500, method="Nelder-Mead"):
    """
    Simulate a linear nonisothermal curve from a single model and given parameters 
    with an optimization procedure.
    
    Parameters
    ----------
    model : callable
        Integral form of a kinetic model.
    A : float or int
        Pre-exponential factor.
    E : float or int
        Activation energy (J/mol)
    alphas : ndarray
        Transformed fraction values.
    rate : float or int
        Linear heating rate.
    T0 : float or int
        Initial temperature guess.
    method : str or callable
        Proxy for optimize.minimize(method=value)
        
    Returns
    -------
    A list of simulated temperatures sequentially associated with given
    trasformation fraction values.
    
    References
    ----------
    #TODO
    """
    objfun = functools.partial(psi, g=model)
    output = [minimize(objfun, T0, args=(a, rate, A, E), method=method) for a in alphas]
    return [o.x for o in output]
