#!/bin/python

from scipy.optimize import linprog
from scipy.optimize import minimize
import numpy as np


def example():
    c = [-1, 4]
    A = [[-3, 1], [1, 2]]
    b = [6, 4]
    x0_bounds = (None, None)
    x1_bounds = (-3, None)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
    print(res)


def dovetail():
    c = [3, 2]
    A = [[-1, -1], [-3, -1]]


# def youtube():
#     # https://www.youtube.com/watch?v=cXHvC_FGx24


def main():
    example()


if __name__ == "__main__":
    main()
