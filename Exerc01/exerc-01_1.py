import matplotlib.pyplot as plt
import numpy as np

from plt_line import Line



def plot_settings():
    plt.ylim(0, 10)
    plt.xlim(0, 10)
    plt.grid()
    plt.legend()


def plot_problem(l1, l2, l3, xAxis, y, xCorner1, xCorner2, yCorner1, yCorner2):
    plt.plot(xAxis, l1, label="2x1+x2 = 4", color="blue")
    plt.plot(xAxis, l2, label="x1 + 2x2 = 5", color="yellow")
    plt.plot(xAxis, l3, label="x1 - 2x2 = 1", color="green")
    plt.plot(xAxis, y, label="x1 = 0", color="orange")
    plt.plot(y, xAxis, label="x2 = 0", color="brown")

    plt.fill(xCorner1, yCorner1, color="gray", alpha=0.5)
    # plt.fill(xCorner2, yCorner2, color="gray", alpha=0.5)


def main_plot():
    xAxis = np.linspace(-100, 100, 100000)

    # Axis
    y = np.poly1d([0])

    # Z
    Z = []
    for i in range(3, 17, 1):
        Z.append(np.poly1d([-3, i]))

    # Restraints

    # 2x1+x2 = 4 <=> x2 = -2x1 + 4
    restraint1 = [-2, 4]
    # x1 + 2x2 = 5 <=> x2 = -0.5x1 + 2.5
    restraint2 = [-0.5, 2.5]
    # x1 - 2x2 = 1 <=> x2 = 0.5x1 - 0.5
    restraint3 = [0.5, -0.5]

    ##########################################
    res1 = np.poly1d(restraint1)
    res2 = np.poly1d(restraint2)
    res3 = np.poly1d(restraint3)

    l1 = res1(xAxis)
    l2 = res2(xAxis)
    l3 = res3(xAxis)

    y = y(xAxis)

    ##########################################
    xCorner1 = [1, 7/5, 3]
    yCorner1 = [0, 1/5, 1]
    xCorner2 = [1, 7/5, 3]
    yCorner2 = [0, 1/5, 1]

    ##########################################

    plt.figure("a")

    plot_problem(l1, l2, l3, xAxis, y, xCorner1,
                 xCorner2, yCorner1, yCorner2)

    # plt.plot(xAxis, Z[0](xAxis), color="purple", label="maxZ = 3x1 + x2")

    # for i in range(1, len(Z)):
    #     plt.plot(xAxis, Z[i](xAxis), color="purple")

    plot_settings()
    ##########################################
    # Define the area of the solutions

    # ##########################################
    # # Question B
    # ##########################################
    # plt.figure("b")
    # plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1,
    #              xCorner2, yCorner1, yCorner2)
    # newZ = []
    # values = [1.9, 4.2]
    # for i in values:
    #     c = (3/4) * i - 1
    #     print(c)
    #     newZ.append(np.poly1d([-(1/c), (1/c) * i]))
    #     plt.plot(xAxis, newZ[-1](xAxis),
    #              label=f"c2 = {c}", color="yellow" if i == 1.9 else "blue")
    # plot_settings()
    # ###########################################
    # # Question C
    # ###########################################
    # plt.figure('c')
    # plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1,
    #              xCorner2, yCorner1, yCorner2)
    # values = [1.1, 0.9]
    # newZ = []
    # for i in values:
    #     newZ.append(np.poly1d([-(i), 2.5 * i + 3]))
    #     plt.plot(xAxis, newZ[-1](xAxis),
    #              label=f"-c1/c2 = {-i}", color="green" if i == 0.9 else "red")
    #     ###########################################
    plot_settings()
    plt.show()


def main():
    l1 = Line(2, 1, 4, "l1")
    l2 = Line(1, 2, 5, "l2")
    l3 = Line(1, -2, 1, "l3")
    l4 = Line(0, 1, 0, "l4")
    l5 = Line(1, 0, 0, "l5")

    v1 = l1.intersection(l2)
    v3 = l2.intersection(l3)

    print(l1.equation(2))
    xAxis = np.linspace(-100, 100, 100000)

    l1.plot(xAxis, "blue")
    l2.plot(xAxis, "yellow")
    l3.plot(xAxis, "green")
    l4.plot(xAxis, "orange", lw= 4)
    l5.plot(xAxis, "orange", lw= 4)

    plt.show()


if __name__ == "__main__":
    main()
    # l1 = line(2,1,4,"l1")
    # print(l1.a,l1.b,l1.c,l1.name)
