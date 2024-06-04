import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from equation_class import equation


class BB:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.best_solution = ((None, None), float("-inf"))
        self.best_value = float("inf")
        self.node_counter = 0
        self.edges = []
        self.node_values = {}
        self.z = {}
        self.variable_series = [0 for i in range(len(c))]

    def main(self):
        self.variable_chooser()
        # self.branch_and_bound_original()

    def branch_and_bound(self):
        pass

    def branch_and_bound_original(self, x1_range=(0, None), x2_range=(0, None)):
        bounds = [x1_range, x2_range]

        res = linprog(self.c, A_ub=self.A, b_ub=self.b, bounds=bounds, method="highs")

        node_id = self.node_counter
        self.node_counter += 1

        if res.success:
            x1_val, x2_val = res.x
            objective = -res.fun

            self.node_values[node_id] = (
                round(x1_val, 2),
                round(x2_val, 2),
                round(objective, 2),
            )

            if (
                x1_val.is_integer()
                and x2_val.is_integer()
                and objective > self.best_solution[1]
            ):
                self.best_solution = ((x1_val, x2_val), objective)

            if not x1_val.is_integer():
                x1_floor = int(np.floor(x1_val))
                self.edges.append((node_id, self.node_counter))
                self.branch_and_bound_original(
                    x1_range=(0, x1_floor), x2_range=x2_range
                )
                self.edges.append((node_id, self.node_counter))
                self.branch_and_bound_original(
                    x1_range=(x1_floor + 1, None), x2_range=x2_range
                )

            if not x2_val.is_integer():
                x2_floor = int(np.floor(x2_val))
                self.edges.append((node_id, self.node_counter))
                self.branch_and_bound_original(
                    x1_range=x1_range, x2_range=(0, x2_floor)
                )
                self.edges.append((node_id, self.node_counter))
                self.branch_and_bound_original(
                    x1_range=x1_range, x2_range=(x2_floor + 1, None)
                )

    def variable_chooser(self):
        for i in range(len(self.c)):
            # Calculate the constraing function for the current variables

            future_series = self.variable_series.copy()
            future_series[i] = 1

            current_sum = np.dot(self.A[0], self.variable_series)
            future_sum = np.dot(self.A[0], future_series)
            # Check if the current value is still less than the constraint

            if current_sum < self.b[0] and future_sum < self.b[0]:
                self.variable_series[i] = 1


if __name__ == "__main__":
    c = [-1, -0.64]
    A = [[50, 31], [-3, 2]]
    b = [250, 4]

    c = [23, 17, 30, 14, 9]
    A = [[6, 5, 10, 7, 5]]
    b = [14]

    bb = BB(c, A, b)
    bb.main()
    # bb.branch_and_bound()
    # print(bb.best_solution)
    # print(bb.node_values)
    # print(bb.edges)
    # bb.visualize_tree(bb.edges, bb.node_values)
