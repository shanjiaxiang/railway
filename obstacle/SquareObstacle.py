# -*- coding:utf-8 -*-
from point_model import Point  # 目前假定障碍物的形状为正方形


class SquareObstacle:
    leftUp = Point(0, 0)
    rightBottom = Point(0, 0)
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    def __init__(self, leftUp, rightBottom):
        self.leftUp = leftUp
        self.rightBottom = rightBottom
        self.minX = leftUp.x
        self.maxX = rightBottom.x
        self.minY = leftUp.y
        self.maxY = rightBottom.y
