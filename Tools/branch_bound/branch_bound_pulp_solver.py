import pulp
import itertools


class BBPulpSolver:
    def __init__(self, *args, **kwargs) -> None:
        """
        Description:
        ------------
        A class that creates a linear programming model using the pulp library.

        Parameters:
        -----------
        *args: int
            The number of variables to be created.
        **kwargs: dict
            name: str
                The name of the model.
            sense: max or min
                The sense of the model. Default is None.
            b: list
                The b vector of the model. Default is [].
            c: list
                The c vector of the model. Default is [].
            obj: list
                The objective function of the model. Default is [].
            inequality: list
                The inequality of the model. Default is [].
        """
        self.name = kwargs.get("name", "PulpSolver")
        self.sense = kwargs.get("sense", None)

        self.b = kwargs.get("b", [])
        self.c = kwargs.get("c", [])
        self.obj = kwargs.get("obj", [])
        self.integers = kwargs.get("integers", [])
        self.solver = pulp.GLPK_CMD()

    def sensing(self):
        if self.sense == "max":
            self.sense = pulp.LpMaximize
        elif self.sense == "min":
            self.sense = pulp.LpMinimize
        elif self.sense is None:
            self.sense = pulp.LpMaximize
        elif self.sense in [pulp.LpMaximize, pulp.LpMinimize]:
            pass
        else:
            raise ValueError("Sense must be either 'max' or 'min'.")

    def create_components(self):
        print(self.b, self.c, self.obj, self.integers)
        self.sensing()

        self.model = pulp.LpProblem(self.name, sense=self.sense)
        self.build_model()

    def solve(self):
        self.status = self.model.solve(self.solver)

    def build_model(self):
        """
        Description:
        """

        # Takes the number of variables and creates them.
        self.x = [
            pulp.LpVariable(name=f"x{i}", lowBound=0, upBound=1)
            for i in range(1, len(self.b[0]) + 1)
        ]

        for i, row in enumerate(self.b):

            self.model += (
                sum([self.x[j] * row[j] for j in range(len(row))]) <= self.c[i]
            )

        self.add_integers()

        self.model += sum([self.x[i] * self.obj[i] for i in range(len(self.obj))])

    def add_integers(self):

        for i, var in enumerate(self.x):

            self.model += var == self.integers[i]

    def presenting_results(self):
        # pass
        if self.status != 1:
            print(f"The model is infeasible. {self.integers}")
            return
        print("-" * 50)
        print("Status:", pulp.LpStatus[self.status])
        print("Objective:", pulp.value(self.model.objective))
        for var in self.model.variables():
            print(f"{var.name }= {var.varValue}")
        #
        for name, constraint in self.model.constraints.items():
            print(f"{name}: {constraint.value()}")

        print("-" * 50)

    def get_iterations(self):
        self.possibles = list(itertools.product([0, 1], repeat=len(self.b[0])))


if __name__ == "__main__":
    pass
