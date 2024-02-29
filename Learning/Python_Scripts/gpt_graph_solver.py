import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


class LinearProgrammingProblem:
    def __init__(self, objective_coefficients, inequality_matrix, inequality_constants):
        self.c = objective_coefficients
        self.A = inequality_matrix
        self.b = inequality_constants

    def plot_objective_function(self, x_range):
        y = np.dot(self.c, x_range)
        plt.plot(x_range, y, label="Objective Function")
        plt.xlabel("X1")
        plt.ylabel("X2")
        plt.legend()
        plt.title("Objective Function")
        plt.grid(True)
        plt.show()

    def plot_feasible_region(self):
        res = linprog(c=self.c, A_ub=self.A, b_ub=self.b, method="highs")
        x_range = np.linspace(0, 10, 100)  # Adjust the range as needed
        plt.fill_between(
            x_range,
            (self.b[0] - self.A[0, 0] * x_range) / self.A[0, 1],
            (self.b[1] - self.A[1, 0] * x_range) / self.A[1, 1],
            where=((self.A @ res.x) <= self.b),
            color="gray",
            alpha=0.5,
            label="Feasible Region",
        )
        plt.xlabel("X1")
        plt.ylabel("X2")
        plt.legend()
        plt.title("Feasible Region")
        plt.grid(True)
        plt.show()

    def solve_and_plot(self):
        self.plot_objective_function(np.linspace(0, 10, 100))
        self.plot_feasible_region()


# Example usage:
# Define the linear programming problem
c = np.array([3, 2])  # Coefficients of the objective function
A = np.array([[1, -1], [3, 1]])  # Coefficients of the inequalities
b = np.array([2, 9])  # Constants of the inequalities

# Create the LinearProgrammingProblem object
lp_problem = LinearProgrammingProblem(c, A, b)

# Solve and plot the objective function and feasible region
lp_problem.solve_and_plot()
