# -*- coding:utf-8 -*-
from Point import *
import Array2D
from obstacle import SquareObstacle


class AStar:
    """
    AStar算法的Python3.x实现
    """

    class Node:  # 描述AStar算法中的节点数据
        def __init__(self, point, endPoint, g=0):
            self.point = point  # 自己的坐标
            self.father = None  # 父节点
            self.g = g  # g值，g值在用到的时候会重新算
            self.h = (abs(endPoint.x - point.x) + abs(endPoint.y - point.y)) * 10  # 计算h值

    def __init__(self, map2d, startPoint, endPoint, passTag=0):
        """
        构造AStar算法的启动条件
        :param map2d: Array2D类型的寻路数组
        :param startPoint: Point类型的寻路起点
        :param endPoint: Point类型的寻路终点
        :param passTag: int类型的可行走标记（若地图数据!=passTag即为障碍）
        """
        # 开启表
        self.openList = []
        # 关闭表
        self.closeList = []
        # 寻路地图
        self.map2d = map2d
        # 起点终点
        self.startPoint = startPoint
        self.endPoint = endPoint
        # 可行走标记
        self.passTag = passTag
        self.pathList = []

    def setNewMap(self, map2D):
        self.map2d = map2D

    def getMinNode(self):
        """
        获得openlist中F值最小的节点
        :return: Node
        """
        currentNode = self.openList[0]
        for node in self.openList:
            if node.g + node.h < currentNode.g + currentNode.h:
                currentNode = node
        return currentNode

    def pointInCloseList(self, point):
        for node in self.closeList:
            if node.point == point:
                return True
        return False

    def pointInOpenList(self, point):
        for node in self.openList:
            if node.point == point:
                return node
        return None

    def endPointInCloseList(self):
        for node in self.openList:
            if node.point == self.endPoint:
                return node
        return None

    def initObstacleArea(self, obstacles):
        for x in range(self.map2d.w):
            for y in range(self.map2d.h):
                for obs in obstacles:
                    if obs.minX < x < obs.maxX and \
                            obs.minY < y < obs.maxY:
                        self.map2d[x][y] = 1

    def addObastacleArea(self, obstacle):
        for x in range(obstacle.leftBottom.x, obstacle.rightUp.x):
            for y in range(obstacle.leftBottom.y, obstacle.rightUp.y):
                if self.map2d[x][y] != 1:
                    self.map2d[x][y] = 1

    def addAllObastacleArea(self, obstacles):
        for obstacle in obstacles:
            for x in range(obstacle.leftBottom.x, obstacle.rightUp.x):
                for y in range(obstacle.leftBottom.y, obstacle.rightUp.y):
                    if self.map2d[x][y] != 1:
                        self.map2d[x][y] = 1

    def getMap2D(self):
        return self.map2d

    def searchNear(self, minF, offsetX, offsetY):
        """
        搜索节点周围的点
        :param minF:F值最小的节点
        :param offsetX:坐标偏移量
        :param offsetY:
        :return:
        """
        # 越界检测
        if minF.point.x + offsetX < 0 or minF.point.x + offsetX > self.map2d.w - 1 or minF.point.y + offsetY < 0 or minF.point.y + offsetY > self.map2d.h - 1:
            return
        # 如果是障碍，就忽略
        if self.map2d[minF.point.x + offsetX][minF.point.y + offsetY] != self.passTag:
            return
        # 如果在关闭表中，就忽略
        currentPoint = Point(minF.point.x + offsetX, minF.point.y + offsetY)
        if self.pointInCloseList(currentPoint):
            return
        # 设置单位花费
        if offsetX == 0 or offsetY == 0:
            step = 10
        else:
            step = 14
        # 如果不再openList中，就把它加入openlist
        currentNode = self.pointInOpenList(currentPoint)
        if not currentNode:
            currentNode = AStar.Node(currentPoint, self.endPoint, g=minF.g + step)
            currentNode.father = minF
            self.openList.append(currentNode)
            return
        # 如果在openList中，判断minF到当前点的G是否更小
        if minF.g + step < currentNode.g:  # 如果更小，就重新计算g值，并且改变father
            currentNode.g = minF.g + step
            currentNode.father = minF

    def start(self):
        """
        开始寻路
        :return: None或Point列表（路径）
        """
        print("开始重新规划。。。")
        # 1.将起点放入开启列表
        startPoint = Point(int(self.startPoint.x), int(self.startPoint.y))
        endPoint = Point(int(self.endPoint.x), int(self.endPoint.y))
        startNode = AStar.Node(startPoint, endPoint)
        print("start() startPoint x:", startPoint.x, ",y:",endPoint.y,
              ",endpoint x:", endPoint.x, ",y:", endPoint.y)
        self.openList.append(startNode)
        # 2.主循环逻辑
        while True:
            # print("while main true....")
            # 找到F值最小的点
            minF = self.getMinNode()
            # print("is in obstacle:", self.isInObstacle(minF.point))
            # 把这个点加入closeList中，并且在openList中删除它
            self.closeList.append(minF)
            self.openList.remove(minF)
            # print("openlist len:", len(self.openList))
            # print("closeList len:", len(self.closeList))
            # 判断这个节点的上下左右节点
            self.searchNear(minF, 0, -1)
            self.searchNear(minF, 0, 1)
            self.searchNear(minF, -1, 0)
            self.searchNear(minF, 1, 0)
            self.searchNear(minF, -1, -1)
            self.searchNear(minF, -1, 1)
            self.searchNear(minF, 1, -1)
            self.searchNear(minF, 1, 1)
            # 判断是否终止
            point = self.endPointInCloseList()
            if point:  # 如果终点在关闭表中，就返回结果
                # print("关闭表中")
                cPoint = point
                pathList = []
                while True:
                    # print("while true....")
                    if cPoint.father:
                        pathList.append(cPoint.point)
                        cPoint = cPoint.father
                    else:
                        # print(pathList)
                        # print(list(reversed(pathList)))
                        # print(pathList.reverse())
                        self.pathList = list(reversed(pathList))
                        return self.pathList
            if len(self.openList) == 0:
                return None

    def getPathList(self):
        return self.pathList

    def setPathList(self):
        self.pathList = []

    def setOpenListEmpty(self):
        self.openList = []

    def setCloseListEmpty(self):
        self.closeList = []

    def isInObstacle(self, point):
        if self.map2d[point.x][point.y] == 1:
            return True
        else:
            return False



if __name__ == '__main__':
    map2d = Array2D.Array2D(50, 50)
    newAstar = AStar(map2d, Point(2, 4), Point(49, 49))
    # 设置障碍
    obstacleList = []
    obstacleList.append(SquareObstacle.SquareObstacle(Point(15, 14), Point(25, 24)))
    obstacleList.append(SquareObstacle.SquareObstacle(Point(32, 16), Point(42, 26)))
    newAstar.initObstacleArea(obstacleList)
    # 显示地图当前样子
    newAstar.getMap2D().showArray2D()
    # map2d.showArray2D()
    # 创建AStar对象,并设置起点为0,0终点为9,0
    # aStar = AStar(map2d, Point(2, 4), Point(29, 0))
    # 开始寻路
    pathList = newAstar.start()
    # 遍历路径点,在map2d上以'8'显示
    for point in pathList:
        newAstar.getMap2D()[point.x][point.y] = '#'
        # print(point)
    print("----------------------")
    # 再次显示地图
    newAstar.getMap2D().showArray2D()

    # obstacleList = []
    # newObstacle = SquareObstacle.SquareObstacle(Point(100, 100), Point(110, 110))
    # obstacleList.append(newObstacle)
