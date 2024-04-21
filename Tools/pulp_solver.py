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

        """
        self.name = kwargs.get("name", "PulpSolver")
        self.sense = kwargs.get("sense", None)
        self.sensing()

        self.b = kwargs.get("b", [])
        self.c = kwargs.get("c", [])

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
        self.model = pulp.LpProblem(self.name, sense=self.sense)
        self.build_model()
        self.solver = pulp.GLKP_CMD()

        self.status = self.model.solve(self.solver)


if __name__ == "__main__":
    pass
