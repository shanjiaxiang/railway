# -*- coding:utf-8 -*-
from turtle_util import *
from obstacle import SquareObstacle
from obstacle import DrawObstacleUtils
import turtle
import draw
from AStar import Array2D, AStar

obstacles = []
obastacleUtil = None
newMap = None
newAstar = None
pathList = None

def onClick(x, y):
    global obstacles
    global obastacleUtil
    global newAstar
    global newMap
    global pathList

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


    newAstar = AStar.AStar(newMap, Point(2, 4), Point(199, 199))
    newAstar.setPathList()
    newAstar.setOpenListEmpty()
    newAstar.setCloseListEmpty()

    newAstar.addObastacleArea(obstacle)
    print("map with obstacle:")
    newAstar.getMap2D().showArray2D()

    # 开始寻路
    pathList = newAstar.start()
    # 遍历路径点,在map2d上以'#'显示
    if pathList is None:
        print("规划路径为空")
        return
    for point in pathList:
        newAstar.getMap2D()[point.x][point.y] = '#'
        # print(point)
    print("after plan----------------------")
    # 再次显示地图
    newAstar.getMap2D().showArray2D()
    print("end-------------------")

def main():
    global obstacles
    global obastacleUtil
    global newMap
    global newAstar

    width = 200
    height =200

    initCanvas(width, height)
    hideTurtle()
    turtle.setworldcoordinates(0, 0, width, height)
    turtle.hideturtle()
    turtleSpeed(0)
    turtle.delay(0)

    obstacles = []
    obastacleUtil = DrawObstacleUtils.DrawObstacleUtils((width, height), obstacles)
    turtle.onscreenclick(onClick)

    # drawUtil = draw.DrawUtils(50, 50, )
    # draw.fun_genUsers()
    # draw.fun_refresh()

    newMap = Array2D.Array2D(width, height)
    # newAstar = AStar.AStar(newMap, Point(2, 4), Point(49, 49))

    turtle.mainloop()
    turtle.done()

if __name__ == '__main__':
  main()
