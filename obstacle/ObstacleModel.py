# -*- coding:utf-8 -*-
from point_model import Point


# 目前假定障碍物的形状为正方形
class SquareObstacle:

    def __init__(self, leftUp, rightBottom):
        self.leftUp = leftUp
        self.rightBottom = rightBottom
        minX = leftUp.x
        maxX = rightBottom.x
        minY = leftUp.y
        maxY = rightBottom.y


