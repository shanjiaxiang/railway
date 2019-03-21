import common_utils
import random


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
        f = open(r'data\data.txt', 'r')
        for line in f.readlines():
            newLine = int(line)
            if newLine != 0:
                listTime.append(newLine)
        return listTime

    @staticmethod
    def writeDestFile(destSize, pointSize):
        f = open(r'..\data\dest.txt', 'w')
        for i in range(pointSize):
            f.write(str(random.randint(0, destSize-1))+'\n')

    @staticmethod
    def readDestFile():
        listIndex = []
        f = open(r'data\dest.txt', 'r')
        for line in f.readlines():
            newLine = int(line)
            if newLine != 0:
                listIndex.append(newLine)
        return listIndex

    @staticmethod
    def writeOutCountFile( count):
        f = open(r'data.txt', 'a+')
        f.write(count)

    @staticmethod
    def writeControlOutCountFile(count):
        f = open(r'data1.txt', 'a+')
        f.write(count)

# FileUtils.writeFile()
# FileUtils.readFile()

# FileUtils.writeDestFile(6, 1000)