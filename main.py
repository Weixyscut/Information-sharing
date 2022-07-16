# coding=utf-8
import agent
import Routing
from matplotlib import pyplot as plt
import GNMProcess
import showData
import fire
import fireSimulator

# 主要的输入
# 输入一：路网文件
a = ""      #定义采用哪一层分类网络进行寻路
file = open("D:\\eclipse\\Grid Generation and IFC Extraction"+a+"\\src\\io\\new_Points1.txt", "r")   #读取路网的节点坐标
row0 = file.readlines()
points_name = []
for line in row0:
    line = list(line.strip().split(','))
    s = []
    for i in line:
        s.append(float(i))
    points_name.append(s)            # 点坐标作为点的name储存
file = open("D:\\eclipse\\Grid Generation and IFC Extraction"+a+"\\src\\io\\new_Edges1.txt", "r")    #读取路网的边长
row1 = file.readlines()
edges_matrix = []
for line in row1:
    line = list(line.strip().split(' '))
    s = []
    for i in line:
        s.append(float(i))
    edges_matrix.append(s)                                            # 边长作为稀疏矩阵储存

# *************************************************************主程序***************************************************************************
timeCalculater = 0                                                    # 计时器
all_rescue_num = 0                                                    # 逃生人员数量
ds = 1 * 3000.0                                                         # 假定人在逃生过程中的行走速度为5m/s,ds代表间隔时间内行走的距离
agentsGroup = []                                                      # 智能体集合（群）
agentsGroup_rescued = []                                              # 智能体获救后信息储存
agent0 = agent.agent(0, [-2458, -4371, 8700.0])                    # 不在路网上的智能体
agent1 = agent.agent(1, [-2458, -4371, 29000.0])                    # 在路网上的智能体
# agent2 = agent.agent(2, [2800.0, -5000.0, 14500.0])
agentsGroup.append(agent0)
agentsGroup.append(agent1)
# agentsGroup.append(agent2)
agents_num = len(agentsGroup)
# 初步处理，遍历所有agent，修改当前路网获取能用于导航的路网
for agentn in agentsGroup:
    m = False
    for p0 in points_name:
        if agentn.getPosition() == p0:                                # 如果当前位置在路网上，则m为TRUE，不需要添加点
            m = True
    if not m:
        points_name, edges_matrix = GNMProcess.matrixAdd(points_name, edges_matrix, agentn.getPosition())
