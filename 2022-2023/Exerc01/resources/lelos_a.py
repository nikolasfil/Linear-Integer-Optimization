import numpy as np
import matplotlib.pyplot as plt


class Line:
    def __init__(self, a: int, b: int, c: int, name: str, bigger: bool = True):
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self.bigger = bigger

    def createLineY(self, x):
        return (self.c-self.a*x)/self.b

    def parameters(self):
        return self.a, self.b, self.c

    def findIntersection(self, line, show: bool = False):
        x = (self.c/self.b-line.c/line.b)/(self.a/self.b-line.a/line.b)
        y = self.createLineY(x)
        plt.plot(x, y, "o", label=self.name+","+line.name+f" ({x},{y})")
        if (show):
            plt.xlim([0, 10])
            plt.ylim([0, 10])
            plt.legend()
            plt.show()
        return (x, y)

    def createPlot(self, x1, show: bool = False):
        plt.plot(x1, self.createLineY(x1), label=self.name)
        if (show):
            plt.xlim([0, 10])
            plt.ylim([0, 10])
            plt.legend()
            plt.show()


# x1 = np.arange(0,10,0.01)
# plt.plot(4-2*x1,label = "P1")
# plt.plot((5-x1)/2,label = "P2")
# plt.plot(-(1+x1)/2,label = "P3")
# # plt.plot(x1, x1)
# plt.legend()

l1 = Line(2, 1, 4, "P1")
l2 = Line(1, 2, 5, "P2")
l3 = Line(1, -2, 1, "P3")

x = np.linspace(0, 1000, 10000)

# y = l1.createLineY(x)


# l1.createPlot(x)
# l2.createPlot(x)
# l3.createPlot(x)

# l1.findIntersection(l2)
# l2.findIntersection(l3)
# l3.findIntersection(l1)

# plt.fill_between(x1,4-2*x1,(1+x1)/2)
# plt.fill_between(x1,(5-x1)/2,(1+x1)/2)
# plt.fill_between(x1,(5-x1)/2,4-2*x1)

# def findIntersectionPoints()


def createLowerBound(line1, line2, line3):
    boundFunction = []
    for i, x in enumerate(line1):
        if x > line2[i] and x > line3[i]:
            boundFunction.append(x)
        elif x > line2[i] and x < line3[i]:
            boundFunction.append(line3[i])
        elif x < line2[i] and x > line3[i]:
            boundFunction.append(line2[i])
        else:
            if (line2[i] > line3[i]):
                boundFunction.append(line2[i])
            else:
                boundFunction.append(line3[i])
        #     else:
        #         boundFunction.append(line3[i])
        # else:
        #     boundFunction.append(line2[i])

    return boundFunction


lowerBound = createLowerBound(l1.createLineY(
    x), l2.createLineY(x), l3.createLineY(x))

z_max_constans = [[2, -5], [2, -4], [2, -3]]
z_max = 0
for z in z_max_constans:
    a_z = z[0]
    b_z = z[1]

    l1.createPlot(x)
    l2.createPlot(x)
    l3.createPlot(x)

    l1.findIntersection(l2)
    l2.findIntersection(l3)
    l3.findIntersection(l1)

    # np.linspace(-100,100,201) ):
    np_list = list(np.linspace(-40, 9.9, 51))
    notfoundIt = True
    for i, M in enumerate(np_list):
        y = Line(a_z, b_z, M, f"Max {i}")
        # max_z.append(y)
        line = y.createLineY(x)
        line[line < lowerBound] = np.nan
        if not all([np.isnan(v) for v in line]):
            z_max = M
        if (i == 0):
            plt.text(0, y.createLineY(0), "z = " +
                     f"{b_z*y.createLineY(0): .0f}")
        if (z_max != 0 and notfoundIt):
            y = Line(a_z, b_z, M+1, f"Max {i}")
            # max_z.append(y)
            line = y.createLineY(x)
            line[line < lowerBound] = np.nan
            if all([np.isnan(v) for v in line]):
                # z_max = 0
                notfoundIt = False
                plt.text(3, y.createLineY(3), "z = " +
                         f"{z_max:.0f}")
        plt.plot(x, line, color=((51-10+M)/51, 0.1, 0.3))
    print(f"{z_max:.0f}")
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.legend()
    # plt.colorbar(np.linspace(-40, 10, 51))
    plt.show()


# plt.plot(l1.createLineY(x)[(l1.createLineY(x)>l2.createLineY(x) and l1.createLineY(x)>l3.createLineY(x))])
# plt.plot(l2.createLineY(x)[(l2.createLineY(x)>l1.createLineY(x) and l2.createLineY(x)>l3.createLineY(x))])
# plt.plot(l3.createLineY(x)[(l3.createLineY(x)>l1.createLineY(x) and l3.createLineY(x)>l1.createLineY(x))])
# plt.show()