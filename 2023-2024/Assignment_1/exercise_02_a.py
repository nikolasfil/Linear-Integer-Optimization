import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.plt_line import line
from Tools.linearGui import LinearGUI


class Exerc2Gui_a(LinearGUI):
    def __init__(self, *args, **kwargs) -> None:
        limit = 500

        kwargs["limit"] = limit
        super().__init__(*args, **kwargs)
        self.lines = []
        self.lines.append(line(-1, -1, -400, "l1", type="line"))
        self.lines.append(line(1, 1, 500, "l2", type="line"))
        self.lines.append(line(0, 1, 250, "l3", type="line"))
        self.lines.append(line(1, -3, 0, "l4", type="line"))
        self.lines.append(line(-3, +2, 0, "l5", type="line"))
        self.parent = Path(__file__).parent

    def find_feasible_points(self):
        # intersection of lines 1 and 5
        self.v.append(self.lines[0].intersection(self.lines[4]))

        # intersection of liens 5 and 3
        self.v.append(self.lines[4].intersection(self.lines[2]))

        # intersection of lines 3 and 2
        self.v.append(self.lines[2].intersection(self.lines[1]))

        # intersection of lines 2 and 4
        self.v.append(self.lines[1].intersection(self.lines[3]))

        # intersection of lines 4 and 1
        self.v.append(self.lines[3].intersection(self.lines[0]))

    def standard_feasible_points(self):
        pass

    def feasible_region(self):
        self.create_figure()
        self.save_image("exerc02_feasible.png")

    def exerc02_a(self):
        self.name = "Z: max 3x1+4x2 (a)"
        self.create_figure()
        self.step = 50
        self.graphical_solution(3, 4, 1500, 1800)
        self.save_image("exerc02_a.png")

    def main(self):
        self.feasible_region()
        self.exerc02_a()
        self.show()
