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
        if self.c and self.bounds is None:
            self.bounds = [(0, 1) for _ in range(len(self.c))]
        # Initialize  final variables
        self.final_variables = None
        self.final_fun = -np.inf

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
        # Solve the problem for the specific bounds
        fun, variables = self.solve(bounds)
        # Check if the solution is valid
        if fun is not None and -fun > self.final_fun:
            # Append to the node list for checking
            self.nodes.append((fun, bounds, variables))

    def initial(self):
        """
        Description:
            Initial Solution of the branch and bounds problem
        """
        first_fun, first_variables = self.solve(self.bounds)

        if first_fun is None:
            print("No solution found")
            return

        # Inverting the sign to convert from minimization to maximization
        # self.best_value = -self.best_value
        print(f"Initial best fun: {-first_fun}, Initial best x: {first_variables}")

        # Creating the node list
        self.nodes = [(first_fun, self.bounds, first_variables)]

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
        # Find the initial solution
        self.initial()
        current_variables = None
        current_fun = None
        # Check all the solutions
        while self.nodes:
            # Choose the best node with sorting
            self.nodes.sort(key=lambda x: x[0])
            previous_variables = current_variables
            previous_fun = current_fun

            current_fun, current_bounds, current_variables = self.nodes.pop()
            current_fun = -current_fun

            current_integer_solution = self.check_integer_solution(
                current_variables, current_bounds, current_fun
            )

            print(
                f"{'-'*50}\nPrevious solution: {previous_variables}, value: {previous_fun}\nCurrent solution {current_variables}, value: {current_fun} "
            )

            if current_integer_solution and current_fun > self.final_fun:
                self.final_variables = current_variables
                self.final_fun = current_fun
                print("New best solution")

            print(f"{'-'*50}\n")

        print(f"Final solution: {self.final_variables}, value: {self.final_fun}")


if __name__ == "__main__":
    # Initial data
    c = np.array([23, 17, 30, 14, 9])
    A = np.array([[6, 5, 10, 7, 5]])
    b = np.array([14])
    bounds = [(0, 1) for _ in range(len(c))]

    # Initial solution
    knapsack = Knapsack(A=A, b=b, c=c, bounds=bounds)
    knapsack.main()
