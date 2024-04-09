import matplotlib.pyplot as plt
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parents[2]))
from Tools.simplex_solver import SimplexSolver
from Tools.simplex_solver_g import SimplexAlgorithm


class Exerc06(SimplexSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.parent = Path(__file__).parent

    def main(self):

        # Initializing the equations

        A = np.array(
            [
                [1, 2, -3, 1],
                [3, 3, 1, 3],
            ]
        )
        b = np.array([24, 36])
        c = np.array([5, 4, -1, 3])

        # Initializing the SimplexSolver class instance
        simplex = SimplexSolver(A=A, b=b, c=c, parent=self.parent)
        # Solve the simplex
        simplex.solve()


class Exerc06_2(SimplexAlgorithm):
    def __init__(self, c, A, b):
        super().__init__(c, A, b)

    def main(self):
        self.solve()


if __name__ == "__main__":
    # exercise = Exerc06()
    A = np.array([[1, 2, -3, 1], [3, 3, 1, 3]])
    b = np.array([24, 36])
    c = np.array([5, 4, -1, 3])
    exercise = Exerc06_2(c, A, b)
    exercise.main()
    try:
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
