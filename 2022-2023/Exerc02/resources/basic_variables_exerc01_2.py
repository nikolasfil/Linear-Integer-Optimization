import numpy as np
from scipy.optimize import linprog

# Define the matrix A
# A = np.array([
#     [3, 11, 9, -1, -29, 0, 0, 0, 0],
#     [0, 1, 1, 1, -2, 1, 0, 0, 4],
#     [-1, 1, -1, -2, -1, 0, 1, 0, 0],
#     [1, 1, 1, 0, -3, 0, 0, 1, 1]
# ])


A = np.array(
    [
        [ 3, 11,  9, -1, -29, 0],
        [ 0,  1,  1,  1,  -2, 4],
        [-1,  1, -1, -2,  -1, 0],
        [ 1,  1,  1,  0,  -3, 1],
    ]
)



# Extract the number of variables and constraints
num_vars = A.shape[1] - len(A) - 1

# Formulate the minimization problem
c = np.zeros(num_vars)
bounds = [(0, None)] * num_vars
res = linprog(c, A_ub=A[1:, :num_vars], b_ub=A[1:, -1], bounds=bounds, method="simplex")

# Retrieve the basic variables
basic_vars = []
for i, x in enumerate(res.x):
    if x != 0:
        basic_vars.append(i + 1)

print("Basic variables:", basic_vars)
