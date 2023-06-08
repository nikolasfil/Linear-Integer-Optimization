import pulp
from useful_functions import creating_variables, constraints_on_variables,printer

def knapsackProblem(x,c,obj,name,sense):
    model = pulp.LpProblem(name=name, sense=sense)

    for i in range(len(c)):
        model += constraints_on_variables(x,c[i],'laq')

    # some math for traversing that one

    for i in [0,1,2,5]:
        # model+= constraints_on_variables(x,[1 if j==i else 0 for j in range(len(x))],'laq')
        model+= x[i] == 0 

    model += constraints_on_variables(x,obj)

    solver = pulp.GLPK_CMD(msg=0)
    model.solve(solver)

    printer(model)


def main():

    # --------- a --------- 
    x = creating_variables(7,lowbound=0,upbound=1)
    c = [ [3,4,3,3,15,13,16,35]]
    obj = [12,12,9,15,90,26,112]

    knapsackProblem(x,c,obj,"assignment5",pulp.LpMaximize)

    
 
if __name__ == "__main__":
    main()
