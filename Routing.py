#utf-8
from collections import defaultdict
from heapq import *

# 寻路模块主函数
# 输入：起始点，路网点集，路网边的稀疏矩阵
# 输出：当前导航路径长度，导航路径中的所有节点
def routing(start_point, points_name, edges_matrix):
    # 输入二：逃生现场的两个终点坐标
    end_point0 = [-9232.727229765405, -22447.4507748233, 0.0]
    end_point1 = [-4882.62602160798, -22497.4507748229, 0.0]
    # 将稀疏矩阵中地关系转化为（点，点，距离）的形式储存
    list_nodes_id = points_name
    M_topo = edges_matrix
    M = float("inf")
    edges = []
    for i in range(len(M_topo)):
        for j in range(len(M_topo[0])):
            if i != j and M_topo[i][j] != M:
                edges.append((i, j, M_topo[i][j]))
    # dijkstra函数：
    # 输入：点的坐标，边的矩阵（转化后），起点（包含在路网中），终点（包含在路网中）
    # 输出：疏散路径长度，疏散路径点坐标
    for i in range(len(points_name)):
        if start_point == points_name[i]:
            a = i
    for i in range(len(points_name)):
        if end_point0 == points_name[i]:
            b = i
    for i in range(len(points_name)):
        if end_point1 == points_name[i]:
            c = i
    length0, Shortest_path0 = dijkstra(points_name, edges, a, b)  # 起点与终点0的最短路
    length1, Shortest_path1 = dijkstra(points_name, edges, a, c)  # 起点与终点1的最短路
    if length0 < length1:
        length = length0
        Shortest_path = Shortest_path0
    else:
        length = length1
        Shortest_path = Shortest_path1
    return length, Shortest_path

# *******************************分界线**************************
def findindex(points, i):
    return points[i]

def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost,path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf"), []

def dijkstra(points, edges, from_node, to_node):
    len_shortest_path = -1
    ret_path=[]
    length,path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue)>0:
        len_shortest_path = length    # 1.Get the length firstly;
        # 2.Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        a = findindex(points,left)
        b = [0,0,0]
        b[0] = float(a[0])
        b[1] = float(a[1])
        b[2] = float(a[2])
        ret_path.append(b)           # 2.1Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            a1 = findindex(points,left)
            b1 = [0, 0, 0]
            b1[0] = float(a1[0])
            b1[1] = float(a1[1])
            b1[2] = float(a1[2])
            ret_path.append(b1)     # 2.2Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()          # 3.Reverse the list finally, to make it be normal sequence.
    return len_shortest_path, ret_path