from __future__ import division
import numpy as np
from scipy import integrate

__all__ = ['area', 'simple']

def simple(p):
    pass

def area(p):
    cumul = np.hstack(([0], integrate.cumtrapz(np.abs(np.gradient(p)))))
    return cumul / max(cumul)
    

