import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


class line:
    """ax1 + bx2 = c"""

    def __init__(
        self,
        a: float,
        b: float,
        c: float,
        name: str,
        legend_show=True,
        type: str = "line",
    ) -> None:
        """
        Args:
            a (float): _description_
            b (float): _description_
            c (float): _description_
            name (str): _description_
            legend_show (bool, optional): _description_. Defaults to True.
        """
        self.a, self.b, self.c = map(float, (a, b, c))
        self.name = name
        self.legend_show = legend_show
        self.type = type

    def __str__(self):
        """returns the equation"""

        output = f"{str(self.a if self.a !=1 else '')+'x1' if self.a else ''}{'+' if self.a and self.b>0 else ''}{str(self.b if self.b !=1 else '')+'x2' if self.b else ''} = {self.c}"
        return output

    def intersection(self, line, plotting=True):
        """returns the intersection point of two lines, and plots it if plotting is True"""

        x_up = line.c * self.b - self.c * line.b
        x_down = line.a * self.b - self.a * line.b
        if x_down == 0:
            # print(f'{self.name} and {line.name} are parallel')
            return None

        x = x_up / x_down
        y = self.equation(x)

        if plotting:
            plt.plot(
                x, y, "ro", label=f"{self.name} ∩ {line.name} = ({x:.2f}, {y:.2f})"
            )
            if self.legend_show:
                plt.legend()
        return [x, y]

    def equation(self, x):
        """returns the y value of the line for a given x value"""
        if self.b != 0:
            return (-self.a * x + self.c) / self.b
        return 0

    def reverse_equation(self, y):
        """returns the x value of the line for a given y value"""
        return (-self.b * y + self.c) / self.a

    def plot(self, x, color=None, lw=2, ms=12):
        """plots the line, and the equation as a label"""

        if self.type == "axis":
            lw = 1

        if self.b == 0:
            plt.axvline(
                x=self.c / self.a,
                label=f"{self.name}: {self}",
                color=self.auto_color_chooser(color),
                linewidth=lw,
                markersize=ms,
            )
        else:
            plt.plot(
                x,
                self.equation(x),
                label=f"{self.name}: {self}",
                color=self.auto_color_chooser(color),
                linewidth=lw,
                markersize=ms,
            )
        # calls the plot settings function to show the legend
        if self.legend_show:
            plt.legend()

    def auto_color_chooser(self, color=None):
        """returns a color from the matplotlib color list, if color is not given, it returns the next color in the list, if color is given, it returns the color if it is in the list, else it returns the first color in the list"""
        colors = sorted(mcolors.cnames)
        if not color and not hasattr(self, "ind"):
            self.ind = 0
        elif not color and hasattr(self, "ind"):
            self.ind = (self.ind + 1) % len(colors)
        elif color and not hasattr(self, "ind"):
            self.ind = colors.index(color) if color in colors else 0
        return colors[self.ind]
