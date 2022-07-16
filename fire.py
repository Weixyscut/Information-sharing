# 火灾类，用于表示每一层的火灾发展情况
class fire:
    # 定义一个新的火灾开始
    # 输入：着火楼层
    def __init__(self, fireFloor1):
        self.startPoint0 = []                                              # 当前层火灾烟气开始蔓延的起点坐标
        self.startTime0 = float("inf")                                     # 当前层火灾烟气蔓延开始时间
        self.fireFloor = fireFloor1                                        # 火灾所在楼层
        self.sumTime0 = 0                                                  # 当前层火灾烟气蔓延持续时间
        self.radius0 = 0                                                   # 当前火灾蔓延半径
        self.corridorPoint = []                                            # 当前层的楼梯间节点
        self.fireSituation = False                                         # 当前层是否开始火灾蔓延

    # 获取火灾所在楼层
    def getFloor(self):
        return self.fireFloor

    # 添加当前层的楼梯节点
    def addCorridorPoint(self, point1):
        self.corridorPoint.append(point1)
        return 0

    # 设置火灾开始蔓延(True)
    def setFireSituation(self):
        self.fireSituation = True
        return 0

    # 判断当前楼层是否开始火灾蔓延
    def getFireSituation(self):
        return self.fireSituation

    # 获取当前楼层的火灾蔓延起点
    def getFireStartPoint(self):
        return self.startPoint0

    # 设置当前楼层火灾起点
    def setStartPoint(self, point1):
        self.startPoint0 = point1
        return 0

    # 设置当前楼层火灾开始时间
    def setStartTime(self, time1):
        self.startTime0 = time1
        return 0

    # 获取当前楼层火灾开始时间
    def getStartTime(self):
        return self.startTime0