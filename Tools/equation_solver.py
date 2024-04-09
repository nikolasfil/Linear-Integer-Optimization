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

        self.combs = [x for x in combinations(self.equations, n)]

    def get_system_solution(self, system: list):
        # a = np.array([eq.coefficients for eq in system])
        # b = np.array([eq.b for eq in system])

        a = np.array([np.array(eq.coefficients) for eq in system])
        a_stacked = np.row_stack(a)

        if np.linalg.det(a_stacked) == 0:
            # It is non Solvable
            return None

        b = np.array([np.array(eq.b) for eq in system])

        result = np.linalg.solve(a, b)

        return result

    def get_peak_points(self, system, viable_solution):

        x = np.zeros((len(self.equations)))

        # number of variables without slack
        variables = len(self.equations) - len(self.equations[0].coefficients)

        

    def tops(self):
        # get the different combinations of the equations
        # get the results of those intersections and see with the checker if they are feasible
        # return the feasible points
        # Also print them somewhere to keep track for the report
        pass

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
