import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


class line:
    """ax1 + bx2 = c"""

    def __init__(self, a, b, c, name, legend_show=True) -> None:
        self.a, self.b, self.c = map(int, (a, b, c))
        self.name = name
        self.legend_show = legend_show

    def __str__(self):
        return f"{str(self.a if self.a !=1 else '')+'x1' if self.a else ''}{'+' if self.a and self.b>0 else ''}{str(self.b if self.b !=1 else '')+'x2' if self.b else ''} = {self.c}"

    def intersection(self, line, plotting = True):

        x = (line.c * self.b - self.c * line.b) / (line.a * self.b - self.a * line.b)
        y = self.equation(x)
        
        if plotting:
            plt.plot(x, y, 'ro', label=f"{self.name} ∩ {line.name} = ({x:.2f}, {y:.2f})")
            self.plot_settings()
        return [x, y]

    def equation(self, x):
        return (-self.a * x + self.c)/self.b

    def reverse_equation(self, y):
        return (-self.b * y + self.c)/self.a

    def plot(self, x, color=None, lw = 2, ms = 12):
        # plot(x, y, 'go--', linewidth=2, markersize=12)
        if self.b == 0:
            plt.axvline(x=self.c/self.a, label=self, color=self.auto_color_chooser(color), linewidth=lw, markersize=ms)
            # plt.plot(0, x, label=self, color=self.auto_color_chooser(color), linewidth=lw, markersize=ms)
        else:
            plt.plot(x, self.equation(x), label=self, color=self.auto_color_chooser(color), linewidth=lw, markersize=ms)
            # plt.plot(x, self.equation(x), label=self, color=self.auto_color_chooser(color))
            

        self.plot_settings()
        # plt.show()

    def plot_settings(self):
        plt.ylim(0, 10)
        plt.xlim(0, 10)
        plt.grid()
        if self.legend_show:
            plt.legend()


    def auto_color_chooser(self,color=None):
        colors = sorted(mcolors.cnames)
        if not color and not hasattr(self, 'ind'):
            self.ind = 0
        elif not color and hasattr(self, 'ind'):
            self.ind = (self.ind+1)%len(colors)
        elif color and not hasattr(self, 'ind'):
            self.ind = colors.index(color) if color in colors else 0
        return colors[self.ind]


