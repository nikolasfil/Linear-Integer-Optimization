import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from Tools.plt_line import line
from Tools.linearGui import LinearGUI


class Exerc01Gui(LinearGUI):
    def __init__(self, *args, **kwargs) -> None:
        limit = 30

        kwargs["limit"] = limit
        super().__init__(*args, **kwargs)
        self.lines = []
        self.lines.append(line(1, 1, 10, "l1", type="line"))
        self.lines.append(line(-10, 1, 10, "l2", type="line"))
        self.lines.append(line(-4, 1, 20, "l3", type="line"))
        self.lines.append(line(1, 4, 20, "l4", type="line"))

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

    def save_image(self, file_name):
        if self.save_images:
            parent = Path(__file__).parent
            img_folder = Path(parent, "img")

            image_file = Path(img_folder, file_name)
            self.plt.savefig(image_file, dpi="figure")

    def feasible_region(self):
        self.create_figure()
        self.save_image("exerc01_a.png")

    def exerc01_a(self):
        self.name = "Z: min 2x1-x2"
        self.create_figure()
        self.step = 5
        self.graphical_solution(2, -1, -25, 5)
        self.save_image("exerc01_a_1.png")

    def exerc01_b(self):
        self.name = "Z: min 11x1-x2"
        self.create_figure()
        self.step = 5
        self.graphical_solution(11, -1, -15, 5)
        self.save_image("exerc01_b.png")

    def exerc01_c(self):
        self.name = "Z: min c1x1-x2"

        # Checks if the lines are the same

        top = self.lines[0].intersection(self.lines[3], plotting=False)
        self.lines.append(line(-1.5, -1, -10, "l1_2", type="line"))
        self.lines.append(line(-0.1, -1, -5, "l4_2", type="line"))

        self.create_figure()
        # self.step = 5
        # self.solution(, -1, -15, 5)
        self.save_image("exerc01_c.png")

    def main(self):

        self.save_images = False
        self.feasible_region()
        self.exerc01_a()
        self.exerc01_b()
        self.exerc01_c()
        # self.show()


if __name__ == "__main__":
    try:
        gui = Exerc01Gui(plt, name="Feasible Region", figsize=(15, 8))
        gui.main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        # input("Press Enter to continue...")
