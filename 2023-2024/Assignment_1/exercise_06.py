import matplotlib.pyplot as plt
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parents[2]))
from Tools.simplex_solver import SimplexSolver


class Exerc06(SimplexSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parent = Path(__file__).parent

    def main(self):
        A = np.array([[1, 2, -3, 1], [3, 3, 1, 3]])
        b = np.array([24, 36])
        c = np.array([5, 4, -1, 3])

        # A = np.array(
        #     [
        #         [1, 2, 3, 1, 0, 0],
        #         [3, 1, 2, 0, 1, 0],
        #         [2, 3, 1, 0, 0, 1],
        #     ]
        # )
        # b = np.array([2, 2, 4])
        # c = np.array([-1, -4, -5, 0, 0, 0])

        simplex = SimplexSolver(A=A, b=b, c=c)
        simplex.parent = self.parent
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
