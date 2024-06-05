import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parents[3]))
from Tools.branch_bound.branch_bound_pulp_solver import BBPulpSolver


class Exerc05(BBPulpSolver):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def exerc_05_a(self):

        self.obj = [23, 17, 30, 14, 9]
        self.b = [[6, 5, 10, 7, 5]]
        self.c = [14]
        self.get_iterations()

        for iteration in self.possibles:
            self.sense = "max"
            self.integers = iteration
            self.create_components()
            self.solve()
            self.presenting_results()

    def main(self):
        ex.exerc_05_a()

        # ex.solve()
        # ex.presenting_results()


if __name__ == "__main__":
    ex = Exerc05(name="Exerc05")
    ex.main()
