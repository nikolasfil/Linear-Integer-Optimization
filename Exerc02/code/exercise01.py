import pulp
from useful_functions import creating_variables, constraints_on_variables, printer
# pip install pulp
# apt install glpk-utils



def main_a(x,c,obj,name,sense):
    model = pulp.LpProblem(name=name, sense=sense)

    for i in range(len(c)):
        model += constraints_on_variables(x,c[i],'laq')
    model += constraints_on_variables(x,obj)

    solver = pulp.GLPK_CMD(msg=0)
    model.solve(solver)

    printer(model=model,variables=x)



def main():

    # --------- a --------- 
    x = creating_variables(4,lowbound=0)
    c = [[1, 3, 0, 1, 8], [2, 1, 0, 0, 6], [0, 2, 4, 1, 6]]
    obj = [2, 4, 1, 1]

    main_a(x,c,obj,"assignment1a",pulp.LpMaximize)

    # --------- b ---------
    # Ευρευση του διαστηματος αντοχης, βελτιστο πινακα and other shit 
    
    print('Disrupting x2')
    for g in range(-5,6):
        obj[1] = obj[1] + g
        
        main_a(x,c,obj,'assignment1b',pulp.LpMaximize)

    print('Disrupting x3')
    for g in range(-5,6):
        obj[2] = obj[2] + g
        
        main_a(x,c,obj,'assignment1b',pulp.LpMaximize)

    # ----------- c -------------- 

    

    print('Disrupting x2')
    for g in range(-5,6):
        c[0][-1] = c[0][-1] + g
        
        main_a(x,c,obj,'assignment1c',pulp.LpMaximize)

    print('Disrupting x3')
    for g in range(-5,6):
        c[1][-1] = c[1][-1] + g
        
        main_a(x,c,obj,'assignment1c',pulp.LpMaximize)


    # -------- d ----------

    y = creating_variables(3,'y',lowbound=0)
    c = []
    obj = []

    # main_a(y,c,obj,'assignment1d',pulp.LpMinimize)



if __name__ == "__main__":
    main()
