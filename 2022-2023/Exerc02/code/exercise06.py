import pulp
from useful_functions import creating_variables, constraints_on_variables, printer


def managers_problem():
    model = pulp.LpProblem(name="assignment6", sense=pulp.LpMaximize)
    x = creating_variables( 10, lowbound=0, upbound=1)

    # I need to put my own constraints here
    Q = 10000
    C = [ 3, 12, 13,  49, 666,  420, 33, 6973, 23, 1339, Q]
    P = [19, 41, 58, 123, 888, 6942, 88, 7076, 32, 4000]

    constraints = [
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1,-1,-1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 4],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2],
        C
    ]

    equalities = ["laq", "laq", "gaq", "laq", "gaq",'laq']

    for i in range(len(constraints)):
        model += constraints_on_variables(x, constraints[i], equalities[i])
        # print(f"{constraints_on_variables(x, constraints[i], equalities[i])}")

    model += constraints_on_variables(x, P)
    # print(constraints_on_variables(x, P))

    model.solve()
    printer(model)


if __name__ == "__main__":
    managers_problem()
