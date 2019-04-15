import common_utils
import random
import os
import sys

class FileUtils:
    @staticmethod
    def writeFile():
        f = open(r'..\data\data.txt', 'w')
        timeList = common_utils.getRandomListByTime(300000, 1000)
        for x in range(len(timeList)):
            timeList[x] = str(timeList[x]) + '\n'
        f.writelines(timeList)

    @staticmethod
    def readFile():
        listTime = []
        filePath = r'data.txt'
        print(FileUtils.resource_path(filePath))

        f = open(FileUtils.resource_path(filePath), 'r')
        for line in f.readlines():
            newLine = int(line)
            if newLine != 0:
                listTime.append(newLine)
        return listTime

    @staticmethod
    def writeDestFile(destSize, pointSize):
        f = open(r'dest.txt', 'w')
        for i in range(pointSize):
            f.write(str(random.randint(0, destSize - 1)) + '\n')

    @staticmethod
    def readDestFile():
        listIndex = []
        filePath = r'dest.txt'
        print(FileUtils.resource_path(filePath))

        f = open(FileUtils.resource_path(filePath), 'r')
        for line in f.readlines():
            newLine = int(line)
            # if newLine != 0:
            listIndex.append(newLine)
        return listIndex

    @staticmethod
    def writeOutCountFile(count):
        f = open(r'out_count_data.txt', 'a+')
        f.write(count)

    @staticmethod
    def writeControlOutCountFile(count):
        f = open(r'control_out_count_data.txt', 'a+')
        f.write(count)

    @staticmethod
    def writeOutFlow(rawList, controlList):
        f = open(r'outFlow.txt', 'a+')
        for x in rawList:
            f.write(str(x) + ',')
        for y in controlList:
            f.write(str(y) + ',')
        f.write('\n')

    @staticmethod
    def writePointSet(rawList, controlList):
        f = open(r'RawPointSet.txt', 'a+')
        for x in rawList:
            f.write('(' + str(x.x) + ',' + str(x.y) + ')')
            f.write(',')
        f.write('\n')
        f = open(r'ControlPointSet.txt', 'a+')
        for y in controlList:
            f.write('(' + str(y.x) + ',' + str(y.y) + ')')
            f.write(',')
        f.write('\n')

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        # base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        # return os.path.join(base_path, relative_path)
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
# FileUtils.writeFile()
# FileUtils.readFile()

# FileUtils.writeDestFile(6, 1000)
