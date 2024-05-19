import pulp


class PulpSolver:
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
        self.inequality = kwargs.get("inequality", [])

    def sensing(self):
        if self.sense == "max":
            self.sense = pulp.LpMaximize
        elif self.sense == "min":
            self.sense = pulp.LpMinimize
        elif self.sense is None:
            self.sense = pulp.LpMaximize
        else:
            raise ValueError("Sense must be either 'max' or 'min'.")

    def create_components(self):
        print(self.b, self.c, self.obj, self.inequality)
        self.sensing()

        self.model = pulp.LpProblem(self.name, sense=self.sense)
        self.build_model()
        self.solver = pulp.GLPK_CMD()

        self.status = self.model.solve(self.solver)

    def build_model(self):
        """
        Description:
        """

        # Takes the number of variables and creates them.
        self.x = [
            pulp.LpVariable(name=f"x{i}", lowBound=0)
            for i in range(1, len(self.b[0]) + 1)
        ]

        for i, row in enumerate(self.b):

            # creating the constraints
            # temp = "".join(
            #     [str(row[j]) + " * " + self.x[j].name + " + " for j in range(len(row))]
            # )

            # temp = " + ".join([f"{row[j]} * {self.x[j]}" for j in range(len(row))])

            # temp += f" <= {self.c[i]}"
            # print(temp)
            # self.model += eval(temp)

            self.model += (
                sum([self.x[j] * row[j] for j in range(len(row))]) <= self.c[i]
            )

        self.model += sum([self.x[i] * self.obj[i] for i in range(len(self.obj))])

    def presenting_results(self):
        print("Status:", pulp.LpStatus[self.status])
        print("Objective:", pulp.value(self.model.objective))
        for var in self.model.variables():
            print(f"{var.name }= {var.varValue}")

        for name, constraint in self.model.constraints.items():
            print(f"{name}: {constraint.value()}")


if __name__ == "__main__":
    pass
