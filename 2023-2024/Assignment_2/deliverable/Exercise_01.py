import sys
from pathlib import Path
import numpy as np

from pulp_solver import PulpSolver


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
        self.presenting_results()

    def exercise_01_b_1(self):
        """
        Description:
            This method solves a matrix multiplication
        """
        from scipy.optimize import linprog
        import fractions

        g = 1
        cn = [5, 0, 0, 0]
        cb = [3, 1, 4, 0]

        B = [
            [-2, 2, 3, 1],
            [2, 2, -1, 0],
            [1, -1, 1, 0],
            [-1, 2, 2, 0],
        ]

        N = [
            [1, 0, 0, 0],
            [2, 1, 0, 0],
            [3, 0, 1, 0],
            [0, 0, 0, 1],
        ]

        B = np.array(B)
        N = np.array(N)

        np.set_printoptions(
            formatter={"all": lambda x: str(fractions.Fraction(x).limit_denominator())}
        )

        B_inv = np.linalg.inv(B)
        B_inv_N = np.dot(B_inv, N)

        print(f"\n{'-'*30}\nB_inv_N:\n{'-'*30}")
        print(B_inv_N)

        # Add a variable g to the cb = [3 + g, 1, 4, 0] and multiply it with the B_inv_N
        # to get the new cn

        cn = np.array(cn)
        cb = np.array(cb)

        B_inv_N_cb = np.dot(cb, B_inv_N)
        print(f"\n{'-'*30}\nB_inv_N_cb:\n{'-'*30}")
        print(B_inv_N_cb)

        cn = cn - B_inv_N_cb

        print(f"\n{'-'*30}\ncn:\n{'-'*30}")
        print(cn)

        # Solve the linear programming problem

    def exercise_01_b_2(self):
        disturbances = [d / 13 for d in range(-32, 16 * 13)]
        # list(map(lambda x:x/13, range(-32, 16*13))

        for d in disturbances:
            print(f"\n\n{'-'*30}\nDisturbance: {d}\n{'-'*30}")
            self.add_disturbance(d, 0)
            self.presenting_results()
            print(f"\n{'-'*30}\n{'-'*30}\n\n")

    def exercise_01_b_3(self):
        disturbances = [d / 13 for d in range(-32, 16 * 13)]
        # list(map(lambda x:x/13, range(-32, 16*13))

        for d in disturbances:
            print(f"\n\n{'-'*30}\nDisturbance: {d}\n{'-'*30}")
            self.add_disturbance(d, 0)
            self.presenting_results()
            print(f"\n{'-'*30}\n{'-'*30}\n\n")

    def add_disturbance(self, d, index=0):
        self.b = [
            [1, -2, 2, 3],
            [2, 2, 2, -1],
            [3, 1, -1, 1],
            [0, -1, 2, 2],
        ]
        self.c = [10, 6, 10, 7]

        # can be written better
        self.inequality = ["<=", "<=", "<=", "<="]
        self.obj = [
            item + d if i == index else item for i, item in enumerate([5, 3, 1, 4])
        ]
        self.sense = "max"
        self.create_components()

    def exercise_01_c_1(self):
        """
        Description:
            This method solves a matrix multiplication
        """
        from scipy.optimize import linprog
        import fractions

        b = [[10], [6], [10], [7]]

        B = [
            [-2, 2, 3, 1],
            [2, 2, -1, 0],
            [1, -1, 1, 0],
            [-1, 2, 2, 0],
        ]

        B = np.array(B)
        b = np.array(b)
        np.set_printoptions(
            formatter={"all": lambda x: str(fractions.Fraction(x).limit_denominator())}
        )

        B_inv = np.linalg.inv(B)
        B_inv_b = np.dot(B_inv, b)

        print(f"\n{'-'*30}\nB_inv_b:\n{'-'*30}")
        print(B_inv_b)

    def exercise_01_c_2(self):
        """
        Description:
            This method solves a matrix multiplication
        """
        from scipy.optimize import linprog
        import fractions

        b = [[10], [6], [10], [7]]

        B = [
            [-2, 2, 3, 1],
            [2, 2, -1, 0],
            [1, -1, 1, 0],
            [-1, 2, 2, 0],
        ]

        N = [
            [1, 0, 0, 0],
            [2, 1, 0, 0],
            [3, 0, 1, 0],
            [0, 0, 0, 1],
        ]

        B = np.array(B)
        b = np.array(b)
        N = np.array(N)
        np.set_printoptions(
            formatter={"all": lambda x: str(fractions.Fraction(x).limit_denominator())}
        )

        B_inv = np.linalg.inv(B)
        B_inv_N = np.dot(B_inv, N)

        print(f"\n{'-'*30}\nB_inv_b:\n{'-'*30}")
        print(B_inv_N)

    def main(self):
        # self.exerc_01_a()
        # self.exercise_01_b_1()
        # self.exercise_01_b_2()
        # self.exercise_01_c_1()
        self.exercise_01_c_2()


if __name__ == "__main__":
    exerc = Exerc01(name="Exercise1a")
    exerc.main()
