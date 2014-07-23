import numpy as np

def kjma(t, n):
    pass # TODO

def sb(a, n=0, m=0, p=0):
    if p == 0:
        return a**n * (1-a)**m * (-np.log(1-a))**p
    else:
        return a**n * (1-a)**m
