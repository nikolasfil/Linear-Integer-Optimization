def matrix_creator(obj, constraints):
    """Creates a matrix for branch and bound.

    Args:
        obj (list): The objective function.
        constraints (list): The constraints.

    Returns:
        list: The matrix.
    """

    matrix = []

    for i, value in enumerate(obj):
        temp = [i, value, constraints[i], value / constraints[i], None]
        matrix.append(temp)

    matrix = sorted(matrix, key=lambda x: x[3], reverse=True)
    for i in range(len(matrix)):
        matrix[i][-1] = i

    return matrix


def main():
    obj = [23, 17, 30, 14, 9]
    constraints = [6, 5, 10, 7, 5]
    matrix = matrix_creator(obj, constraints)
    for item in matrix:
        print(item)


if __name__ == "__main__":
    main()
