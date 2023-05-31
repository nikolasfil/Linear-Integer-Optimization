import pulp


def creating_variables(number, name="x", lowbound=None, upbound=None):
    if not lowbound and not upbound:
        return [pulp.LpVariable(name=f"{name}{i:02d}") for i in range(1,number+1)]

    elif not upbound and lowbound:
        return [
            pulp.LpVariable(name=f"{name}{i:02d}", lowBound=lowbound)
            for i in range(1,number+1)
        ]
    elif not lowbound and upbound:
        return [
            pulp.LpVariable(name=f"{name}{i:02d}", upBound=upbound) for i in range(1,number+1)
        ]
    else:
        return [
            pulp.LpVariable(name=f"{name}{i:02d}", lowBound=lowbound, upBound=upbound)
            for i in range(1,number+1)
        ]


def constraints_on_variables(x, y, state=None):
    result = x[0] * y[0]
    for i in range(1, len(x)):
        result += x[i] * y[i]

    if not state:
        return result
    if state == "eq":
        return result == y[-1]
    elif state == "laq":
        return result <= y[-1]
    elif state == "gaq":
        return result >= y[-1]

    elif state == "leq":
        return result < y[-1]
    elif state == "geq":
        return result > y[-1]

    # if not state:
    #     return result
    # if state == "eq":
    #     return sum(x[i] * y[i] for i in range(len(x))) == y[-1]
    # elif state == "laq":
    #     return result <= y[-1]
    # elif state == "gaq":
    #     return sum(x[i] * y[i] for i in range(len(x))) >= y[-1]

    # elif state == "leq":
    #     return sum(x[i] * y[i] for i in range(len(x))) < y[-1]
    # elif state == "geq":
    #     return sum(x[i] * y[i] for i in range(len(x))) > y[-1]


def printer(model, variables):
    print("-" * 50)
    print(f"status: {model.status}, {pulp.LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")
    print("-" * 50)
    for var in variables:
        print(f"{var.name}: {var.value()}")
    print("-" * 50)
    for x, constraint in model.constraints.items():
        print(f"""{x}: {constraint.value()}""")
    print("-" * 50)
