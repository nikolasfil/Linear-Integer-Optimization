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
        self.parent = kwargs.get("parent", Path(__name__).parent)

    def build_all_equations(self):
        if self.equations:
            self.coefficients = [eq.coefficients for eq in self.equations]

        if self.coefficients:
            self.equations = [
                equation(*coef, name=f"line{i}")
                for i, coef in enumerate(self.coefficients)
            ]

        self.add_positivity_constraints()

        self.equations = np.array(self.equations)

        self.num_coefficients = len(self.equations[0].coefficients)
        self.num_equations = len(self.equations)

    def add_positivity_constraints(self):
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
        results = []
        for eq in self.equations:
            if eq.name.startswith("pos_x"):
                results.append(eq(*args) >= 0)
            else:
                results.append(eq(*args) <= eq.b)
        # results = [eq(*args) <= eq.b for eq in self.equations]
        return all(results)

    def number_of_tops(self):
        """
        Description:
            Returns the number of tops that can be found using bionomial theorem
        Returns:
            int: The number of tops that can be found
        """

        # In the constraints we also have that x_i >= 0
        return binom(self.num_coefficients + self.num_equations, self.num_equations)

    def get_combinations(self):
        """
        Description:
            Get the combinations of the equations that can be used to solve the system using itertools combination
        """
        self.num_coefficients = len(self.equations[0].coefficients)
        self.num_equations = len(self.equations)
        self.combination_index = list(range(self.num_equations))
        self.combos = [
            x for x in combinations(self.combination_index, self.num_coefficients)
        ]

    def get_system_solution(self, system: list):
        """
        Description:
            Get the solution of the system of equations given the indexes of the equations to be used

        Args:
            system (list): The indexes of the equations to be used

        Returns:
            list: The solutions of the system equations or None if it's not solvable
        """

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

    def tops(self):
        self.get_combinations()
        num_of_vars = len(self.equations[0].coefficients)
        for lis in self.combos:
            solution = self.get_system_solution(lis)
            if solution is not None:
                print(
                    f"{'-'*10}\n{solution} | {self.checker(*solution[:num_of_vars])}\n{'-'*10}"
                )

    def str_single(self, *args, **kwargs):
        """
        Description:
            Returns the string representation of the solution

        Args:
            *args: list
                The solution to be printed
            **kwargs: dict
                solution: list
                    The solution to be printed
                combo: list
                    The indexes of the equations that were used to solve the system

        Returns:
            str: The string representation of the solution
        """

        if args:
            solution = args[0]
        else:
            solution = kwargs.get("solution", None)
        output = []

        equations_combos = kwargs.get("combo", None)
        ind = kwargs.get("ind", "")

        if solution is not None:

            # temp_aknowledge = f"| Solution: {solution} | Feasible:  {self.checker(*solution[:self.num_coefficients])} |"

            # Creates a string for the solution.
            solution_ack = f"| Solution {ind}: {str(solution).replace(' ',' ').replace('  ',' ').replace('   ',' ')} |"
            solution_ack += (
                f" Feasible:  {self.checker(*solution[:self.num_coefficients])} |"
            )

            # Get the length of the solution string to prettify the output
            length = len(solution_ack)

            # If the equation combo is provided it will be printed
            if equations_combos:

                equations = [str(self.equations[i]) for i in equations_combos]
                lengths = [len(eq) + 4 for eq in equations]
                lengths.append(length)
                max_length = max(lengths)

                output.append("-" * max_length)

                equations = [f"| {eq:^{max_length-4}} |" for eq in equations]
                output.append("\n".join(equations))

            output.append("-" * max_length)
            output.append(solution_ack)
            output.append("-" * max_length + "\n")

        return "\n".join(output)

    def feasible_tops(self):
        self.get_combinations()
        output = []
        for i, lis in enumerate(self.combos):

            # Get the solution of the system
            solution = self.get_system_solution(lis)

            # Check if the solution exists
            if solution is not None:
                # If it exists, it will be printed
                if self.checker(*solution[: self.num_coefficients]):
                    output.append(f"Solution {i} : {solution} | Feasible: True")

        print("\n".join(output))

    def main(self):

        self.get_combinations()
        output = []
        for i, lis in enumerate(self.combos):

            # Get the solution of the system
            solution = self.get_system_solution(lis)

            # Check if the solution exists
            if solution is not None:
                # If it exists, it will be printed
                output.append(self.str_single(solution, combo=lis, ind=i))

        print("\n".join(output))
        file = Path(self.parent, "output_exerc_05_a.txt")
        with open(file, "w") as f:
            f.write("\n".join(output))


if __name__ == "__main__":
    try:
        coef = [
            [3, 2, 0, 5],
            [2, 1, 2, 5],
        ]
        eq = EquationSolver(coefficients=coef)
        eq.main()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
