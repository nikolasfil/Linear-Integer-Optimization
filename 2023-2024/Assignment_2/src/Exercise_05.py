import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parents[3]))
from Tools.knapsack import Knapsack


class Exerc05(Knapsack):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def exerc_05_a(self):
        self.c = np.array([23, 17, 30, 14, 9])
        self.A = np.array([[6, 5, 10, 7, 5]])
        self.b = np.array([14])
        self.bounds = [(0, 1) for _ in range(len(self.c))]

        self.main()


if __name__ == "__main__":
    exerc = Exerc05(name="Exercise5a")
    exerc.exerc_05_a()
