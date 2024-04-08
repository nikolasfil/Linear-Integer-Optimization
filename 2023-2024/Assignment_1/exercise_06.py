import matplotlib.pyplot as plt
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parents[2]))
from Tools.simplex_solver import SimplexSolver


class Exerc06(SimplexSolver):

    def main(self):
        A = np.array([[1, 2, -3, 1], [3, 3, 1, 3]])
        b = np.array([24, 36])
        c = np.array([5, 4, -1, 3])

        simplex = SimplexSolver(A=A, b=b, c=c)
        simplex.solve()


if __name__ == "__main__":
    exercise = Exerc06()
    exercise.main()
    try:
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
