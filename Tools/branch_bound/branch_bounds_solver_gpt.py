import numpy as np
from scipy.optimize import linprog


class BranchAndBound:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.best_solution = None
        self.best_value = float("inf")

    def solve(self):
        self.branch_and_bound([], [])
        return self.best_solution, self.best_value

    def branch_and_bound(self, fixed_vars, fixed_values):
        c = self.c
        A = self.A
        b = self.b

        bounds = [(0, 1)] * len(c)
        for var, value in zip(fixed_vars, fixed_values):
            bounds[var] = (value, value)

        res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

        if res.success:
            solution = res.x
            value = res.fun
            if self.is_integer_solution(solution):
                if value < self.best_value:
                    self.best_value = value
                    self.best_solution = solution
            else:
                branch_var = self.select_branch_variable(solution)
                for val in [0, 1]:
                    self.branch_and_bound(
                        fixed_vars + [branch_var], fixed_values + [val]
                    )

    def is_integer_solution(self, solution):
        return all(x.is_integer() for x in solution)

    def select_branch_variable(self, solution):
        for i, x in enumerate(solution):
            if not x.is_integer():
                return i
        return None


if __name__ == "__main__":
    # Example usage
    c = [23, 17, 30, 14, 9]  # Objective function coefficients (maximize c^T * x)
    A = [[6, 5, 10, 7, 5]]  # Constraint coefficients
    b = [14]  # Constraint bounds

    bb = BranchAndBound(c, A, b)
    best_solution, best_value = bb.solve()

    print("Best Solution:", best_solution)
    print("Best Value:", best_value)
