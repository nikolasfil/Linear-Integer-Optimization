class equation:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name", "equation")
        self.coefficients = args[:-1]
        self.b = args[-1]

    def __str__(self):
        output = []

        for i, coef in enumerate(self.coefficients):
            if coef == 1:
                temp = f"x{i+1}"
            elif coef == -1:
                temp = f"-x{i+1}"
            else:
                temp = f"{str(coef)}x{i+1}"
            output.append(temp)

        result = output[0]

        for item in output[1:]:
            if item[0] == "-":
                result += item
            else:
                result += "+" + item
        result += f" = {self.b}"

        return result

    def __call__(self, *args, reverse=False):
        return self.equation(*args)

    def equation(self, *args):
        return sum([coef * x for coef, x in zip(self.coefficients, args)])


if __name__ == "__main__":
    l1 = equation(1, 1, 1, 1, name="l1")
    l2 = equation(1, 1, 1, 2, name="l2")
    print(l1)
