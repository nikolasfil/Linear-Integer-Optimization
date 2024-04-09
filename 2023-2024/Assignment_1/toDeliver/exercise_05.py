import matplotlib.pyplot as plt
import sys
from pathlib import Path

from equation_solver import EquationSolver


class Exerc05(EquationSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parent = Path(__file__).parent

    # def main(self):
    #     super().main()

    #     self.feasible_tops()


if __name__ == "__main__":
    try:
        obj = ["max", -2, 1, -4, 3]
        coef = [[1, 1, 3, 2, 4], [1, 0, -3, 4, 2], [2, 1, 0, 0, 3]]
        exerc = Exerc05(coefficients=coef)
        exerc.main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
