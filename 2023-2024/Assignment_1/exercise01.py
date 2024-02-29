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


if __name__ == "__main__":
    gui = Gui(
        plt,
        name="Feasible Region",
    )
    gui.main()
