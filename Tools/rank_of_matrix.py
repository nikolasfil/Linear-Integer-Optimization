import numpy as np

def find_rank(A):
    rank = 0
    m, n = A.shape
    for i in range(m):
        if np.count_nonzero(A[i]) > 0:
            rank += 1
            for j in range(i+1, m):
                ratio = A[j, i] / A[i, i]
                A[j] -= ratio * A[i]
    return rank

def find_rank_augmented(A, b):
    augmented_matrix = np.hstack((A, b))
    rank = np.linalg.matrix_rank(augmented_matrix)
    return rank

    