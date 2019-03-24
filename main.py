# -*- coding:utf-8 -*-
from turtle_util import *
from obstacle import SquareObstacle
from obstacle import DrawObstacleUtils
from turtle import TurtleScreen, RawTurtle, TK
import turtle
import draw
from AStar import Array2D, AStar
import threading
from config import Configurations

obstacles = []
obstacles2 = []

obastacleUtil = None
drawUtil = None
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


def addObstacle(x, y):
    global obstacles
    global obstacles2
    global drawUtil
    global obastacleUtil
    # 是否生成障碍物
    obstacle = obastacleUtil.getObstacle(x, y)
    if obstacle is None:
        return
    else:
        # obstacles.append(obstacle)
        # if x >150:
        #     drawUtil.OBSTACLE_LIST2 = obstacles
        # else:
        #     drawUtil.OBSTACLE_LIST = obstacles
        drawUtil.OBSTACLE_LIST = obastacleUtil.getObstacles()
        drawUtil.OBSTACLE_LIST1 = obastacleUtil.getObstacles1()
        obstacles = obastacleUtil.getObstacles()
        obstacles2 = obastacleUtil.getObstacles1()
        print("after add size:", len(drawUtil.OBSTACLE_LIST))


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


def initDrawUtil(width, height, startPoint, startPoint2):
    global drawUtil
    global obstacles
    global obstacles2
    dests = []
    dests.append(DestinationModel(0, "闸机1", Point(50, 50)))
    dests.append(DestinationModel(1, "闸机2", Point(50, 100)))
    dests.append(DestinationModel(2, "闸机3", Point(50, 150)))
    dests.append(DestinationModel(3, "闸机4", Point(150, 50)))
    dests.append(DestinationModel(4, "闸机5", Point(150, 100)))
    dests.append(DestinationModel(5, "闸机6", Point(150, 150)))

    dests2 = []
    dests2.append(DestinationModel(0, "闸机1", Point(250, 50)))
    dests2.append(DestinationModel(1, "闸机2", Point(250, 100)))
    dests2.append(DestinationModel(2, "闸机3", Point(250, 150)))
    dests2.append(DestinationModel(3, "闸机4", Point(350, 50)))
    dests2.append(DestinationModel(4, "闸机5", Point(350, 100)))
    dests2.append(DestinationModel(5, "闸机6", Point(350, 150)))
    # drawUtil2 = draw.DrawUtils(width, height, startPoint2, dests2)

    drawUtil = draw.DrawUtils(width, height, startPoint, dests, startPoint2, dests2, obstacles, obstacles2)
    drawUtil.fun_genUsers()
    drawUtil.startRefresh()


def main():
    global obstacles
    global obstacles2
    global obastacleUtil
    global newMap
    global newAstar
    global drawUtil

    width = Configurations.width
    height = Configurations.height

    initCanvasHere(width, height)

    # root = TK.Tk()
    # root1 = TK.Tk()
    # cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")
    # cv2 = TK.Canvas(root1, width=300, height=200, bg="#ffeeee")
    # cv1.pack()
    # cv2.pack()
    #
    # s1 = TurtleScreen(cv1)
    # s1.bgcolor(0.85, 0.85, 1)
    # s2 = TurtleScreen(cv2)
    # s2.bgcolor(1, 0.85, 0.85)

    # p = RawTurtle(s1)
    # q = RawTurtle(s2)

    obstacles = []
    obstacles2 = []
    obstacles.append(SquareObstacle.SquareObstacle(Point(100, 60), Point(100 + 10, 60 + 10)))
    obstacles.append(SquareObstacle.SquareObstacle(Point(130, 90), Point(130 + 10, 90 + 10)))
    obstacles2.append(SquareObstacle.SquareObstacle(Point(300, 60), Point(300 + 10, 60 + 10)))
    obstacles2.append(SquareObstacle.SquareObstacle(Point(330, 90), Point(330 + 10, 90 + 10)))
    obastacleUtil = DrawObstacleUtils.DrawObstacleUtils((width, height), obstacles, obstacles2)
    turtle.onscreenclick(addObstacle)
    initDrawUtil(width, height, Point(50, 50),Point(250, 50))

    newMap = Array2D.Array2D(width, height)

    turtle.mainloop()
    turtle.done()


if __name__ == '__main__':
    main()
