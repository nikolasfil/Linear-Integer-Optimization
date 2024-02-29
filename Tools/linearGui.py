import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))
from Tools.plt_line import line


class LinearGUI:
    def __init__(self, *args, **kwargs) -> None:
        """
        Args:
            plt (module): the matplotlib module
            xAxis (np.array): the x axis
            limit (int): the limit of the graph
            ylim (tuple): the y axis limits
            xlim (tuple): the x axis limits
            lines (list): the lines to plot
            v (list): the feasible points
            name (str): the name of the graph
        """

        self.plt = kwargs.get("plt", plt)

        xAxis = np.linspace(-100, 100, 100000)
        self.xAxis = kwargs.get("xAxis", xAxis)

        self.limit = kwargs.get("limit", 10)

        self.ylim = kwargs.get("ylim", (0, self.limit))
        self.xlim = kwargs.get("xlim", (0, self.limit))

        self.lines = kwargs.get("lines", [])
        self.name = kwargs.get("name", "LinearGUI")
        self.v = []

    def show(self):
        self.plt.show()

    def plot_equations(self):
        for i, line in enumerate(self.lines):
            if line.type == "line":
                if i == 0:
                    color = "blue"
                else:
                    color = self.lines[i - 1].auto_color_chooser()
                line.plot(self.xAxis, color)

        self.add_axis_lines()

    def add_axis_lines(self):
        right_limit = line(1, 0, self.limit, "limit", type="axis")
        # right_limit = line(1, 0, self.limit, f"limit={self.limit}", type="axis")
        x = line(0, 1, 0, "x-axis", type="axis")
        y = line(1, 0, 0, "y-axis", type="axis")

        self.lines.append(right_limit)
        self.lines.append(x)
        self.lines.append(y)

        x.plot(self.xAxis, "orange", lw=4)
        y.plot(self.xAxis, "orange", lw=4)

    def standard_feasible_points(self):

        self.v.append([self.limit, self.limit])

        # It is the upper-left corner
        self.v.append([0, self.limit])

    def find_feasible_points(self):
        pass

    def fill_feasible(self):
        self.standard_feasible_points()

        self.find_feasible_points()

        print(self.v)
        # Create the x and y Coordinates for the fill area
        x = [i[0] for i in self.v]
        y = [i[1] for i in self.v]

        # Fill takes the x and y of a polygon and fills it with color
        self.plt.fill(x, y, color="gray", alpha=0.5)

    def solution(self, a, b, minlim, maxlim, legend=True):
        """plots the extra lines of the objective function"""

    def create_figure(self, name: str = None):
        if name:
            self.name = name
        plt.figure(self.name)

        self.plt.ylim(*self.ylim)
        self.plt.xlim(*self.xlim)
        self.plt.grid()
        self.plot_equations()
        self.fill_feasible()
