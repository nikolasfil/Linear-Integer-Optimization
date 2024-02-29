import numpy as np

def identify_basic_variables(A, c):
    m, n = A.shape
    basic_variables = []

    for j in range(n):
        if np.count_nonzero(A[:, j]) == 1 and A[:, j].sum() == 1:
            i = np.argmax(A[:, j])
            if c[j] != 0:
                basic_variables.append((i, j))

    return basic_variables

def simplex_algorithm(A, c):
    m, n = A.shape
    tableau = np.hstack((A, np.eye(m)))
    objective = np.concatenate((c, np.zeros(m)))

    while True:
        entering_variable = np.argmax(objective[:-m])
        if objective[entering_variable] <= 0:
            break

        ratios = tableau[:, -m-1] / tableau[:, entering_variable]
        ratios[ratios <= 0] = np.inf
        leaving_variable = np.argmin(ratios)

        pivot_row = tableau[leaving_variable, :]
        tableau[leaving_variable, :] = pivot_row / pivot_row[entering_variable]

        for i in range(m):
            if i != leaving_variable:
                factor = tableau[i, entering_variable]
                tableau[i, :] -= factor * tableau[leaving_variable, :]

    basic_vars = identify_basic_variables(tableau[:, :-m], objective[:-m])
    return basic_vars

# Define the matrix A and the vector c
A = np.array([
    [3, 11, 9, -1, -29, 0, 0, 0, 0],
    [0, 1, 1, 1, -2, 1, 0, 0, 4],
    [-1, 1, -1, -2, -1, 0, 1, 0, 0],
    [1, 1, 1, 0, -3, 0, 0, 1, 1]
])
c = np.zeros(A.shape[1] - len(A))

basic_vars = simplex_algorithm(A, c)
for var in basic_vars:
    print(f"Row {var[0] + 1}, Column {var[1] + 1} is a basic variable.")
