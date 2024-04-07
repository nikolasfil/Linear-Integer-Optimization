import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from equation_class import equation


class EquationSolver:
    def __init__(self, *args, **kwargs) -> None:
        self.equations = kwargs.get("equations", [])

    def checker(self, *args):
        results = [eq(*args) <= eq.c for eq in self.equations]
        results.extend(item >= 0 for item in args)
        return all(results)

    def main(self):
        pass


if __name__ == "__main__":
    try:
        eqs = [
            [3, 2, 0, 5],
            [2, 1, 2, 5],
        ]
        eqs = [equation(*eq) for eq in eqs]
        eq = EquationSolver(equations=eqs)
        eq.main()
        print(eq.checker(1, 1, 1))

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
