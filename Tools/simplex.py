import numpy as np

def simplex(c, A, b):
    m, n = A.shape

    # Add slack variables to convert inequalities to equations
    c = np.concatenate((c, np.zeros(m)))
    A = np.hstack((A, np.eye(m)))
    basis = np.arange(n, n + m)

    while True:
        # Compute the reduced cost coefficients
        c_b = c[basis]
        c_n = c - np.dot(c_b, A[:, basis])
        
        # Check for optimality
        if np.all(c_n >= 0):
            x = np.zeros(n)
            x[basis] = np.linalg.solve(A[:, basis], b)
            return x
        
        # Choose entering variable
        entering = np.argmin(c_n)
        
        # Compute the direction
        d = np.linalg.solve(A[:, basis], A[:, entering])
        
        # Check for unboundedness
        if np.all(d <= 0):
            return None
        
        # Choose leaving variable
        ratios = np.divide(b, np.dot(A[:, basis], d))
        leaving = np.argmin(ratios)
        
        # Update basis
        basis[leaving] = entering

# Example usage
c = np.array([-2, -3, -4])  # Coefficients of the objective function
A = np.array([[3, 2, 1], [2, 5, 3], [4, 1, 2]])  # Coefficients of the constraints
b = np.array([10, 15, 18])  # RHS of the constraints

x = simplex(c, A, b)
if x is not None:
    print("Optimal solution found:")
    print(x)
else:
    print("Problem is unbounded.")
