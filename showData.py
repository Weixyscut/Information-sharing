import numpy as py
import os
import matplotlib.pyplot as plt

# 三维展示图的代码
def showRescueRoute(Shortest_path):
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    lt1 = []
    lt2 = []
    lt3 = []
    for i in range(len(Shortest_path)):
        xd = Shortest_path[i][0]
        yd = Shortest_path[i][1]
        zd = Shortest_path[i][2]
        lt1.append(xd)
        lt2.append(yd)
        lt3.append(zd)
    ax1.plot(lt1, lt2, lt3, c='blue', marker='o')
    plt.show()

# 展示点的代码
# fileList = os.listdir("D:\eclipse\obstacles_ConvexHull")
# for file0 in fileList:
#     file2 = open("D:\eclipse\obstacles_ConvexHull"+"\\"+file0, 'r')
#     j = 0
#     pointList = []        #记录输入的点
#     x0 = 0
#     y0 = 0
#     z0 = 0
#     row0 = file2.readlines()
#     for line in row0:
#         line = line.strip('\n')
#         temp_line = line
#         pointList.append(temp_line)
#     updatedListAddLen = int((len(pointList)-3)*1.5)
#     updatedList = [0]*(len(pointList)-3)  #记录更新后的点
#     updatedListAdd = [0]*updatedListAddLen
#     for i in range(0,len(pointList)):
#         if i == 0:
#             x0 = pointList[i]
#         elif i == 1:
#             y0 = pointList[i]
#         elif i == 2:
#             z0 = pointList[i]
#         elif i%2 == 1:
#             updatedList[i-3] = 100*float(pointList[i])+float(x0)
#         elif i%2 == 0:
#             updatedList[i-3] = 100*float(pointList[i])+float(y0)
#         else:
#             print("error")
#     file1 = open("D:\eclipse\obstacles"+"\\"+file0, mode='x')
#     for i in range(0,updatedListAddLen):
#         if (i+1)%3 != 0:
#             updatedListAdd[i] = updatedList[int((i+1)/1.5)]
#         elif (i+1)%3 == 0:
#             updatedListAdd[i] = (int(z0)-1)*2900
#         else:
#             print("error")
#     for cor0 in updatedListAdd:
#         file1.write(str(cor0)+"\n")
#     file1.write("1000000000" + "\n")
#     file1.write("底面积与区域比值 临界值0.5" + "\n")
#     file1.write("宽敞区域 1宽敞 0狭窄" + "\n")
#     file1.write("危险性 1危险 0安全" + "\n")
#     file1.write("高度 低<200 中<1000" + "\n")
#     file1.write("纹理 0不可拆 1可拆" + "\n")
#     file1.write("重量 0不可搬 1可搬" + "\n")
#     file1.write(str((float(z0)-1)*2900))
#     file1.close()

