import pulp
import numpy as np


def creating_variables(number, name='x',lowbound=None,upbound=None):
    if lowbound is None and upbound is None:
        return [pulp.LpVariable(name=f"{name}{i+1}") for i in range(number)]

    elif upbound is None and lowbound is not None:
        return [pulp.LpVariable(name=f"{name}{i+1}", lowBound=lowbound) for i in range(number)]

    elif lowbound is None and upbound is not None:
        return [pulp.LpVariable(name=f"{name}{i+1}", upBound=upbound) for i in range(number)]

    elif lowbound is not None and upbound is not None:
        return [pulp.LpVariable(name=f"{name}{i+1}", lowBound=lowbound,upBound=upbound) for i in range(number)]



def constraints_on_variables(x, y, state=None):
    if not state: 
        return sum([x[i] * y[i] for i in range(len(x))])
    if state == "eq":
        return sum([x[i] * y[i] for i in range(len(x))]) == y[-1]
    elif state == "laq":
        return sum([x[i] * y[i] for i in range(len(x))]) <= y[-1]
    elif state == "gaq":
        return sum([x[i] * y[i] for i in range(len(x))]) >= y[-1]
    elif state == "leq":
        return sum([x[i] * y[i] for i in range(len(x))]) < y[-1]
    elif state == "geq":
        return sum([x[i] * y[i] for i in range(len(x))]) > y[-1]



def printer(model):
    print('-'*50)
    print(f"status: {model.status}, {pulp.LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")
    print('-'*50)
    for var in model.variables():
        print(f"{var.name}: {var.value()}")
    print('-'*50)
    for x,constraint in model.constraints.items():
        print(f"""{x}: {constraint.value()}""")
    print('-'*50)


def identify_basic_variables(matrix):
    """Identify the basic variables of a matrix.
        matrix is the constraints and the results all in one"""
    num_rows, num_cols = matrix.shape
    basic_variables = []

    for col in range(num_cols):
        if np.count_nonzero(matrix[:, col]) == 1:
            row_idx = np.argmax(matrix[:, col])
            basic_variables.append((row_idx, col))

    return basic_variables