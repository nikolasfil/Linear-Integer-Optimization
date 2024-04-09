from pathlib import Path
import numpy as np


class SimplexSolver:
    def __init__(self, *args, **kwargs) -> None:
        """
        Description:
            SimplexSolver class for solving linear programming problems using the simplex method.
        Args:
            A: numpy array
                The constraint matrix
            b: numpy array
                The right-hand side of the constraints
            c: numpy array
                The coefficients of the objective function
            parent: str
                The parent directory of the file
        """
        self.interactive = False
        np.set_printoptions(precision=2)

        self.A = kwargs.get("A")
        self.b = kwargs.get("b")
        self.c = kwargs.get("c")
        self.parent = kwargs.get("parent", Path(__file__).parent)

    def equation(self, *args) -> float:
        """
        Description :
            Getting the value of the equation given the arguments
            The coefficients of the equation are stored in the c attribute

        Args:
            *args: float
                The arguments of the equation

        Returns:
            float: The value of the equation
        """
        # if len(args) != len(self.c):
        #     # raise ValueError(
        #     #     "The number of arguments must be equal to the equation parameters"
        #     # )
        # return sum([coef * x for coef, x in zip(self.c, args)])
        return sum([coef * x for coef, x in zip(self.c, args)])

    def solve(self):
        """
        Description:
            Solves the linear programming problem using the simplex method
        Returns:
            : _description_
            return cbT, cbIndx, cnT, cnIndx, bHat, cnHat
            cbT, cbIndex is final basic variable values, and indices
            cnT, cnIndex is final nonbasic variable values and indices
            bHat is final solution values,
            cnHat is optimality condition
        """

        # Size of basic vectors, m , number of constraints
        basicSize = self.A.shape[0]

        # Size of nonbasic vector , n-m, number of variables
        nonBasicSize = self.A.shape[1] - basicSize

        # global index tracker of variables of basic and nonbasic variables (objective)
        # that is, index 0 corresponds with x_0, 1 with x_1 and so on.  So each index corresponds with a variable

        c_index = [i for i in range(len(self.c))]

        # basic variable coefficients
        cbT_basic_variable_coef = np.array(self.c[nonBasicSize:])

        # nonbasic variable coefficients
        cnT_nonbasic_variable_coef = np.array(self.c[:nonBasicSize])

        step = 0

        while True:
            step += 1
            print(f"Step {step}")

            # Keep track of the current indices of basic and non-basic variables

            c_b_index = c_index[nonBasicSize:]
            c_nb_index = c_index[:nonBasicSize]

            # Basic matrix
            # Array slicing. B will contain all the row of A but only the columns specified by cbIndx
            B = self.A[:, c_b_index]
            Binv = np.linalg.inv(B)

            # Non-basic matrix
            N = self.A[:, c_nb_index]

            # bHat, the values of the basic variables
            # recall that at the start the basic variables are the slack variables, and have values equal the vector b (as primary variables are set to 0 at the start)
            basic_var_values = Binv @ self.b
            yT = cbT_basic_variable_coef @ Binv

            # use to check for optimality, determine variable to enter basis

            cnHat = cnT_nonbasic_variable_coef - (yT @ N)

            # find indx of minimum value of cnhat, this is the variable to enter the basis

            cnMinIndx = np.argmin(cnHat)

            M = np.column_stack([N, Binv, basic_var_values])

            print("Basic Variables: ", np.array(c_b_index) + 1)
            print("Non-Basic Variables: ", np.array(c_nb_index) + 1)
            print("Z: ", cnHat)
            print(M)

            x = np.zeros((nonBasicSize + basicSize))
            x[np.array(c_b_index)] = basic_var_values

            print(f"Z = {self.equation(*x[:basicSize])}")

            if all(cnHat > 0):
                return (
                    cbT_basic_variable_coef,
                    c_b_index,
                    cnT_nonbasic_variable_coef,
                    c_nb_index,
                    basic_var_values,
                    cnHat,
                )

            if self.interactive:
                cnMinIndx = int(
                    input("Enter the index of the variable to enter the basis: ")
                )

            indx = c_nb_index[cnMinIndx]
            Ahat = Binv @ self.A[:, indx]

            # now we want to iterate through Ahat and bHat and pick the minimum ratios
            # only take ratios of variables with Ahat_i values greater than 0
            # pick smallest ratio to get variable that will become
            # nonbasic.

            ratios = []
            for i in range(len(basic_var_values)):
                Aval = Ahat[i]
                Bval = basic_var_values[i]

                if Aval > 0:
                    ratios.append(Bval / Aval)
                else:
                    # ratios.append(np.inf)
                    ratios.append(10000000)

            ratioMinIndx = np.argmin(ratios)

            print(
                f"Swapping{c_index[ratioMinIndx+nonBasicSize]+1} for {c_index[cnMinIndx]+1}\n"
            )

            # swaps
            # switch basic and nonbasic variables using the indices
            (
                cnT_nonbasic_variable_coef[cnMinIndx],
                cbT_basic_variable_coef[ratioMinIndx],
            ) = (
                cbT_basic_variable_coef[ratioMinIndx],
                cnT_nonbasic_variable_coef[cnMinIndx],
            )

            c_index[cnMinIndx], c_index[ratioMinIndx + nonBasicSize] = (
                c_index[ratioMinIndx + nonBasicSize],
                c_index[cnMinIndx],
            )

            print("\n")


if __name__ == "__main__":
    # Example usage
    try:
        A = np.array([[1, 1], [2, 1], [1, 0]])
        b = np.array([4, 5, 2])
        c = np.array([3, 2])
        oc = np.array([0, 0])

        simplex = SimplexSolver(A=A, b=b, c=c, objective_coefficients=oc)
        simplex.solve()
        print(simplex.equation(1, 1))

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
