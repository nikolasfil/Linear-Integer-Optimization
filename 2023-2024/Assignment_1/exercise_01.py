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
        limit = 30

        kwargs["limit"] = limit
        # kwargs["ylim"] = [-5, limit]
        # kwargs["xlim"] = [-5, limit]
        super().__init__(*args, **kwargs)
        self.lines = []
        self.lines.append(line(1, 1, 10, "l1", type="line"))
        self.lines.append(line(-10, 1, 10, "l2", type="line"))
        # self.lines.append(line(10, -1, -10, "l2", type="line"))
        self.lines.append(line(-4, 1, 20, "l3", type="line"))
        self.lines.append(line(1, 4, 20, "l4", type="line"))

    def find_feasible_points(self):
        self.v.append([0, 10])
        self.plt.plot(*self.v[0], "o", color="red")
        self.v.append(self.lines[2].intersection(self.lines[1]))
        self.v.append([0, 20])
        self.plt.plot(*self.v[2], "o", color="red")

    def standard_feasible_points(self):

        pass

    def solution(self, a, b, minlim, maxlim, legend=True):

        line_l3 = [l for l in self.lines if l.name == "l2"][0]
        # extra_lines = [line(a, b, i, "extra") for i in range(minlim, maxlim, step=0.5)]
        line_yaxis = [l for l in self.lines if l.name == "y-axis"][0]
        step = 0.5
        # step = 1
        counter = minlim
        while counter < maxlim:
            extra = line(a, b, counter, "extra")
            extra.legend_show = False
            extra.plot(self.xAxis, "cornflowerblue")
            # extra.legend_show = True
            extra.intersection(line_l3)
            line_yaxis.intersection(extra)
            counter += step

            # for lin in extra_lines:
            # lin.legend_show = False
            # lin.plot(self.xAxis, "cornflowerblue")
            # lin.legend_show = True

            # lin.intersection(line_l3)


def main():

    gui = Gui(plt, name="Feasible Region")
    # gui.create_figure()
    # gui.plt.savefig("img/exerc01_a.png", dpi="figure")

    # gui.name = "Z: min 2x1-x2"
    # gui.create_figure()
    # gui.solution(2, -1, -12, -9)
    # gui.plt.savefig("img/exerc01_a_2.png", dpi="figure")

    gui.name = "Z: min 11x1-x2"
    gui.create_figure()
    gui.solution(11, -1, -13, -8)
    gui.plt.savefig("img/exerc01_b.png", dpi="figure")

    gui.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        # input("Press Enter to continue...")
