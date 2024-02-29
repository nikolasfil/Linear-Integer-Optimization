import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[3]))
from Tools.plt_line import line


def plot_equations():

    # create the x axis points
    xAxis = np.linspace(-100, 100, 100000)

    # create the lines from the constraints
    l1 = line(2, 1, 4, "l1", type="line")
    l2 = line(1, 2, 5, "l2", type="line")
    l3 = line(1, -2, 1, "l3", type="line")
    l4 = line(0, 1, 0, "l4", type="axis")
    l5 = line(1, 0, 0, "l5", type="axis")

    # plot the lines
    l1.plot(xAxis, "blue")
    l2.plot(xAxis, l1.auto_color_chooser())
    l3.plot(xAxis, l2.auto_color_chooser())

    l4.plot(xAxis, "orange", lw=4)

    l5.plot(xAxis, "orange", lw=4)

    line_x10 = line(1, 0, 10, "x=10")
    # line_x10.plot(xAxis, "orange", lw=4)

    # fill the feasible space, based on the constraints
    # find the vector points (different name)
    v0 = [0, 10]

    v1 = [0, 4]
    # l1 intersection with x=0
    plt.plot(v1[0], v1[1], "o", color="red")
    v2 = l1.intersection(l2)
    v3 = l2.intersection(l3)

    v4 = l3.intersection(line_x10, plotting=False)

    # corner point for the fill
    v5 = [10, 10]

    v = [v4, v5, v0, v1, v2, v3]
    print(v)

    # create the x and y coordinates for the fill
    x = [i[0] for i in v]
    y = [i[1] for i in v]

    # fill takes the x and y of a polygon and fills it with color
    plt.fill(x, y, color="gray", alpha=0.5)


def graphical_solution_max(a, b, minlim, maxlim, xAxis, legend=True):
    """plots the extra lines of the objective function"""
    extra_lines = [line(a, b, i, "extra") for i in range(minlim, maxlim)]
    for lin in extra_lines:
        lin.legend_show = legend
        lin.plot(xAxis, "cornflowerblue")
        # we need to find the intersection with the l3 (brown line) to find the max value of the objective function

        lin.intersection(line(1, -2, 1, "l3"))
        # prints the legend and the intersection points


def plt_settings(limit):
    # adjusts the dimentions of the plot
    plt.ylim(0, limit)
    plt.xlim(0, limit)
    plt.grid()


def main():
    xAxis = np.linspace(-100, 100, 100000)

    plt.figure("feasible region")
    plt_settings(10)
    plot_equations()
    # plt.savefig("exerc01-feasible_region.png", dpi="figure")

    plt.figure("a: max 2x1-5x2")
    plt_settings(10)
    plot_equations()
    graphical_solution_max(2, -5, 0, 2, xAxis=xAxis)
    # # plt.savefig("img/exerc01-a.png", dpi="figure")

    # plt.figure("b: max 2x1-4x2")
    # plt_settings(10)
    # plot_equations()
    # graphical_solution_max(2, -4, 0, 3, xAxis=xAxis)
    # # plt.savefig("exerc01-b.png", dpi="figure")

    # plt.figure("c: max 2x1-3x2")
    # plt_settings(10)

    # plot_equations()
    # graphical_solution_max(2, -3, 0, 20, xAxis=xAxis, legend=False)
    # plt.savefig("exerc01-c.png", dpi="figure")

    plt.show()


if __name__ == "__main__":
    main()
