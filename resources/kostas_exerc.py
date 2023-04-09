import matplotlib.pyplot as plt
import numpy as np


def plot_settings():
    plt.ylim(-1, 10)
    plt.xlim(-1, 10)
    plt.grid()
    plt.legend()


def plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1, xCorner2, yCorner1, yCorner2):
    plt.plot(xAxis, l1, label="6x1 + 3x2 = 12", color="blue")
    plt.plot(xAxis, l2, label="4x1 + 8x2 = 16", color="yellow")
    plt.plot(xAxis, l3, label="6x1 + 5x2 = 30", color="green")
    plt.plot(xAxis, l4, label="6x1 + 7x2 = 36", color="red")
    plt.plot(xAxis, y, label="x1 = 0", color="orange")
    plt.plot(y, xAxis, label="x2 = 0", color="brown")

    plt.fill(xCorner1, yCorner1, color="gray", alpha=0.5)
    plt.fill(xCorner2, yCorner2, color="gray", alpha=0.5)


def main():
    xAxis = np.linspace(-100, 100, 100000)

    # Axis
    y = np.poly1d([0])
    
    # Z
    Z = []
    for i in range(3, 17, 1):
        Z.append(np.poly1d([-3, i]))


    # Restraints
    # 6x1 + 3x2 = 12 <=> x2 = -2x1 + 4
    restraint1 = [-2, 4]
    # 4x1 + 8x2 = 16 <=> x2 = -(0.5)x1 + 2
    restraint2 = [-0.5, 2]
    # 6x1 + 5x2 = 30 <=> x2 = -6/5x1 + 6
    restraint3 = [-(6/5), 6]
    # 6x1 + 7x2 = 36 <=> x2 = -(6/7)x1 + (36/7)
    restraint4 = [-(6/7), (36/7)]
    
    ##########################################
    res1 = np.poly1d(restraint1)
    res2 = np.poly1d(restraint2)
    res3 = np.poly1d(restraint3)
    res4 = np.poly1d(restraint4)
    l1 = res1(xAxis)
    l2 = res2(xAxis)
    l3 = res3(xAxis)
    l4 = res4(xAxis)
    y = y(xAxis)
    ##########################################
    xCorner1 = [0, 15/6, 5, 4]
    yCorner1 = [36/7, 3, 0, 0]
    xCorner2 = [0, 0, 4/3, 4]
    yCorner2 = [36/7, 4, 4/3, 0]
    ##########################################
    plt.figure("a")
    plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1,
                 xCorner2, yCorner1, yCorner2)
    plt.plot(xAxis, Z[0](xAxis), color="purple", label="maxZ = 3x1 + x2")
    for i in range(1, len(Z)):
        plt.plot(xAxis, Z[i](xAxis), color="purple")
    plot_settings()
    ##########################################
    # Define the area of the solutions

    ##########################################
    # Question B
    ##########################################
    plt.figure("b")
    plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1,
                 xCorner2, yCorner1, yCorner2)
    newZ = []
    values = [1.9, 4.2]
    for i in values:
        c = (3/4) * i - 1
        print(c)
        newZ.append(np.poly1d([-(1/c), (1/c) * i]))
        plt.plot(xAxis, newZ[-1](xAxis),
                 label=f"c2 = {c}", color="yellow" if i == 1.9 else "blue")
    plot_settings()
    ###########################################
    # Question C
    ###########################################
    plt.figure('c')
    plot_problem(l1, l2, l3, l4, xAxis, y, xCorner1,
                 xCorner2, yCorner1, yCorner2)
    values = [1.1, 0.9]
    newZ = []
    for i in values:
        newZ.append(np.poly1d([-(i), 2.5 * i + 3]))
        plt.plot(xAxis, newZ[-1](xAxis),
                 label=f"-c1/c2 = {-i}", color="green" if i == 0.9 else "red")
        ###########################################
    plot_settings()
    plt.show()


if __name__ == "__main__":
    main()
