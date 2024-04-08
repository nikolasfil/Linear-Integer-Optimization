from pathlib import Path
import numpy as np


class SimplexSolver:
    def __init__(self, *args, **kwargs) -> None:
        self.interactive = False
        np.set_printoptions(precision=2)

        self.A = kwargs.get("A")
        self.b = kwargs.get("b")
        self.c = kwargs.get("c")
        self.parent = kwargs.get("parent", Path(__file__).parent)

    def equation(self, *args):
        if len(args) != len(self.c):
            # raise ValueError(
            #     "The number of arguments must be equal to the equation parameters"
            # )
            return sum([coef * x for coef, x in zip(self.c, args)])
        return sum([coef * x for coef, x in zip(self.c, args)])

    def solve(self):

        basicSize = self.A.shape[0]
        nonBasicSize = self.A.shape[1] - basicSize

        # global index tracker of variables of basic and nonbasic variables (objective)
        # that is, index 0 corresponds with x_0, 1 with x_1 and so on.  So each index corresponds with a variable

        cindx = [i for i in range(len(self.c))]

        # basic variable coefficients
        cbT = np.array(self.c[nonBasicSize:])

        # nonbasic variable coefficients
        cnT = np.array(self.c[:nonBasicSize])

        step = 0

        while True:
            step += 1
            print(f"Step {step}")

            # Keep track of the current indices of basic and non-basic variables

            cbIndx = cindx[nonBasicSize:]
            cnIndx = cindx[:nonBasicSize]

            # Basic matrix

            B = self.A[:, cbIndx]
            Binv = np.linalg.inv(B)

            # Non-basic matrix
            N = self.A[:, cnIndx]
            # bHat, the values of the basic variables
            # recall that at the start the basic variables are the slack variables, and
            # have values equal the vector b (as primary variables are set to 0 at the start)
            bHat = Binv @ self.b
            yT = cbT @ Binv

            # use to check for optimality, determine variable to enter basis

            cnHat = cnT - (yT @ N)

            # find indx of minimum value of cnhat, this is the variable to enter the basis

            cnMinIndx = np.argmin(cnHat)

            M = np.column_stack([N, Binv, bHat])

            print("Basic Variables: ", np.array(cbIndx) + 1)
            print("Non-Basic Variables: ", np.array(cnIndx) + 1)
            print("Z: ", cnHat)
            print(M)

            x = np.zeros((nonBasicSize + basicSize))
            x[np.array(cbIndx)] = bHat

            print(f"Z = {self.equation(*x[:basicSize])}")

            file = Path(self.parent, "data_exerc6", f"step_{step}.csv")

            np.savetxt(file, M, delimiter=",", fmt="%1.2f", newline=" \\\\\n")

            if all(cnHat > 0):
                return cbT, cbIndx, cnT, cnIndx, bHat, cnHat

            if self.interactive:
                cnMinIndx = int(
                    input("Enter the index of the variable to enter the basis: ")
                )

            indx = cnIndx[cnMinIndx]
            Ahat = Binv @ self.A[:, indx]

            # now we want to iterate through Ahat and bHat and pick the minimum ratios
            # only take ratios of variables with Ahat_i values greater than 0
            # pick smallest ratio to get variable that will become
            # nonbasic.

            ratios = []
            for i in range(len(bHat)):
                Aval = Ahat[i]
                Bval = bHat[i]

                if Aval > 0:
                    ratios.append(Bval / Aval)
                else:
                    # ratios.append(np.inf)
                    ratios.append(10000000)

            ratioMinIndx = np.argmin(ratios)

            print(
                f"Swapping{cindx[ratioMinIndx+nonBasicSize]+1} for {cindx[cnMinIndx]+1}\n"
            )

            # swaps
            # switch basic and nonbasic variables using the indices
            cnT[cnMinIndx], cbT[ratioMinIndx] = cbT[ratioMinIndx], cnT[cnMinIndx]

            cindx[cnMinIndx], cindx[ratioMinIndx + nonBasicSize] = (
                cindx[ratioMinIndx + nonBasicSize],
                cindx[cnMinIndx],
            )

            print("\n")


if __name__ == "__main__":
    try:
        A = np.array([[1, 1], [2, 1], [1, 0]])
        b = np.array([4, 5, 2])
        c = np.array([3, 2])
        oc = np.array([0, 0])

        simplex = SimplexSolver(A=A, b=b, c=c, objective_coefficients=oc)
        print(simplex.equation(1, 1))

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
