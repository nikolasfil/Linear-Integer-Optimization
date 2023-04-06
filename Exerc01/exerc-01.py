import numpy as np
import matplotlib.pyplot as plt

# def graph(formula,x_range, color='g'):
#     x = np.array(x_range)
#     y = formula(x)

#     plt.plot(x,y,color)
#     plt.show()


def graph(formulas,x_range):
    # plt.figure()
    # plt.subtitle('Exercise 1 Graph')
    plt.axis([0,10,0,10])
    colors = ['b','g','r']
    x = np.array(x_range)
    
    for i,f in enumerate(formulas):
        y = f(x)
        plt.plot(x,y,colors[i])
    plt.show()

def line_p1(x1):
    return 4 - x1*2

def line_p2(x1):
    return (5 - x1)/2

def line_p3(x1):
    return (-1 + x1)/2

graph([line_p1,line_p2,line_p3], range(0,10))
