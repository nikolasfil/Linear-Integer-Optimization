import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.pulp_solver import PulpSolver


class Exerc01(PulpSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    exerc = Exerc01(3, "x", lowbound=0)
