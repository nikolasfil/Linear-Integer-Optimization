import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

from plt_line import line

def plot_equations():

    # create the x axis points
    xAxis = np.linspace(-100, 100, 100000)

    # create the lines from the constraints
    l1 = line(2, 1, 4, "l1")
    l2 = line(1, 2, 5, "l2")
    l3 = line(1, -2, 1, "l3")
    l4 = line(0, 1, 0, "l4")
    l5 = line(1, 0, 0, "l5")

    # plot the lines
    l1.plot(xAxis, "blue")
    l2.plot(xAxis, l1.auto_color_chooser())
    l3.plot(xAxis, l2.auto_color_chooser())
    l4.plot(xAxis, "orange", lw= 4)
    l5.plot(xAxis, "orange", lw= 4)


    
    # fix the axis intersections
    # additional lines for help, temp measure
    line_x0 = line(1, 0, 0, "x=0")
    line_y10 = line(0, 1, 10, "y=10")
    line_x10 = line(1, 0, 10, "x=10")


    # fill the feasible space, based on the constraints
    # find the vector points (different name)
    # v0 = line_x0.intersection(line_y10)
    v0 = [0,10]
    # plt.plot(v0[0], v0[1], "o", color="red")

    # v1 = line_x0.intersection(l1)
    v1 = [0,4]
    plt.plot(v1[0], v1[1], "o", color="red")

    v2 = l1.intersection(l2)
    v3 = l2.intersection(l3)
    
    v4 = l3.intersection(line_x10)
    
    # v5 = line_x10.intersection(line_y10)
    v5 = [10,10]
    # plt.plot(v5[0], v5[1], "o", color="red")



    x = [i[0] for i in [v0, v1, v2, v3, v4, v5]]
    y = [i[1] for i in [v0, v1, v2, v3, v4, v5]]

    plt.fill(x, y, color="gray", alpha=0.5)
    

def graphical_solution():
    xAxis = np.linspace(0, 100, 100000)
    extra_lines = [line(2,-5,i,'extra',legend_show=False).plot(xAxis,'cornflowerblue') for i in range(-10,2)]




def main():
    plt.figure('a')
    plot_equations()
    graphical_solution()



    # plt.figure('b')
    # plot_equations()
    plt.show()

if __name__ == "__main__":
    main()
