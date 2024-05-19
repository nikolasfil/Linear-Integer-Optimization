import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[3]))
from Tools.pulp_solver import PulpSolver


class Exerc01(PulpSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def exerc_01_a(self):
        self.b = [
            [1, -2, 2, 3],
            [2, 2, 2, -1],
            [3, 1, -1, 1],
            [0, -1, 2, 2],
        ]
        self.c = [10, 6, 10, 7]

        # can be written better
        self.inequality = ["<=", "<=", "<=", "<="]
        self.obj = [5, 3, 1, 4]
        self.sense = "max"
        self.create_components()

    def main(self):
        self.exerc_01_a()
        self.presenting_results()


if __name__ == "__main__":
    exerc = Exerc01(name="Exercise1a")
    exerc.main()
