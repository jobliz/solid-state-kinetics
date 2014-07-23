import numpy as np

__all__ = ['returnarray']

def returnarray(func):
    """decorator: wraps generator expression to return a ndarray"""
    def new(*args, **kwargs):
        return np.array(list(func(*args, **kwargs)))
    new.func_doc = func.func_doc
    new.original = func
    return new
