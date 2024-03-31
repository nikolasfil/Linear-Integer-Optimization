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

        # self.lines.append(line(11, -1, (11 * 1.67 - 26.67), "l7", type="line"))
        # self.lines.append(line(11, -1, (-8.5), "l8", type="line"))

        # self.lines.append(line(2, -1, -23.3, "l5", type="line"))
        # self.lines.append(line(2, -1, -24, "l6", type="line"))

    def find_feasible_points(self):

        # self.v.append([0, 10])
        # self.plt.plot(*self.v[-1], "o", color="red")

        # Intersection lines 1 and 2
        self.v.append(self.lines[0].intersection(self.lines[1]))

        # Intersection lines 2 and 3
        self.v.append(self.lines[2].intersection(self.lines[1]))

        # Upper left limit corner
        self.v.append([self.lines[2](self.limit, reverse=True), self.limit])
        # self.plt.plot(*self.v[-1], "o", color="red")

        # Upper right corner
        self.v.append([self.limit, self.limit])
        # self.plt.plot(*self.v[-1], "o", color="red")

        # Lower right corner
        self.v.append([self.limit, 0])
        # self.plt.plot(*self.v[-1], "o", color="red")

        # Intersection x_axis and line 4

        # self.v.append([self.lines[3](0, reverse=True), 0])
        # self.plt.plot(*self.v[-1], "o", color="red")
        x_axis = [l for l in self.lines if l.name == "x-axis"][0]
        self.v.append(self.lines[3].intersection(x_axis))

        # Intersection line 4 and line 1
        self.v.append(self.lines[0].intersection(self.lines[3]))
        # self.plt.plot(*self.v[-1], "o", color="red")

        # self.plt.plot(*self.v[-1], "o", color="red")

    def standard_feasible_points(self):
        pass

    def solution(self, a, b, minlim, maxlim, legend=True):

        line_l3 = [l for l in self.lines if l.name == "l3"][0]
        line_l1 = [l for l in self.lines if l.name == "l1"][0]
        # extra_lines = [line(a, b, i, "extra") for i in range(minlim, maxlim, step=0.5)]

        counter = minlim
        while counter < maxlim:
            extra = line(a, b, counter, "extra")
            extra.plot(self.xAxis, "cornflowerblue")
            extra.legend_show = False
            extra.intersection(line_l3)
            extra.intersection(line_l1)
            counter += self.step


class Exercise01:
    def __init__(self, *args, **kwargs) -> None:
        self.gui = kwargs.get("gui", Gui(plt, name="Feasible Region", figsize=(15, 8)))
        self.save_images = kwargs.get("save_images", False)

    def save_image(self, file_name):
        if self.save_images:
            parent = Path(__file__).parent
            img_folder = Path(parent, "img")

            image_file = Path(img_folder, file_name)
            self.gui.plt.savefig(image_file, dpi="figure")

    def feasible_region(self):
        self.gui.create_figure()
        self.save_image("exerc01_a.png")

    def exerc01_a(self):
        self.gui.name = "Z: min 2x1-x2"
        self.gui.create_figure()
        self.gui.solution(2, -1, -25, 5)
        self.save_image("exerc01_a_1.png")

    def exerc01_b(self):
        self.gui.name = "Z: min 11x1-x2"
        self.gui.create_figure()
        self.gui.step = 5
        self.gui.solution(11, -1, -15, 5)
        self.save_image("exerc01_b.png")

    def exerc01_c(self):
        self.gui.name = "Z: min c1x1-x2"
        # self.gui.lines.append()

        # Checks if the lines are the same

        top = self.gui.lines[0].intersection(self.gui.lines[3], plotting=False)
        self.gui.lines.append(line(-1.5, -1, -10, "l1_2", type="line"))
        self.gui.lines.append(line(-0.1, -1, -5, "l4_2", type="line"))

        # print(c_0_25(top[0]), top[1])
        # print(c_1(top[0]), top[1])

        # self.gui.lines.append(extra_line)
        # self.gui.lines.append(extra_line2)
        self.gui.create_figure()
        # self.gui.step = 5
        # self.gui.solution(, -1, -15, 5)
        self.save_image("exerc01_c.png")


def main():
    gui = Gui(plt, name="Feasible Region", figsize=(15, 8))

    exerc01 = Exercise01(gui=gui, save_images=True)
    # exerc01.feasible_region()
    # exerc01.exerc01_a()
    # exerc01.exerc01_b()
    # exerc01.save_images = False
    exerc01.exerc01_c()

    gui.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        # input("Press Enter to continue...")
