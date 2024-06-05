from scipy.optimize import linprog
import numpy as np


class Knapsack:
    def __init__(self, *args, **kwargs):
        """
        Description: Initialization of the class

        Args:
            A (np_array, optional) : Defaults to None
            b (np_array, optional) : Defaults to None
            c (np_array, optional) : Defaults to None
            bounds (list, optional): Defaults to None
        """
        self.A = kwargs.get("A", None)
        self.b = kwargs.get("b", None)
        self.c = kwargs.get("c", None)
        self.bounds = kwargs.get("bounds", None)
        # Initial final solution
        self.final_solution = None
        self.final_value = -np.inf

    def solve(self, bounds):
        """Solves the knapsack problem

        Args:
            bounds (list): Bounds for the variables

        Args Used :
            self.c (np_array)
            self.A (np_array)
            self.b (np_array)

        Returns:
            function(float), x variables(list) : Returns the function value and the x variables
        """
        result = linprog(
            -self.c, A_ub=self.A, b_ub=self.b, bounds=bounds, method="highs"
        )
        if result.success:
            return result.fun, result.x
        return None, None

    def adding_nodes(self, bounds):
        """
        Description: Adds nodes to the list self.nodes according to the bounds given, if the value is greater than the final value

        Args:
            bounds (list): bounds for the variables
        """

        value, solution = self.solve(bounds)
        if value is not None:
            if -value > self.final_value:
                self.nodes.append((value, bounds, solution))

    def initial(self):
        """
        Description:
            Initial Solution of the branch and bounds problem
        """
        self.best_value, self.best_solution = self.solve(self.bounds)

        if self.best_value is None:
            print("No solution found")
            return

        # Inverting the sign to convert from minimization to maximization
        # self.best_value = -self.best_value
        print(
            f"Initial best fun: {-self.best_value}, Initial best x: {self.best_solution}"
        )

        # Creating the node list
        self.nodes = [(self.best_value, self.bounds, self.best_solution)]

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

            self.nodes.sort(key=lambda x: x[0])

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
