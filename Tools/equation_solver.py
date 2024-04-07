import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from equation_class import Equation


class EquationSolver:
    def __init__(self) -> None:
        pass

    def main(self):
        pass


if __name__ == "__main__":
    try:
        eq = Equation("3x1+4x2")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
