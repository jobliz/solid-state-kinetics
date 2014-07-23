import numpy as np
import matplotlib.pyplot as plt
from ssk import simulation, models
import sys

A = 10 ** 13
E = 100 * 1000
alpha = np.arange(0.01, 1, 0.03)
temps = [340, 345, 350, 355, 360]
rates = [1, 2, 4, 8]

times = [simulation.single_nonisothermal(models.iA2, A, E, alpha, b) for b in rates]
plots = [plt.plot(time, alpha)[0] for time in times]

plt.legend(plots, map(str, rates), loc="best")
plt.show()
