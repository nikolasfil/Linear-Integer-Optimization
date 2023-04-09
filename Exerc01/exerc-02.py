import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

from plt_line import line


def plot_equations():

    # create the x axis points
    xAxis = np.linspace(-100, 100, 100000)

    # create the lines from the constraints
    l1 = line(-6, -4.5, -5.1, "l1")
    l2 = line(6,  9, 8.4, "l2")
    l3 = line(12, 9, 10.8, "l3")
    l4 = line(0, 1, 0, "l4")
    l5 = line(1, 0, 0, "l5")
    l6 = line(1, 1, 1, "l6")
    l7 = line(-1, -1, -1, "l7")

    # plot the lines
    l1.plot(xAxis, "blue")
    l2.plot(xAxis, l1.auto_color_chooser())
    l3.plot(xAxis, l2.auto_color_chooser())
    l6.plot(xAxis, l3.auto_color_chooser())
    l7.plot(xAxis, l6.auto_color_chooser())

    l4.plot(xAxis, "orange", lw=4)

    l5.plot(xAxis, "orange", lw=4)

    
    v1 = l2.intersection(l7)
    v3 = l1.intersection(l7)


def plt_settings(limit):
    plt.ylim(0, limit)
    plt.xlim(0, limit)
    plt.grid()


def main():
    xAxis = np.linspace(-100, 100, 100000)

    plt.figure('min 6x1-7.5x2')
    plt_settings(1.4)
    plot_equations()

    # extra_lines = [line(6, -7.5, c, 'extra') for c in range(0, 5)]
    # for lin in extra_lines:
    #     lin.legend_show = False
    #     lin.plot(xAxis, 'cornflowerblue')

    plt.show()


if __name__ == "__main__":
    main()
