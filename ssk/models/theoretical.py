from __future__ import division
import numpy as np

def iP2(a):
    return a**(1/2)

def iP3(a):
    return a**(1/3)

def iP4(a):
    return a**(1/4)

def iPN(a, n=None):
    return a**(1/n)

def iA2(a):
    return (-np.log(1-a))**(1/2)
    
def iA3(a):
    return (-np.log(1-a))**(1/3)

def iA4(a):
    return (-np.log(1-a))**(1/4)

def iAN(a, n=None):
    return (-np.log(1-a))**(1/n)
    
def iB1(a):
    return np.log(a/(1-a))

def iR2(a):
    return 1 - (1 - a)**(1/2) 

def iR3(a):
    return 1 - (1 - a)**(1/3) 

def iD1(a):
    return a**2

def iD2(a):
    return ((1-a) * np.log(1-a)) + a

def iD3(a):
    return (1 - (1-a)**(1/3)) ** 2

def iD4(a):
    return 1 - (2*a/3) - (1-a)**(2/3)

def iF1(a):
    return -np.log(1-a)

def iF2(a):
    return (1-a)**-1 - 1

def iF3(a):
    return 0.5 * ((1-a)**-2 - 1)

def dP2(a):
    return 2*a**(1/2)

def dP3(a):
    return 3*a**(2/3)

def dP4(a):
    return 4*a**(3/4)

def dA2(a):
    return 2 * (1-a) * (-np.log(1-a))**(1/2)

def dA3(a):
    return 3 * (1-a) * (-np.log(1-a))**(2/3)

def dA4(a):
    return 4 * (1-a) * (-np.log(1-a))**(3/4)

def dB1(a):
    return a * (1-a)

def dR2(a):
    return 2 * (1-a)**(1/2)

def dR3(a):
    return 3 * (1-a)**(2/3)

def dD1(a):
    return 0.5 * a**-1

def dD2(a):
    return (-np.log(1-a))**-1

# In doubt for Combined Kinetic Analysis...
def dD3_old(a):
    return 3 * (1-a)**(2/3)

def dD3(a):
    t1 = 3 * (1-a)**(2.0/3)
    t2 = 2 * (1 - (1-a)**(1.0/3))
    return t1 / t2
    
def dD4(a):
    return (3/2 *  (((1-a)**(-1/3))-1)  )

def dF1(a):
    return (1-a)

def dF2(a):
    return (1-a)**2

def dF3(a):
    return (1-a)**3
