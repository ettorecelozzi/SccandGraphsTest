class Node:
    def __init__(self):
        self.color = "white"
        self.parent = None
        self.sons = []
        self.discoveredTime = -1
        self.endTime = -1

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def addSon(self, son):
        self.sons.append(son)

    def setSon(self):
        self.sons = []

    def getSons(self):
        return self.sons

    def setD(self, time):
        self.discoveredTime = time

    def getD(self):
        return self.discoveredTime

    def setEndTime(self, time):
        self.endTime = time

    def getEndTime(self):
        return self.endTime
