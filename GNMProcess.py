# 定义路网相关的操作函数
import Routing
import math

# 定义往路网中添加新的节点的函数
# 输入：所有点的坐标，路网矩阵，新添加的点
# 输出：处理后的点集，处理后的路网矩阵
def matrixAdd(points_name, edges_matrix, point0):
    M_topo = edges_matrix
    M_name = points_name
    M_name.append(point0)
    minimum = float("inf")
    relatedPoint = point0
    for p0 in points_name:
        if float(p0[2]) == float(point0[2]) and p0 != point0:
            dis0 = math.sqrt(pow((point0[0]-p0[0]), 2)+pow((point0[1]-p0[1]), 2))
            if dis0 < minimum:
                minimum = dis0
                relatedPoint = p0
    # 在边的矩阵中添加新的行和列
    for i in range(len(M_topo)):
        M_topo[i].append(float("inf"))
    a0 = []
    for i in range(len(M_topo[0])):
        a0.append(float("inf"))
    M_topo.append(a0)
    # 在指定位置赋值
    relatedPointIndex0 = points_name.index(relatedPoint)
    M_topo[relatedPointIndex0][len(M_topo[0])-1] = minimum
    M_topo[len(M_topo)-1][relatedPointIndex0] = minimum
    return M_name, M_topo

# 定义删除路网中某一特定点的函数
# 输入：所有点的坐标，路网矩阵，新添加的点
# 输出：处理后的点集，处理后的路网矩阵
def matrixMinus(points_name, edges_matrix, point):
    num_deletedPoint = points_name.index(point)
    new_points_name = []
    new_edges_matrix = []
    for i in range(len(points_name)):
        if i != num_deletedPoint:
            new_points_name.append(points_name[i])
    for i in range(len(points_name)):
        line = []
        if i != num_deletedPoint:
            for j in range(len(points_name)):
                if j != num_deletedPoint:
                    line.append(edges_matrix[i][j])
            new_edges_matrix.append(line)
    return new_points_name, new_edges_matrix

# 去除点集和矩阵中重复的点的函数
# 输入：点集、路网矩阵
# 输出：处理后的点集、处理后的路网矩阵
def removeRepeatedPoint(points_name, edges_matrix):
    deleteList = []
    for p0 in points_name:
        for p1 in points_name:
            if p0 == p1 and points_name.index(p0) != points_name.index(p1):
                deleteList.append(p1)
    for p1 in deleteList:
        points_name, edges_matrix = matrixMinus(points_name, edges_matrix, p1)
    return points_name, edges_matrix