# **************************************火灾参数模块*********************************开头****************************************************
# updatedPoints = []                                                    # 已经通过火灾蔓延模块更新过的点
# corridorPoints0 = []                                                  # 模型中的楼梯0的节点
# corridorPoints1 = []                                                  # 模型中的楼梯1的节点
# for p0 in points_name:
#     if -14157.7 < p0[0] <= -7757.7 and -3347.5 <= p0[1] < -447.5:    # 楼梯0的范围
#         corridorPoints0.append(p0)
#     if -6457.7 < p0[0] <= -307.7 and -3347.5 <= p0[1] < -447.5:      # 楼梯1的范围
#         corridorPoints1.append(p0)
# # 火灾开始，获取起火点坐标
# originalFireStartPoint = [-18156.3, -4154.5, 0]
# originalFire = fire.fire(originalFireStartPoint[2] / 2900 + 1)        # 火灾开始蔓延
# originalFire.setStartTime(0)
# originalFire.setStartPoint(originalFireStartPoint)
# # 分层储存火灾发展情况
# fireGroup = []                                                        # 火灾集合（一共17层）
# for i in range(17):
#     fireGroup.append(fire.fire(i+1))
# fireGroup[int(originalFire.getFloor()) - 1] = originalFire                # 储存原始火灾
# originalFireFloor = originalFire.getFloor()                           # 初始着火楼层
# fireGroup_down = []                                                   # 初始楼层以下的火灾
# fireGroup_up = []                                                     # 初始楼层以上的火灾
# for fire0 in fireGroup:
#     if fire0.getFloor() < originalFireFloor:
#         fireGroup_down.append(fire0)
#     if fire0.getFloor() > originalFireFloor:
#         fireGroup_up.append(fire0)
# originalFireFloorCorridorPoints0 = []                                 # 初始着火楼层楼梯间0的节点
# originalFireFloorCorridorPoints1 = []                                 # 初始着火楼层楼梯间1的节点
# for p0 in corridorPoints0:
#     if (originalFireFloor - 1) * 2900 <= p0[2] < originalFireFloor * 2900:
#         originalFireFloorCorridorPoints0.append(p0)
# for p0 in corridorPoints1:
#     if (originalFireFloor - 1) * 2900 <= p0[2] < originalFireFloor * 2900:
#         originalFireFloorCorridorPoints1.append(p0)
# # 预先计算各火灾节点的临界时间阈值
# t0 = float("inf")                                                      # 火灾蔓延至初始楼层楼梯0的时间
# t1 = float("inf")                                                      # 火灾蔓延至初始楼层楼梯1的时间
# for t in range(36000):                                                 # 火灾蔓延至初始楼层楼梯
#     if fireSimulator.originalFiretoCorridor(originalFire.getFireStartPoint(), originalFireFloorCorridorPoints0, 800 * t):
#         t0 = t
#         break
# for t in range(36000):  # 火灾蔓延至初始楼层楼梯
#     if fireSimulator.originalFiretoCorridor(originalFire.getFireStartPoint(), originalFireFloorCorridorPoints1, 800 * t):
#         t1 = t
#         break
# # 判断先进行火灾蔓延的楼梯
# corridor_in_fire = 0                                                   # 如果t0更小，则楼梯0先进行火灾蔓延
# eachFloorStartTime0 = t0                                               # 设置楼梯间开始蔓延时间为t0
# if t1 < t0:
#     corridor_in_fire = 1                                               # 如果t1更小，则楼梯1先进行火灾蔓延
#     eachFloorStartTime0 = t1                                           # 设置楼梯间开始蔓延时间为t1
# for fire0 in fireGroup:                                                # 火灾在楼梯中蔓延，遍历每个fire对象
#     dis_floor = fire0.getFloor() - originalFireFloor                   # 记录当前楼层与火灾初始楼层的距离
#     if dis_floor < 0:
#         if t1 < t0:
#             eachFloorStartPoint3D = [-3382.7, -1897.5, (fire0.getFloor() - 1) * 2900]         # 设置楼梯0的中心点二维坐标为开始蔓延的节点
#         else:
#             eachFloorStartPoint3D = [-12557.7, -1897.5, (fire0.getFloor() - 1) * 2900]        # 设置楼梯1的中心点二维坐标为开始蔓延的节点
#         eachFloorStartTime = eachFloorStartTime0 + abs(int((originalFireFloor - fire0.getFloor()) * 2900 / 800))         # 火灾在初始起火点楼层之下蔓延，速度1m/s
#     elif dis_floor > 0:
#         if t1 < t0:
#             eachFloorStartPoint3D = [-3382.7, -1897.5, (fire0.getFloor() - 1) * 2900]
#         else:
#             eachFloorStartPoint3D = [-12557.7, -1897.5, (fire0.getFloor() - 1) * 2900]
#         eachFloorStartTime = eachFloorStartTime0 + abs(int((originalFireFloor - fire0.getFloor()) * 2900 / 1500))         # 火灾在初始起火点楼层之上蔓延，速度1.5m/s
#     else:
#         continue
#     fire0.setStartPoint(eachFloorStartPoint3D)
#     fire0.setStartTime(eachFloorStartTime)
# *******************************************火灾参数模块******************************结尾****************************************************
# 进入时间序列遍历，获取路径
for t in range(36000):                                                # 时间跨度定为10h
    print("current rescue time:" + str(timeCalculater) + " s")        # 打印当前时间
    # 根据风险蔓延模型调整路网中的路径长度
    # edges_matrix, updatedPoints = fireSimulator.updateThisFloor(originalFire.getFireStartPoint(), originalFireFloor, 800 * t, points_name, edges_matrix, updatedPoints)            # 更新火灾当前层的节点边长
    # if t >= t0:
    #     edges_matrix, updatedPoints = fireSimulator.updateCorridor(originalFireFloor, (t - t0), corridorPoints0, points_name, edges_matrix, updatedPoints)       # 更新楼梯间0的节点边长
    # if t >= t1:
    #     edges_matrix, updatedPoints = fireSimulator.updateCorridor(originalFireFloor, (t - t1), corridorPoints1, points_name, edges_matrix, updatedPoints)       # 更新楼梯间1的节点边长
    # for fire0 in fireGroup:
    #     if fire0.getFloor() != originalFireFloor:                                     # 遍历除了初始楼层的其它层火灾对象
    #         if t > fire0.getStartTime():
    #             edges_matrix, updatedPoints = fireSimulator.updateOtherFloor(fire0.getFireStartPoint(), (t - fire0.getStartTime()) * 800, fire0.getFloor(), corridorPoints0 + corridorPoints1, points_name, edges_matrix, updatedPoints)
    # 遍历agent，进行寻路
    for agentn in agentsGroup:
        if not agentn.getSituation():
            a1 = ''
            if -14157.7 < agentn.getPosition()[0] <= -7757.7 and -3347.5 <= agentn.getPosition()[1] < -447.5:
                a1 = 'left'
            elif -6457.7 < agentn.getPosition()[0] <= -307.7 and -3347.5 <= agentn.getPosition()[1] < -447.5:
                a1 = 'right'
            print("agent"+str(agentn.getIdentity())+"的当前位置：["+str(int(agentn.getPosition()[0]))+', '+str(int(agentn.getPosition()[1]))+', '+str(int(agentn.getPosition()[2]))+']'+a1)
            agentn.window_for_getting_information()                    # 遍历所有agent，使其汇报当前节点是否存在需共享的信息
            length0, route0 = Routing.routing(agentn.getPosition(), points_name, edges_matrix)
            # if agentn.getPosition()[2] < 2000:
            #     print(route0)
            # 先判断agent是否即将逃脱
            if length0 <= ds:
                for i in range(len(route0)):
                    if i != 0:
                        agentn.addRoutePoint(route0[i])                # 添加逃生路径节点
                print("agent"+str(agentn.getIdentity())+"顺利疏散，疏散总用时约："+str(timeCalculater+1)+"s")
                # showData.showRescueRoute(agentn.getRoute())
                agentn.setSituation(True)
            else:
                StartPoint0, points_name, edges_matrix = GNMProcess.calculateNewStartPoint(route0, points_name, edges_matrix)
                # updatedPoints.append(StartPoint0)                    # 考虑风险蔓延模型时需要用到
                sharedSituation = agentn.getShared(t)  # 根据agent的信息共享情况调整路网中的路径长度
                points_name, edges_matrix = GNMProcess.updateMatrixBySharedInformation(agentn.getPosition(), points_name, edges_matrix, sharedSituation)
                points_name, edges_matrix = GNMProcess.removeRepeatedPoint(points_name, edges_matrix)
                if agentn.getShared(t) == 2 or agentn.getShared(t) == 3:
                    StartPoint0 = agentn.getRoute()[-2]
                    agentn.setPosition(StartPoint0)
                    agentn.addRoutePoint(StartPoint0)
                else:
                    agentn.setPosition(StartPoint0)
                    agentn.addRoutePoint(StartPoint0)                  # 添加逃生路径节点
    timeCalculater = timeCalculater + 1                                # 间隔时间为1s，计时器加1s
    # 判断是否所有agent逃生成功
    for agentn in agentsGroup:
        if agentn.getSituation():
            all_rescue_num = all_rescue_num + 1
            agentsGroup_rescued.append(agentn)
            agentsGroup.remove(agentn)
    if all_rescue_num == agents_num:
        break
# 跳出循环，输出逃生路径
for agentn in agentsGroup_rescued:
    showData.showRescueRoute(agentn.getRoute())
    # print("agent"+str(agentn.getIdentity())+"的逃生路径："+str(agentn.getRoute()))
print("total rescue time:"+str(timeCalculater)+"s")
print("MISSION ACCOMPLISHED!")