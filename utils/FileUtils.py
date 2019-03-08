import common_utils
import random


class FileUtils:
    @staticmethod
    def writeFile():
        f = open('..\data\data.txt', 'w')
        timeList = common_utils.getRandomListByTime(60000, 200)
        for x in range(len(timeList)):
            timeList[x] = str(timeList[x]) + '\n'
        f.writelines(timeList)

    @staticmethod
    def readFile():
        listTime = []
        f = open('data\data.txt', 'r')
        for line in f.readlines():
            newLine = int(line)
            if newLine != 0:
                listTime.append(newLine)
        return listTime

    @staticmethod
    def writeDestFile(destSize, pointSize):
        f = open('..\data\dest.txt', 'w')
        for i in range(pointSize):
            f.write(str(random.randint(0, destSize-1))+'\n')

    @staticmethod
    def readDestFile():
        listIndex = []
        f = open('data\dest.txt', 'r')
        for line in f.readlines():
            newLine = int(line)
            if newLine != 0:
                listIndex.append(newLine)
        return listIndex
# FileUtils.writeFile()
# FileUtils.readFile()

# FileUtils.writeDestFile(6, 200)