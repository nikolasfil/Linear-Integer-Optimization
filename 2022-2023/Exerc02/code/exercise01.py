import pulp
from useful_functions import creating_variables, constraints_on_variables, printer


def solver(x, c, obj, name, sense):
    model = pulp.LpProblem(name=name, sense=sense)

    for i in range(len(c)):
        model += constraints_on_variables(x, c[i], "laq")
    model += constraints_on_variables(x, obj)

    solver = pulp.GLPK_CMD(msg=0)
    model.solve(solver)

    printer(model=model)


def main_a():
    global x,c,obj
    # --------- a ---------
    x = creating_variables(4, lowbound=0)
    c = [[1, 3, 0, 1, 8], [2, 1, 0, 0, 6], [0, 2, 4, 1, 6]]
    obj = [2, 4, 1, 1]

    solver(x, c, obj, "assignment1a", pulp.LpMaximize)

    print(f'{" | ".join([x[i].name for i in range(len(x))])} \n')
    for i in range(len(c)):
        print(f"{'  | '.join([str(c[i][j]) for j in range(len(c[i])-1)])} \n")

def main_b():
    # --------- b ---------
    # Ευρευση του διαστηματος αντοχης, βελτιστο πινακα and other shit

    print("Disrupting x2")
    for g in range(-5, 6):
        obj[1] = obj[1] + g

        solver(x, c, obj, "assignment1b", pulp.LpMaximize)

    print("Disrupting x3")
    for g in range(-5, 6):
        obj[2] = obj[2] + g

        solver(x, c, obj, "assignment1b", pulp.LpMaximize)

def main_c():

    # ----------- c --------------

    print("Disrupting x2")
    for g in range(-5, 6):
        c[0][-1] = c[0][-1] + g

        solver(x, c, obj, "assignment1c", pulp.LpMaximize)

    print("Disrupting x3")
    for g in range(-5, 6):
        c[1][-1] = c[1][-1] + g

        solver(x, c, obj, "assignment1c", pulp.LpMaximize)

def main_d():

    # -------- d ----------

    y = creating_variables(3, "y", lowbound=0)
    c = []
    obj = []

    # solver(y,c,obj,'assignment1d',pulp.LpMinimize)

def main():
    main_a()
    # main_b()
    # main_c()
    # main_d()

if __name__ == "__main__":
    main()
