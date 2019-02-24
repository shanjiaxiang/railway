# -*- coding:utf-8 -*-
from turtle_util import *
from obstacle import SquareObstacle
from obstacle import DrawObstacleUtils
import turtle
import draw
from AStar import Array2D, AStar
import threading

obstacles = []
obastacleUtil = None
newMap = None
newAstar = None
pathList = None
startPoint = Point(100, 100)
destPoint = Point(199, 199)


def onClick(x, y):
    global obstacles
    global obastacleUtil
    global newAstar
    global newMap
    global pathList
    global startPoint
    global destPoint

    # 是否生成障碍物
    obstacle = obastacleUtil.getObstacle(x, y)
    if obstacle is None:
        return
    else:
        # 如果之前有路径
        if pathList is not None:
            for point in pathList:
                newMap = newAstar.getMap2D()
                newMap[point.x][point.y] = 0

    newAstar = AStar.AStar(newMap, startPoint, destPoint)
    newAstar.setPathList()
    newAstar.setOpenListEmpty()
    newAstar.setCloseListEmpty()

    newAstar.addObastacleArea(obstacle)
    print("map with obstacle:")
    # newAstar.getMap2D().showArray2D()

    # 开始寻路
    pathList = newAstar.start()
    # 遍历路径点,在map2d上以'#'显示
    if pathList is None:
        print("规划路径为空")
        return
    else:
        length = calPathLength(pathList)
        print("规划路径长度为", length)

    # for point in pathList:
    #     newAstar.getMap2D()[point.x][point.y] = '#'
    # print("after plan----------------------")
    # 再次显示地图
    # newAstar.getMap2D().showArray2D()
    # print("end-------------------")


def calNextPosition(speed, time, paths):
    if (paths is None) or (len(paths) < 1):
        return None
    distance = round(speed * time, 2)
    length = 0
    newPaths = []
    size = len(paths) - 1
    print("移除前size:", size)
    for x in range(size):
        absX = abs(paths[x].x - paths[x + 1].x)
        absY = abs(paths[x].y - paths[x + 1].y)
        if absX == 1 and absY == 1:
            length += 1.4
        elif absX == 1 and absY == 0:
            length += 1
        elif absX == 0 and absY == 1:
            length += 1
        else:
            length += 1
            print("路径中存在不相邻点")
        newPaths.append(paths[x])
        length = round(length, 2)
        if length >= distance:
            nextPoint = paths[x]
            print("第几个点：", x)
            for point in newPaths:
                paths.remove(point)
            print("移除后路径size:", len(paths))
            return nextPoint
    nextPoint = paths[-1]
    paths.clear()
    return nextPoint


def calPathLength(path):
    length = 0
    for x in range(len(path) - 1):
        absX = abs(path[x].x - path[x + 1].x)
        absY = abs(path[x].y - path[x + 1].y)
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


def initCanvasHere(width, height):
    initCanvas(width, height)
    hideTurtle()
    turtle.setworldcoordinates(0, 0, width, height)
    turtle.hideturtle()
    turtleSpeed(0)
    turtle.delay(0)


def drawPosition():
    clear()
    drawPoint(startPoint, 10)
    drawPoint(destPoint, 10)
    nextPoint = calNextPosition(5, 1, pathList)
    if nextPoint is not None:
        drawPoint(nextPoint, 10)
    # 每秒计算一次
    timer = threading.Timer(1, drawPosition)
    timer.start()


def main():
    global obstacles
    global obastacleUtil
    global newMap
    global newAstar

    width = 200
    height = 200

    initCanvasHere(width, height)

    obstacles = []
    obastacleUtil = DrawObstacleUtils.DrawObstacleUtils((width, height), obstacles)
    turtle.onscreenclick(onClick)

    timer = threading.Timer(1, drawPosition)
    timer.start()

    # drawUtil = draw.DrawUtils(50, 50, )
    # draw.fun_genUsers()
    # draw.fun_refresh()

    newMap = Array2D.Array2D(width, height)
    # newAstar = AStar.AStar(newMap, Point(2, 4), Point(49, 49))

    turtle.mainloop()
    turtle.done()


if __name__ == '__main__':
    main()
