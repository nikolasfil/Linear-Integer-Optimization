import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.plt_line import line
from Tools.linearGui import LinearGUI


class Gui(LinearGUI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.lines = []
        self.lines.append(line(2, 1, 4, "l1", type="line"))
        self.lines.append(line(1, 2, 5, "l2", type="line"))
        self.lines.append(line(1, -2, 1, "l3", type="line"))

    def find_feasible_points(self):

        # This one is manual :
        # It is supposed to be the highest y that intersects with the y-axis
        self.v.append([0, 4])
        self.plt.plot(*self.v[0], "o", color="red")
        # This one is the intersection of l1 and l2
        self.v.append(self.lines[0].intersection(self.lines[1]))

        # This one is the intersection of l2 and l3
        self.v.append(self.lines[1].intersection(self.lines[2]))

        right_limit = [l for l in self.lines if l.name == "limit"][0]

        self.v.append(self.lines[2].intersection(right_limit, plotting=False))

    def solution(self, a, b, minlim, maxlim, legend=True):
        """plots the extra lines of the objective function"""
        extra_lines = [line(a, b, i, "extra") for i in range(minlim, maxlim)]

        line_l3 = [l for l in self.lines if l.name == "l3"][0]

        for lin in extra_lines:
            lin.legend_show = legend
            lin.plot(self.xAxis, "cornflowerblue")
            # we need to find the intersection with the l3 (brown line) to find the max value of the objective function

            lin.intersection(line_l3)
            # prints the legend and the intersection points


if __name__ == "__main__":
    gui = Gui(plt, name="Feasible Region")
    gui.create_figure()

    gui.name = "a: max 2x1-5x2"
    gui.create_figure()
    gui.solution(2, -5, 0, 2)
    # gui.plt.savefig("img/exerc01-a.png", dpi="figure")

    gui.name = "b: max 2x1-4x2"
    gui.create_figure()
    gui.solution(2, -4, 0, 3)
    # gui.plt.savefig("img/exerc01-b.png", dpi="figure")

    gui.name = "c: max 2x1-3x2"
    gui.create_figure()
    gui.solution(2, -3, 0, 20, legend=False)
    # gui.plt.savefig("img/exerc01-c.png", dpi="figure")

    gui.show()