# 定义计算新起点的函数
# 输入：间隔时间△t(单位：s)，规划路径的点集，路网点集，路网矩阵
# 输出：新的起点，新的路网点集，新的路网矩阵
def calculateNewStartPoint(routingPoints, GNMPoints, GNMMatrix):
    ds = 3000.0                                         # 假定人在逃生过程中的行走速度为5m/s,ds代表间隔时间内行走的距离
    sumRoute = 0.0
    newStartPoint = routingPoints[1]                                     # 新的起点
    for i in range(len(routingPoints) - 1):
        a0 = int(-1)                                       # 记录前一个点在路网点集中的序号
        b0 = int(-1)                                       # 记录后一个点在路网点集中的序号
        for j in range(len(GNMPoints)):
            if GNMPoints[j] == routingPoints[i]:           # 查询当前节点的坐标
                a0 = j
                break
        for j in range(len(GNMPoints)):
            if GNMPoints[j] == routingPoints[i+1]:         # 查询下一节点的坐标
                b0 = j
                break
        if a0 != int(-1) and b0 != int(-1):
            dis1 = GNMMatrix[a0][b0]                       # 查询得到当前节点与下一节点之间的距离
        else:
            print("error, have no element")
        sumRoute = sumRoute + dis1
        if sumRoute > ds:
            if routingPoints[i + 1] == routingPoints[i]:   # 避免除零错误
                continue
            dd = ds - sumRoute + dis1
            x0 = routingPoints[i + 1][0] - (dis1 - dd) / dis1 * (routingPoints[i + 1][0] - routingPoints[i][0])
            y0 = routingPoints[i + 1][1] - (dis1 - dd) / dis1 * (routingPoints[i + 1][1] - routingPoints[i][1])
            z0 = routingPoints[i + 1][2] - (dis1 - dd) / dis1 * (routingPoints[i + 1][2] - routingPoints[i][2])
            # if math.sqrt(pow((routingPoints[i+1][0]-routingPoints[i][0]), 2)+ pow((routingPoints[i+1][1] - routingPoints[i][1]), 2)
            #              + pow((routingPoints[i+1][2]-routingPoints[i][2]), 2)) != 0:
            weight0 = dis1 / math.sqrt(pow((routingPoints[i + 1][0] - routingPoints[i][0]), 2) + pow((routingPoints[i + 1][1] - routingPoints[i][1]), 2)
                         + pow((routingPoints[i + 1][2] - routingPoints[i][2]), 2))
            # else:
            #     weight0 = 1
            if -100000 < x0 < 100000 and -100000 < y0 < 100000 and -100000 < z0 < 100000:
                newStartPoint = [x0, y0, z0]
            else:
                newStartPoint = routingPoints[1]
                print('little error')
            a101 = 1
            for p0 in GNMPoints:                           # 如果p0已经在路网中，则不添加该点
                if p0 == newStartPoint:
                    a101 = 0
            if a101:                                       # 在原有路网中添加新的起点进去
                GNMPoints.append(newStartPoint)
                for i in range(len(GNMMatrix)):
                    GNMMatrix[i].append(float("inf"))
                c0 = []
                for i in range(len(GNMMatrix[0])):
                    c0.append(float("inf"))
                GNMMatrix.append(c0)
                # 添加上一节点的边长进稀疏矩阵
                d0 = math.sqrt(
                    pow((GNMPoints[a0][0] - x0), 2) + pow((GNMPoints[a0][1] - y0), 2) + pow((GNMPoints[a0][2] - z0), 2))
                GNMMatrix[a0][len(GNMMatrix[0]) - 1] = d0 * weight0
                GNMMatrix[len(GNMMatrix) - 1][a0] = d0 * weight0
                # 添加下一节点的边长进稀疏矩阵
                e0 = math.sqrt(
                    pow((GNMPoints[b0][0] - x0), 2) + pow((GNMPoints[b0][1] - y0), 2) + pow((GNMPoints[b0][2] - z0), 2))
                GNMMatrix[b0][len(GNMMatrix[0]) - 1] = e0 * weight0
                GNMMatrix[len(GNMMatrix) - 1][b0] = e0 * weight0
                # 将上下两个节点之间的连接打断
                GNMMatrix[a0][b0] = float('inf')
                GNMMatrix[b0][a0] = float('inf')
            break
        elif sumRoute == ds:
            newStartPoint = routingPoints[i+1]
            break
    return newStartPoint, GNMPoints, GNMMatrix

# 更新点所在边的长度
# 输入：当前点、路网点集、路网边矩阵、更新权重
# 输出：更新后的路网边矩阵
def updateMatrixBySharedInformation(currentPoint, points, edgesMatrix, weight):
    for p0 in points:
        if currentPoint == p0:
            index0 = int(points.index(p0))
            if weight == 0:    # 当前节点清晰，可以通行
                for i in range(len(edgesMatrix)):
                    edgesMatrix[index0][i] = edgesMatrix[index0][i] * 1
                    edgesMatrix[i][index0] = edgesMatrix[i][index0] * 1
            elif weight == 1:  # 当前节点存在障碍物，影响通行
                for i in range(len(edgesMatrix)):
                    edgesMatrix[index0][i] = edgesMatrix[index0][i] * 1.5
                    edgesMatrix[i][index0] = edgesMatrix[i][index0] * 1.5
            elif weight == 2:  # 当前节点堵塞，不能通行
                for p0 in points:
                    if currentPoint[0] - 2000 < p0[0] < currentPoint[0] + 2000 and currentPoint[1] - 2000 < p0[1] < currentPoint[1] + 2000 and currentPoint[2] - 500 < p0[2] < currentPoint[2] + 500:
                        points, edgesMatrix = matrixMinus(points, edgesMatrix, p0)
            elif weight == 3:  # 当前节点危险，不能通行
                for p0 in points:
                    if currentPoint[0] - 2000 < p0[0] < currentPoint[0] + 2000 and currentPoint[1] - 2000 < p0[1] < \
                            currentPoint[1] + 2000 and currentPoint[2] - 2000 < p0[2] < currentPoint[2] + 2000:
                        points, edgesMatrix = matrixMinus(points, edgesMatrix, p0)
            else:
                print('error! something wrong with shared information!')
    return points, edgesMatrix



























