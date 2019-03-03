# -*- coding:utf-8 -*-


class QueueModel:
    userList = []
    destId = 0
    destTime = 0

    def __init__(self, destId, userList, destTime):
        self.destId = destId
        self.userList = userList
        self.destTime = destTime
