import common_utils


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
# FileUtils.writeFile()
# FileUtils.readFile()