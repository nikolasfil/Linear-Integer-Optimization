import numpy as np

def solve_linear_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        print("The system is either singular or incompatible.")
        return None

# Example usage
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

solution = solve_linear_system(A, b)
if solution is not None:
    print("The solution is:")
    print(solution)