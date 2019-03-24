# -*- coding:utf-8 -*-
from point_model import Point  # 目前假定障碍物的形状为正方形


class SquareObstacle:
    leftBottom = Point(0, 0)
    rightUp = Point(0, 0)
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    def __init__(self, leftBottom, rightUp):
        self.leftBottom = leftBottom
        self.rightUp = rightUp
        self.minX = leftBottom.x
        self.maxX = rightUp.x
        self.minY = leftBottom.y
        self.maxY = rightUp.y
