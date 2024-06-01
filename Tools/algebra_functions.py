#!/bin/python
import numpy as np
import fractions


def invert_matrix(matrix):
    """Inverts a matrix.

    Args:
        matrix (list): A matrix to be inverted.


    Returns:
        list: The inverted matrix.
    """

    return np.linalg.inv(matrix)


def main():
    matrix = [
        [-2, 2, 3, 1],
        [2, 2, -1, 0],
        [1, -1, 1, 0],
        [-1, 2, 2, 0],
    ]

    print(invert_matrix(matrix))
    


if __name__ == "__main__":
    np.set_printoptions(
        formatter={"all": lambda x: str(fractions.Fraction(x).limit_denominator())}
    )
    main()
