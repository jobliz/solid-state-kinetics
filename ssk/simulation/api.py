"""
Most functions on this submodule straightfoward and independent one of each 
other.

* single_isothermal depends on psi
* ni_integrate works with a user-made function that can be simplified by
  using ni_rates
"""

from __future__ import division
import math
import itertools
import functools
import numpy as np
from scipy.constants import R
from scipy.optimize import minimize
from scipy.integrate import ode

from ..ti import senumyang

__all__ = [
    'psi',
    'single_isothermal',
    'single_nonisothermal',
    'ni_rates',
    'ni_integrate'
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
    
def ni_rates(*args):
    """
    Calculates non-isothermal rate constants. Parameter format is
    [b, T, A1, E1, A2, E2, A3, E3...]
    
    Parameters (*args) all int or float
    ----------------------------------
    [0]   : Heating rate (b)
    [1]   : Actual temperature
    [n]   : Pre-exponential factor
    [n+1] : Activation Energy
    
    Returns
    -------
    k : iterable
        List of rate constants for given non-isothermal step
    """
    
    b, T, A, E = args[0], args[1], [], []
    cycle = itertools.cycle([A, E])
    
    for arg in args[2:]:
        cycle.next().append(arg)
    
    K = []
    for n, _ in enumerate(A):
        K.append(A[n]/b * math.exp(-E[n]/(R*T)))
        
    return K

def ni_integrate(func, T0, args=None, dT=1, T1=None, verbose=False):
    """
    Integrate a non-isothermal composite kinetic model.
    
    Parameters
    ----------
    func : callable
        Model function
    T0 : int or float
        Startint temperature (in Kelvins)
    args : iterable
        Heating rate followed by A, E pairs.
    dT : int or float
        Temperature step size
    T1 : int or float (optional)
        Force final simulation temperature to this value.
    verbose : boolean (optional)
        Print results from every integration step
        
    Returns
    -------
    temps : iterable
        Temperature list.
    alphas: iterable
        Transformation fraction list.
    """
    
    n = math.ceil(len(args[2:]) / 2) + 1
    r = ode(func).set_integrator('zvode', method='bdf', with_jacobian=False)
    r.set_initial_value(np.zeros(n), T0).set_f_params(*args)
    temps, alphas = [], []
    
    while r.successful():
        r.integrate(r.t+dT)
        
        if verbose:
            print r.t, r.y
        
        # work until alpha == 1
        if not T1: 
            if r.y[n-1] < 1: # last y position should be total transformed fraction
                temps.append(r.t)
                alphas.append(r.y[n-1])
            else:
                break
        
        # work until given last temperature (long graph style)
        else:      
            if r.t < T1:
                temps.append(r.t)
                alphas.append(r.y[n-1])
            else:
                break
                
    return temps, alphas
