# 火灾烟气蔓延模拟模块
import math

weight_of_danger = 2  # 火灾对路径长度的影响系数

# 定义计算初始火灾层楼梯间节点是否开始蔓延
# 输入：火灾起点，楼梯间节点
# 输出：是否已蔓延至楼梯间
def originalFiretoCorridor(startPoint, points1, radius):
    b0 = False
    for p0 in points1:
        dis0 = math.sqrt(pow((startPoint[0] - p0[0]), 2) + pow((startPoint[1] - p0[1]), 2))
        if dis0 < radius:
            b0 = True
    return b0

# 定义初始层火灾烟气蔓延的边更新函数
# 输入：火灾起点，火灾蔓延半径，楼梯节点，节点列表，边的矩阵，已经更新过的点
# 输出：更新后的边的矩阵，已经更新过的点
def updateThisFloor(startPoint, floor, radius, pointsList, edgesMatrix, updatedPoints):
    points_in_this_floor = []
    updatedPoints0 = updatedPoints
    for p0 in pointsList:
        if ((floor - 1) * 2900 <= p0[2] < floor * 2900) and (p0 not in updatedPoints0):
            points_in_this_floor.append(p0)
    for p0 in points_in_this_floor:
        dis0 = math.sqrt(pow((startPoint[0] - p0[0]), 2) + pow((startPoint[1] - p0[1]), 2))
        index0 = int(pointsList.index(p0))
        if dis0 < radius:
            updatedPoints0.append(p0)
            for i in range(len(pointsList)):
                if edgesMatrix[index0][i] != float("inf") and (pointsList[i] not in updatedPoints0):
                    updatedPoints0.append(pointsList[i])
                    edgesMatrix[index0][i] = edgesMatrix[index0][i] * weight_of_danger
                    edgesMatrix[i][index0] = edgesMatrix[i][index0] * weight_of_danger
    return edgesMatrix, updatedPoints0

# 定义其他层火灾烟气蔓延的边更新函数
# 输入：火灾起点，火灾蔓延半径，楼梯节点，节点列表，边的矩阵，已经更新过的点
# 输出：更新后的边的矩阵，已经更新过的点
def updateOtherFloor(startPoint, radius, floor, corridorPoints, pointsList, edgesMatrix, updatedPoints):
    points_in_this_floor = []
    updatedPoints0 = updatedPoints
    for p0 in pointsList:
        if (p0 not in corridorPoints) and (p0 not in updatedPoints0) and ((floor - 1) * 2900 <= p0[2] < floor * 2900):
            points_in_this_floor.append(p0)
    for p0 in points_in_this_floor:
        dis0 = math.sqrt(pow((startPoint[0] - p0[0]), 2) + pow((startPoint[1] - p0[1]), 2))
        index0 = int(pointsList.index(p0))
        if dis0 < radius:
            updatedPoints0.append(p0)
            for i in range(len(pointsList)):
                if edgesMatrix[index0][i] != float("inf") and (pointsList[i] not in updatedPoints0):
                    updatedPoints0.append(pointsList[i])
                    edgesMatrix[index0][i] = edgesMatrix[index0][i] * weight_of_danger
                    edgesMatrix[i][index0] = edgesMatrix[i][index0] * weight_of_danger
    return edgesMatrix, updatedPoints0

# 定义楼梯间节点的边更新函数
# 输入：初始蔓延楼层，蔓延持续时间，楼梯间点集，全局点集，全局边稀疏矩阵，已经更新过的点
# 输出：更新后的边稀疏矩阵，已经更新过的点
def updateCorridor(startFloor, spreadTime, corridorPoints, pointsList, edgesMatrix, updatedPoints):
    corridorPointsUpdated = []
    updatedPoints0 = updatedPoints
    for p0 in corridorPoints:
        if p0 not in updatedPoints0:
            corridorPointsUpdated.append(p0)
    for p0 in corridorPointsUpdated:
        dis0 = p0[2] - (startFloor - 1) * 2900  # 计算楼梯间节点与起火楼层的距离
        index0 = int(pointsList.index(p0))
        if dis0 < 0:  # 当前楼梯间节点低于火灾初始楼层节点（蔓延速度为1m/s）
            if dis0 < spreadTime * 800:
                updatedPoints0.append(p0)
                for i in range(len(pointsList)):
                    if edgesMatrix[index0][i] != float("inf") and (pointsList[i] not in updatedPoints0):
                        updatedPoints0.append(pointsList[i])
                        edgesMatrix[index0][i] = edgesMatrix[index0][i] * weight_of_danger
                        edgesMatrix[i][index0] = edgesMatrix[i][index0] * weight_of_danger
        elif dis0 >= 2900:
            if dis0 < spreadTime * 1500:
                updatedPoints0.append(p0)
                for i in range(len(pointsList)):
                    if edgesMatrix[index0][i] != float("inf") and (pointsList[i] not in updatedPoints0):
                        updatedPoints0.append(pointsList[i])
                        edgesMatrix[index0][i] = edgesMatrix[index0][i] * weight_of_danger
                        edgesMatrix[i][index0] = edgesMatrix[i][index0] * weight_of_danger
    return edgesMatrix, updatedPoints0
