# -*- coding:utf-8 -*-
import random
from point_model import *

# 获取控制点y坐标
def controlPointY(pS, pD, controlPointX):
    # 控制点取自中垂线
    # -(Bx-Ax)/(By-Ay)x+(Bx-Ax)/(By-Ay)*(Ax+Bx)/2+(Ay+By)/2
    return ((-1 * (pD.x - pS.x)) / (pD.y - pS.y)) * controlPointX + ((pD.x - pS.x) / (
        pD.y - pS.y)) * (pS.x + pD.x) / 2 + (pS.y + pD.y) / 2

# 获取控制点x坐标
def controlPointX(pS, pD, controlPointY):
    # 控制点取自中垂线
    # -(Bx-Ax)/(By-Ay)x+(Bx-Ax)/(By-Ay)*(Ax+Bx)/2+(Ay+By)/2
    if pD.y == pS.y:
        pD.y = pD.y + 0.01
    if pD.x == pS.x:
        pD.x = pD.x + 0.01
    return (controlPointY - (pS.y + pD.y) / 2 - ((pD.x - pS.x) / (
        pD.y - pS.y)) * (pS.x + pD.x) / 2) / ((-1 * (pD.x - pS.x)) / (pD.y - pS.y))

# 计算控制点
def calControlPoint(pS, pD):
    k = getGradient(pS, pD)
    # print("k " , k)
    if k > 1:
        midx = (pS.x+pD.x)/2
        min = midx - abs(pS.y-pD.y)/2
        max = midx + abs(pS.y-pD.y)/2
        # print("(pS.y-pD.y)/2",abs(pS.y-pD.y)/2)
        # print("midx", midx)
        # print("min", min)
        # print("max", max)
        midx = random.uniform(min, max)
        midy = controlPointY(pS,pD, midx)
    else:
        midy = (pS.y + pD.y) / 2
        min = midy - abs(pS.x - pD.x) / 2
        max = midy + abs(pS.x - pD.x) / 2
        # print("(pS.x - pD.x) / 2", abs(pS.x - pD.x) / 2)
        # print("midx", midy)
        # print("min", min)
        # print("max", max)
        midy = random.uniform(min, max)
        midx = controlPointX(pS, pD, midy)
    point = Point(midx, midy)
    return point

# 起始点、终点，获得t时刻弧线上的点
def calCurvePoint(t, start, dest):
    control = calControlPoint(start, dest)
    return calCurvePointWithControl(t, start, control, dest)

# 通过控制点获得弧线上t时刻的点
def calCurvePointWithControl(t, start, control, dest):
    x = start.x * pow(1 - t, 2) \
        + control.x * t * (1 - t) * 2 \
        + dest.x * pow(t, 2)

    y = start.y * pow(1 - t, 2) \
        + control.y * t * (1 - t) * 2 \
        + dest.y * pow(t, 2)
    return Point(x, y)

# 斜率
def getGradient(pointS, pointD):
    if pointS.x != pointD.x:
        k = (pointS.y - pointD.y) / (pointS.x - pointD.x)
        return abs(k)
    else:
        return 0