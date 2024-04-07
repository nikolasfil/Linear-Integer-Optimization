import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import sys
from pathlib import Path
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point

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
            save_images (bool): save the images
            v (list): the feasible points
            name (str): the name of the graph
        """

        self.plt = kwargs.get("plt", plt)

        self.limit = kwargs.get("limit", 10)

        # xAxis = np.linspace(-100, 100, 100000)
        xAxis = np.linspace(-10, self.limit + 10, 10)
        self.xAxis = kwargs.get("xAxis", xAxis)

        self.ylim = kwargs.get("ylim", (0, self.limit))
        self.xlim = kwargs.get("xlim", (0, self.limit))

        self.lines = kwargs.get("lines", [])
        self.name = kwargs.get("name", "LinearGUI")
        self.figsize = kwargs.get("figsize")
        self.step = kwargs.get("step", 1)
        self.save_images = kwargs.get("save_images", False)

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

    def create_figure(self, name: str = None):
        if name:
            self.name = name
        if self.figsize:
            plt.figure(self.name, figsize=self.figsize)
        else:
            plt.figure(self.name)

        self.plt.ylim(*self.ylim)
        self.plt.xlim(*self.xlim)
        self.plt.grid()
        self.plot_equations()
        self.fill_feasible()

    def check_feasible_point(self, points):
        p = Point(points)
        polygon = Polygon(self.v)
        return polygon.contains(p)

    def intersections_in_feasible(self, extra):
        for l in self.lines:
            possible = extra.intersection(l, plotting=False)
            if self.check_feasible_point(possible):
                extra.intersection(l)

    def graphical_solution(self, a, b, minlim, maxlim, legend=True):

        counter = minlim
        while counter < maxlim:
            extra = line(a, b, counter, "extra")
            extra.plot(self.xAxis, "cornflowerblue")
            extra.legend_show = False
            self.intersections_in_feasible(extra)
            counter += self.step

    def save_image(self, file_name):
        if self.save_images:
            img_folder = Path(self.parent, "img")

            image_file = Path(img_folder, file_name)
            self.plt.savefig(image_file, dpi="figure")
