import numpy as np


class SimplexAlgorithm:
    def __init__(self, c, A, b):
        self.c = c  # coefficients of the objective function
        self.A = A  # constraint matrix
        self.b = b  # right-hand side vector
        self.m, self.n = A.shape  # dimensions of the constraint matrix

    def initialization(self):
        # Initialize basic and non-basic variable indices
        self.cbIndx = np.arange(self.n, self.n + self.m)
        self.cnIndx = np.arange(0, self.n)

        # Initial basic feasible solution
        self.xB = self.b
        self.xN = np.zeros(self.n)

    def perform_gauss_elimination(self):
        # Perform Gaussian elimination
        # Step 1: Update tableau
        B_inv = np.linalg.inv(self.A[:, self.cbIndx])
        self.tableau = np.hstack(
            (np.eye(self.m), B_inv, np.expand_dims(np.dot(B_inv, self.b), axis=1))
        )

        # Step 2: Update cost coefficients
        cB = self.c[self.cbIndx]
        cN = self.c[self.cnIndx]
        self.revised_cN = cN - np.dot(cB, B_inv) @ self.A[:, self.cnIndx]

        # Step 3: Update objective value
        self.objective_value = np.dot(cB, np.dot(B_inv, self.b))

    def select_entering_variable(self):
        # Select entering variable
        entering_variable_index = np.argmax(self.revised_cN)
        return entering_variable_index

    def calculate_theta(self, entering_variable_index):
        # Calculate theta
        theta_values = []
        for i in range(self.m):
            if self.tableau[i, entering_variable_index] > 0:
                theta = self.xB[i] / self.tableau[i, entering_variable_index]
                theta_values.append(theta)
            else:
                theta_values.append(np.inf)
        return np.argmin(theta_values)

    def pivot_operation(self, entering_variable_index, exiting_variable_index):
        # Perform pivot operation
        pivot_element = self.tableau[exiting_variable_index, entering_variable_index]
        self.tableau[exiting_variable_index, :] /= pivot_element
        for i in range(self.m):
            if i != exiting_variable_index:
                multiplier = self.tableau[i, entering_variable_index]
                self.tableau[i, :] -= (
                    multiplier * self.tableau[exiting_variable_index, :]
                )
        self.cbIndx[exiting_variable_index] = entering_variable_index

    def solve(self):
        self.initialization()
        self.perform_gauss_elimination()

        while True:
            entering_variable_index = self.select_entering_variable()
            if self.revised_cN[entering_variable_index] <= 0:
                print("Optimal solution found.")
                break

            exiting_variable_index = self.calculate_theta(entering_variable_index)
            if np.isinf(exiting_variable_index):
                print("Unbounded problem.")
                break

            self.pivot_operation(entering_variable_index, exiting_variable_index)
            self.perform_gauss_elimination()

        return self.tableau[:, -1]


if __name__ == "__main__":

    # Example usage
    c = np.array([1, -2, -3, 0, 0])
    A = np.array([[2, 1, 1, 1, 0], [1, 3, 2, 0, 1]])
    b = np.array([4, 5])

    simplex = SimplexAlgorithm(c, A, b)
    solution = simplex.solve()
    print("Optimal solution:", solution)
