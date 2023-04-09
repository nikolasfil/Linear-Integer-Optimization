import matplotlib.pyplot as plt
import numpy as np


class Line:
    """ax1 + bx2 = c"""

    def __init__(self, a, b, c, name) -> None:
        self.a, self.b, self.c = map(int, (a, b, c))
        self.name = name

    def __str__(self):
        return f"{str(self.a if self.a !=1 else '')+'x1' if self.a else ''}{' + ' if self.a and self.b else ''}{str(self.b if self.b !=1 else '')+'x2' if self.b else ''} = {self.c}"

    def intersection(self, line):
        x = (line.c * self.b - self.c * line.b) / \
            (line.a * self.b - self.a * line.b)
        y = self.equation(x)
        return [x, y]

    def equation(self, x):
        return (-self.a * x + self.c)/self.b

    def plot(self, x, color, lw = 2, ms = 12):
        # plot(x, y, 'go--', linewidth=2, markersize=12)
        if self.b == 0:
            plt.axvline(x=self.c/self.a, label=self, color=color, linewidth=lw, markersize=ms)
            # plt.plot(0, x, label=self, color=color, linewidth=lw, markersize=ms)
        else:
            plt.plot(x, self.equation(x), label=self, color=color, linewidth=lw, markersize=ms)
            # plt.plot(x, self.equation(x), label=self, color=color)
            

        self.plot_settings()
        # plt.show()

    def plot_settings(self):
        plt.ylim(0, 10)
        plt.xlim(0, 10)
        plt.grid()
        plt.legend()
