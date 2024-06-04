from scipy.optimize import linprog
import numpy as np


class Knapsack:
    def __init__(self, *args, **kwargs):
        self.A = kwargs.get("A", None)
        self.b = kwargs.get("b", None)
        self.c = kwargs.get("c", None)
        self.bounds = kwargs.get("bounds", [(0, 1) for _ in range(len(self.c))])

    def solve(self, bounds):
        """Solves the knapsack problem

        Args:
            c (np_array): _description_
            A (np_array): _description_
            b (np_array): _description_
            sense (str, optional): _description_. Defaults to "max".

        Returns:
            function, x variables
        """
        result = linprog(
            -self.c, A_ub=self.A, b_ub=self.b, bounds=bounds, method="highs"
        )
        if result.success:
            return result.fun, result.x
        return None, None

    def adding_nodes(self, bounds):

        value, solution = self.solve(bounds)
        if value is not None:
            value = -value
            if value > self.final_value:
                # self.final_value = value
                # self.final_solution = solution
                self.nodes.append((-value, bounds, solution))

    def initial(self):

        self.best_value, self.best_solution = self.solve(self.bounds)

        if self.best_value is None:
            print("No solution found")
            return

        # Inverting the sign to convert from minimization to maximization
        self.best_value = -self.best_value
        print(
            f"Initial best fun: {self.best_value}, Initial best x: {self.best_solution}"
        )

        self.nodes = [(-self.best_value, self.bounds, self.best_solution)]

        self.final_solution = None
        self.final_value = -np.inf

    def check_integer_solution(self, current_solution, current_bounds, current_value):
        for i, item in enumerate(current_solution):
            if item not in [0, 1]:

                # Create two new nodes
                new_bounds_zero = current_bounds.copy()
                new_bounds_one = current_bounds.copy()

                new_bounds_zero[i] = (0, 0)
                new_bounds_one[i] = (1, 1)

                self.adding_nodes(new_bounds_zero)
                self.adding_nodes(new_bounds_one)

                return False

        return True

    def main(self):
        self.initial()

        while self.nodes:
            # Choose the best node

            self.nodes.sort(key=lambda x: x[0])  # reverse=True

            current_value, current_bounds, current_solution = self.nodes.pop()
            current_value = -current_value

            current_integer_solution = self.check_integer_solution(
                current_solution, current_bounds, current_value
            )

            if current_integer_solution and current_value > self.final_value:
                self.final_solution = current_solution
                self.final_value = current_value

        print(f"Final solution: {self.final_solution}, value: {self.final_value}")


if __name__ == "__main__":
    # Initial data
    c = np.array([23, 17, 30, 14, 9])
    A = np.array([[6, 5, 10, 7, 5]])
    b = np.array([14])
    bounds = [(0, 1) for _ in range(len(c))]

    # Initial solution
    knapsack = Knapsack(A=A, b=b, c=c, bounds=bounds)
    knapsack.main()
