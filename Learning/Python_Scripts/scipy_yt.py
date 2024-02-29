#!/bin/python

import numpy as np
from scipy.optimize import minimize


def product(x):
    result = 1
    for num in x:
        result *= num
    return result


def objective(x):
    return x[0] * x[3] * (x[0] + x[1] + x[2]) + x[2]


def constraint1(x):
    # f(x)>=0
    return product(x) - 25


def constraint2(x):
    # g(x) = 0
    sum_sq = 40
    sum_sq -= np.sum(np.square(x))

    return sum_sq


def youtube_example():
    x0 = [1, 5, 5, 1]
    b = (1.0, 5.0)
    bound_list = [b, b, b, b]

    con1 = {"type": "ineq", "fun": constraint1}
    con2 = {"type": "eq", "fun": constraint2}
    cons = [con1, con2]

    solution = minimize(
        objective, x0, method="SLSQP", bounds=bound_list, constraints=cons
    )
    print(solution)


def main():
    youtube_example()


if __name__ == "__main__":
    main()
