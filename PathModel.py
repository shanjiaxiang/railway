class PathModel:
    destIndex = 0
    pathList = []
    distance = 0

    def __init__(self, destIndex, pathList, distance):
        self.destIndex = destIndex
        self.pathList = pathList
        self.distance = self.calPathLength()

    def calPathLength(self):
        length = 0
        for x in range(len(self.pathList) - 1):
            absX = abs(self.pathList[x].x - self.pathList[x + 1].x)
            absY = abs(self.pathList[x].y - self.pathList[x + 1].y)
            if absX == 1 and absY == 1:
                length += 1.4
            elif absX == 1 and absY == 0:
                length += 1
            elif absX == 0 and absY == 1:
                length += 1
            else:
                length += 1
                print("路径中存在不相邻点")
        return round(length, 2)
