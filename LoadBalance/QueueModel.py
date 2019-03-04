# -*- coding:utf-8 -*-


class QueueModel:
    userList = []
    destId = 0
    endTime = 0
    startTime = 0
    pointDensity = 0


    def __init__(self, destId, userList):
        self.destId = destId
        self.userList = userList

    def calculate(self):
        minTime = self.userList[0].destTime
        maxTime = self.userList[0].destTime
        for user in self.userList:
            if user.destTime < minTime:
                minTime = user.destTime
            if user.destTime > maxTime:
                maxTime = user.destTime
        self.startTime = minTime
        self.endTime = maxTime
        # 理论上列表需要这么久清空
        time = len(self.userList)*3000 + self.startTime
        if time > self.endTime:
            self.endTime = time
        self.pointDensity = int((self.endTime - self.startTime)/len(self.userList))
        print("当前队列信息如下：")
        print("Dest id:", self.destId)
        print("User list size:", len(self.userList))
        print("queue start time:", self.startTime)
        print("queue end time:", self.endTime)
        print("queue density:", self.pointDensity)
