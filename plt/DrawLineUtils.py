import matplotlib.pyplot as plt
import numpy as np
import _thread

xs = [0, 0]
ys = [1, 1]
xs1 = [0, 0]
ys1 = [1, 1]


class DrawLineUtils:
    color = ['red', 'blue', 'green', 'yellow', 'black', 'magenta']

    def __init__(self, size):
        self.preListX = []
        self.preListY = []
        self.initPlt(size)
        pass

    def initPlt(self, size):
        plt.axis([0, 60, 0, 50])
        plt.ion()
        plt.xlabel("Time(10s)")
        plt.ylabel("Points")
        plt.title("各闸机10s内规划点数")
        for i in range(size):
            self.preListX.append(0)
            self.preListY.append(0)

    def drawLines(self, curList):
        for i in range(len(curList)):
            x = self.preListX[i] + 1
            y = curList[i]
            plt.plot([self.preListX[i], x], [self.preListY[i], y], c=self.color[i])
            self.preListX[i] = x
            self.preListY[i] = y
            plt.show()


# plt.axis([0, 60, 0, 50])
# for i in range(100):
#     y = np.random.random()
#     xs[0] = xs[1]
#     ys[0] = ys[1]
#     xs[1] = i
#     ys[1] = y
#
#     xs1[0] = xs1[1]
#     ys1[0] = ys1[1]
#     xs1[1] = i + 1
#     ys1[1] = y + 1
#     plt.plot(xs, ys, c='red')
#     plt.plot(xs1, ys1, c='blue')
#     plt.pause(0.1)
# util = DrawLineUtils(6)
# for i in range(10):
#     util.drawLines([i+1,i+2,i+3,i+4,i+5,i+6])
#     plt.pause(0)
