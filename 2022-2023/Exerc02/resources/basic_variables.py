import numpy as np


def identify_basic_variables(matrix):
    num_rows, num_cols = matrix.shape
    basic_variables = []

    for col in range(num_cols):
        if np.count_nonzero(matrix[:, col]) == 1:
            row_idx = np.argmax(matrix[:, col])
            basic_variables.append((row_idx, col))

    return basic_variables


# Example usage
# A = np.array([[1, 2, 0, 1, 0],
#               [0, 1, 1, 0, 1],
#               [0, 1, 0, 2, 3]])


# A = np.array([[3,2,0,0,0,0,0],
#               [1,1,1,0,0,0,9],
#               [3,1,0,1,0,0,18],
#               [1,0,0,0,1,0,7],
#               [0,1,0,0,0,1,6]])


A = np.array(
    [
        [ 3, 11,  9, -1, -29, 0, 0, 0, 0],
        [ 0,  1,  1,  1,  -2, 1, 0, 0, 4],
        [-1,  1, -1, -2,  -1, 0, 1, 0, 0],
        [ 1,  1,  1,  0,  -3, 0, 0, 1, 1],
    ]
)


basic_vars = identify_basic_variables(A)
for var in basic_vars:
    print(f"Row {var[0] + 1}, Column {var[1] + 1} is a basic variable.")
