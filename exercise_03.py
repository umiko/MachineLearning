import numpy as np
import matplotlib.pyplot as plt


def f(data):
    return data[0] ** 2 + 2 * data[1] ** 2


def fDeriv(data):
    return 2 * data[0] + 4 * data[1]


def gradientDesc(start, steps, size):
    for x in range(steps):
        break

