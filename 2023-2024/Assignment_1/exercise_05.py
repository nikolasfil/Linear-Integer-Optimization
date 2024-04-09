import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.equation_solver import EquationSolver


class Exerc05(EquationSolver):

    def main(self):
        # for eq in self.equations:
        #     print(eq)
        self.get_combinations()
        for lis in self.combos:
            print("----")
            print(lis)
            print(self.get_system_solution(lis))
            print("----")
        self.get_peak_points(None, None)


if __name__ == "__main__":
    obj = ["max", -2, 1, -4, 3]
    coef = [[1, 1, 3, 2, 4], [1, 0, -3, 4, 2], [2, 1, 0, 0, 3]]
    # coef = [[-3, 2, 8, 17], [-1, 1, 3, 9], [-2, 1, 8, 16]]
    exerc = Exerc05(coefficients=coef)
    exerc.main()
    try:
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
