import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.pulp_solver import PulpSolver


class Exerc01(PulpSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def exerc_01_a(self):
        self.b = [
            [1, 3, 0, 1],
            [2, 1, 0, 0],
            [0, 1, 4, 1],
            [2, 4, 1, 1],
        ]
        self.b = [
            [1, 3, 0, 1],
            [-2, -1, 0, 0],
            [0, 1, 4, 1],
            [2, 4, 1, 1],
        ]
        self.c = [8, -6, 6, 0]
        # can be written better
        self.inequality = ["<=", "<=", "<=", "<="]
        self.obj = [2, 4, 1, 1]
        self.sense = "max"
        self.create_components()

    def main(self):
        self.exerc_01_a()


if __name__ == "__main__":
    exerc = Exerc01(name="Exercise1a")
    exerc.main()
