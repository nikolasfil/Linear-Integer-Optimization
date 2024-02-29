import numpy as np

def identify_basic_variables(matrix):
    num_rows, num_cols = matrix.shape
    basic_variables = []

    for col in range(num_cols):
        if np.count_nonzero(matrix[:, col]) == 1:
            row_idx = np.argmax(matrix[:, col])
            basic_variables.append((row_idx, col))

    return basic_variables

# Create the matrix A and the vector c
A = np.array([[0, 1, 1, 1, -2],
              [-1, 1, 1, 2, 1],
              [1, 1, 1, 0, -3]])
c = np.array([-3, -11, -9, 1, 29])






# Add slack variables to the matrix A
slack_variables = np.eye(3)
slack_variables = np.hstack((slack_variables, np.zeros((3, 1))))
A = np.hstack((A[:, :-1], slack_variables))

# Combine the matrix A and the vector c
matrix = np.vstack((A.T, c))

basic_vars = identify_basic_variables(matrix.T)
for var in basic_vars:
    print(f"Row {var[0] + 1}, Column {var[1] + 1} is a basic variable.")
