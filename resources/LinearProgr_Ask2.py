import matplotlib.pyplot as plt
import numpy as np


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
        if ((self.a/self.b-line.a/line.b) == 0):
            if ((self.c/self.b-line.c/line.b) == 0):
                x = self.c/self.b
            else:
                x = np.nan
        else:
            x = (self.c/self.b-line.c/line.b)/(self.a/self.b-line.a/line.b)
        y = self.createLineY(x)
        plt.plot(x, y, "o", label=self.name+"," +
                 line.name+f" ({x:.3f},{y:.3f})")
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


FI = Line(6, 4.5, 5.1, "FI")
Lip = Line(6, 9, 8.4, "Lip")
Prot = Line(12, 9, 10.8, "Prot")
Prod = Line(1, 1, 1, "Prod")


x = np.linspace(0, 1000, 10000)

# FI.createPlot(x)
# Lip.createPlot(x)
# Prot.createPlot(x)

# # FI.findIntersection(Lip)
# # Lip.findIntersection(Prot)
# # Prot.findIntersection(FI)

# plt.xlim([0, 10])
# plt.ylim([0, 10])

# plt.show()

FI.createPlot(x)
Lip.createPlot(x)
Prot.createPlot(x)
Prod.createPlot(x)

FI.findIntersection(Lip)
Lip.findIntersection(Prot)
Prot.findIntersection(FI)
Prod.findIntersection(FI)
Prod.findIntersection(Prot)
Prod.findIntersection(Lip)


# # np.linspace(-100,100,201) ):
# for i, M in enumerate(np.linspace(-100, 99.9, 201)):
#     y = Line(a_z, b_z, M, f"Max {i}")
#     # max_z.append(y)
#     line = y.createLineY(x)
#     line[line < lowerBound] = np.nan
#     if not all([np.isnan(v) for v in line]):
#         z_max = M

#     plt.plot(x, line, 'b')
# print(z_max)
# z_max = 0
# a_z = 6
# b_z = 7.5
# # np.linspace(-100,100,201) ):
# np_list = list(np.linspace(-40, 9.9, 51))
# notfoundIt = True
# lowerBound = FI.createLineY(x)
# protLine = Prot.createLineY(x)
# lipLine = Lip.createLineY(x)
# for i, y in enumerate(lowerBound):
#     if y > protLine[i]:
#         lowerBound[i] = protLine[i]

# # upperBound = lipLine
# for i, y in enumerate(lowerBound):
#     if y > lipLine[i]:
#         lowerBound[i] = lipLine[i]

# lowerBound[lowerBound < FI.createLineY(x)] = FI.createLineY(x)
# lowerBound[lowerBound > Lip.createLineY(x)] = Lip.createLineY(x)
# lowerBound[lowerBound > Prot.createLineY(x)] = Prot.createLineY(x)

# for i, M in enumerate(np_list):
#     y = Line(a_z, b_z, M, f"Max {i}")
#     # max_z.append(y)
#     line = y.createLineY(x)
#     line[line < lowerBound] = np.nan
#     if not all([np.isnan(v) for v in line]):
#         z_max = M
#     if (i == 0):
#         plt.text(0, y.createLineY(0), "z = " +
#                  f"{b_z*y.createLineY(0): .0f}")
#     if (z_max != 0 and notfoundIt):
#         y = Line(a_z, b_z, M+1, f"Max {i}")
#         # max_z.append(y)
#         line = y.createLineY(x)
#         line[line < lowerBound] = np.nan
#         if all([np.isnan(v) for v in line]):
#             # z_max = 0
#             notfoundIt = False
#             plt.text(3, y.createLineY(3), "z = " +
#                      f"{z_max:.0f}")
#     plt.plot(x, line, color=((51-10+M)/51, 0.1, 0.3))
# print(f"{z_max:.0f}")
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.legend()
# plt.colorbar(np.linspace(-40, 10, 51))
plt.xlim([0, 1.4])
plt.ylim([0, 1.4])
plt.legend()
plt.show()
