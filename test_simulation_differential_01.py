from __future__ import division
import math
import numpy as np
from ssk import models
from scipy.constants import R
from scipy.integrate import ode, odeint
import itertools
import matplotlib.pyplot as plt
import sys
import ssk

def F1(a):
    return 1 - a

def f(T, y, b, A1, E1, A2, E2):
    k = ssk.simulation.ni_rates(b, T, A1, E1, A2, E2)
    a0, a1, a2 = y
    da0 = k[0] * F1(a0)
    da1 = k[1] * (1- F1(a0) -a1)
    return [da0, da1, (da0+da1)/2]
 
rates = [2, 4, 8, 16]
constants = [900 * 60, 58.5 * 1000, 5 * 10**8 * 60, 125.4 * 1000]

for b in rates:
    params = [b] + constants
    temps, alphas = ssk.simulation.ni_integrate(f, 400, args=params, T1=700)
    plt.plot(temps, alphas)
    
plt.show()
