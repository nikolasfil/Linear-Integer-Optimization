import numpy as np

def simplex(c_obj, A_eq, b_eq):
    num_constraints, num_variables = A_eq.shape
    tableau = np.zeros((num_constraints + 1, num_variables + num_constraints + 1))
    
    tableau[:num_constraints, :num_variables] = A_eq
    tableau[:num_constraints, num_variables:] = np.eye(num_constraints)
    tableau[num_constraints, :num_variables] = c_obj
    
    while np.any(tableau[-1, :-1] < 0):
        entering_variable_col = np.argmin(tableau[-1, :-1])
        pivot_row = np.argmin(tableau[:-1, -1] / tableau[:-1, entering_variable_col])
        
        pivot_value = tableau[pivot_row, entering_variable_col]
        tableau[pivot_row, :] /= pivot_value
        
        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, entering_variable_col] * tableau[pivot_row, :]
    
    optimal_solution_value = tableau[-1, -1]
    optimal_solution = tableau[:-1, -1]
    
    return optimal_solution_value, optimal_solution

# Example usage
c_obj = np.array([-3, -5])
A_eq = np.array([[1, 0], [0, 2], [3, 2]])
b_eq = np.array([4, 12, 18])

optimal_solution_value, optimal_solution = simplex(c_obj, A_eq, b_eq)

print("Optimal solution value:", optimal_solution_value)
print("Optimal solution:", optimal_solution)
