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
        limit = 20

        kwargs["limit"] = limit
        kwargs["ylim"] = [-5, limit]
        kwargs["xlim"] = [-5, limit]
        super().__init__(*args, **kwargs)
        self.lines = []
        self.lines.append(line(1, 1, 10, "l1", type="line"))
        self.lines.append(line(10, 1, 10, "l2", type="line"))
        self.lines.append(line(-4, 1, 20, "l3", type="line"))
        self.lines.append(line(1, 4, 20, "l4", type="line"))

    def find_feasible_points(self):

        # # This one is manual :
        # # It is supposed to be the highest y that intersects with the y-axis
        # self.v.append([0, 10])
        # self.plt.plot(*self.v[0], "o", color="red")
        # # This one is the intersection of l1 and l2
        # self.v.append(self.lines[0].intersection(self.lines[1]))

        # # This one is the intersection of l2 and l3
        # self.v.append(self.lines[1].intersection(self.lines[2]))

        # # This one is the intersection of l3 and l4
        # self.v.append(self.lines[2].intersection(self.lines[3]))

        # right_limit = [l for l in self.lines if l.name == "limit"][0]

        # self.v.append(self.lines[3].intersection(right_limit, plotting=False))
        pass

    def standard_feasible_points(self):
        # return super().standard_feasible_points()
        pass


if __name__ == "__main__":
    gui = Gui(plt, name="Feasible Region")
    gui.create_figure()

    # gui.name = "a: max 2x1-x2"

    gui.show()
