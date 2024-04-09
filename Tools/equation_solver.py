import sys
from pathlib import Path
from itertools import combinations
from scipy.special import binom
import numpy as np

sys.path.append(str(Path(__file__).parent))
from equation_class import equation


class EquationSolver:
    def __init__(self, *args, **kwargs) -> None:
        """
        Description:

        Args:
            equations (list): the equations
            coefficients (list): the coefficients of the equations
        """
        self.equations = kwargs.get("equations", [])
        self.coefficients = kwargs.get("coefficients", [])
        self.current_system = None
        self.build_all_equations()

    def build_all_equations(self):
        if self.equations:
            self.coefficients = [eq.coefficients for eq in self.equations]

        if self.coefficients:
            self.equations = [
                equation(*coef, name=f"line{i}")
                for i, coef in enumerate(self.coefficients)
            ]

        n = len(self.equations[0].coefficients) + 1

        positive_constraints = [
            [0 if i != j else 1 for i in range(n)] for j in range(n - 1)
        ]

        positive_constraints_eq = [
            equation(*item, name=f"pos_x{i}")
            for i, item in enumerate(positive_constraints)
        ]

        self.equations.extend(positive_constraints_eq)

        self.equations = np.array(self.equations)

    def checker(self, *args):
        results = [eq(*args) <= eq.b for eq in self.equations]
        return all(results)

    def number_of_tops(self):
        n = len(self.equations[0].coefficients)
        m = len(self.equations)
        # In the constraints we also have that x_i >= 0
        return binom(n + m, m)

    def get_combinations(self):
        n = len(self.equations[0].coefficients)
        m = len(self.equations)
        self.combination_index = list(range(m))
        self.combos = [x for x in combinations(self.combination_index, n)]

    def get_system_solution(self, system: list):
        # a = np.array([eq.coefficients for eq in system])
        # b = np.array([eq.b for eq in system])

        # System, contains the indexes of the equations that were chosen
        system = np.array(system)
        self.current_system = system
        # Get a list of the equations chosen
        equations = list(np.array(self.equations)[system])

        # Build the matrix A, with the coefficients of the equations used
        a = np.array([np.array(eq.coefficients) for eq in equations])

        # Stack the equations in a row
        a_stacked = np.row_stack(a)

        # Check if the determinant of the matrix is 0
        if np.linalg.det(a_stacked) == 0:
            # It is non Solvable
            return None

        # b = np.array([np.array(eq.b) for eq in system])
        # Build the matrix B, with the b values of the equations used
        b = np.array([np.array(eq.b) for eq in equations])

        # Compute the result of the system of equations
        result = np.linalg.solve(a, b)

        # Saving the variables that were used
        result_all_var = np.zeros((len(self.equations)))

        # Assign values to the variables that were used in the correct order
        result_all_var[system] = result

        return result_all_var

    def get_peak_points(self, system, viable_solution):

        x = np.zeros((len(self.equations)))

        # number of variables without slack
        variables = len(self.equations) - len(self.equations[0].coefficients)

    def tops(self):
        self.get_combinations()
        num_of_vars = len(self.equations[0].coefficients)
        for lis in self.combos:
            solution = self.get_system_solution(lis)
            if solution is not None:
                print(
                    f"{'-'*10}\n{solution} | {self.checker(*solution[:num_of_vars])}\n{'-'*10}"
                )

    def main(self):
        pass


if __name__ == "__main__":
    try:
        coef = [
            [3, 2, 0, 5],
            [2, 1, 2, 5],
        ]
        eq = EquationSolver(coefficients=coef)
        eq.main()
        print(eq.checker(1, 1, 1))

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
