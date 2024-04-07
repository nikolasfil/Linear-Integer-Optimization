import sys
from pathlib import Path

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

        if self.equations:
            self.coefficients = [eq.coefficients for eq in self.equations]

        if self.coefficients:
            self.equations = [equation(*coef) for coef in self.coefficients]

    def checker(self, *args):
        results = [eq(*args) <= eq.c for eq in self.equations]
        results.extend(item >= 0 for item in args)
        return all(results)

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
