import pulp

# pip install pulp
# apt install glpk-utils


def mul(x, y, state=None):
    if not state: 
        return sum([x[i] * y[i] for i in range(len(x))])
    if state == "eq":
        return sum(x[i] * y[i] for i in range(len(x))) == y[-1]
    elif state == "laq":
        return sum([x[i] * y[i] for i in range(len(x))]) <= y[-1]
    elif state == "gaq":
        return sum(x[i] * y[i] for i in range(len(x))) >= y[-1]

    elif state == "leq":
        return sum(x[i] * y[i] for i in range(len(x))) < y[-1]
    elif state == "geq":
        return sum(x[i] * y[i] for i in range(len(x))) > y[-1]


def main_universal():
    model = pulp.LpProblem(name="assignment1a", sense=pulp.LpMaximize)

    x = [pulp.LpVariable(name=f"x{i+1}", lowBound=0) for i in range(4)]

    c = [[1, 3, 0, 1, 8], [2, 1, 0, 0, 6], [0, 2, 4, 1, 6]]

    obj = [2, 4, 1, 1]

    model += sum([(mul(x, c[i], "laq")) for i in range(len(c))])
    model += mul(x,obj)

    solver = pulp.GLPK_CMD()
    status = model.solve(solver)

    print('-'*50)
    print(f"status: {model.status}, {pulp.LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")
    print('-'*50)
    for var in x:
        print(f"{var.name}: {var.value()}")
    print('-'*50)
    
    for x,constraint in model.constraints.items():
        print(f"""{x}: {constraint.value()}""")



def main_a(x,c,obj):
    model = pulp.LpProblem(name="assignment1a", sense=pulp.LpMaximize)

    for i in range(len(c)):
        model += mul(x,c[i],'laq')
    model += mul(x,obj)

    solver = pulp.GLPK_CMD(msg=0)
    status = model.solve(solver)

    print('-'*50)
    print(f"status: {model.status}, {pulp.LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")
    print('-'*50)
    for var in x:
        print(f"{var.name}: {var.value()}")
    print('-'*50)
    for x,constraint in model.constraints.items():
        print(f"""{x}: {constraint.value()}""")
    print('-'*50)


def main():
    model = pulp.LpProblem(name="assignment1a", sense=pulp.LpMaximize)

    x = [pulp.LpVariable(name=f"x{i+1}", lowBound=0) for i in range(4)]
    c = [[1, 3, 0, 1, 8], [2, 1, 0, 0, 6], [0, 2, 4, 1, 6]]
    obj = [2, 4, 1, 1]


    for i in range(len(c)):
        model += mul(x,c[i],'laq')
    model += mul(x,obj)

    solver = pulp.GLPK_CMD(msg=0)
    status = model.solve(solver)

    print('-'*50)
    print(f"status: {model.status}, {pulp.LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")
    print('-'*50)
    for var in x:
        print(f"{var.name}: {var.value()}")
    print('-'*50)
    for x,constraint in model.constraints.items():
        print(f"""{x}: {constraint.value()}""")
    print('-'*50)



def main_b():
    model = pulp.LpProblem(name='assignment1b',sense=pulp.LpMaximize)





if __name__ == "__main__":
    # main_a()
    main()
