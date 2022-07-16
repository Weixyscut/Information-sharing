# 定义智能体类
import tkinter as tk
class agent:
    # 定义智能体的属性
    def __init__(self, identity0, initialPosition0):
        self.identity = identity0                         # 智能体编号
        self.initialPosition = initialPosition0           # 智能体初始出发点
        self.position = initialPosition0                  # 智能体当前位置
        self.rescue = False                               # 智能体获救状态
        self.route = [initialPosition0]                   # 智能体的逃生路径
        self.exsistShared = []                            # 智能体在当前时间节点是否存在共享信息，元素为Boolean

    # 信息共享函数
    def shareInformation(self, position0):
        self.position = position0

    def getIdentity(self):
        return self.identity

    # 获取智能体的当前位置
    def getPosition(self):
        return self.position

    # 设置智能体的当前位置
    def setPosition(self, Position0):
        self.position = Position0
        return 0

    # 获救状态设置函数
    # 输入：获救状态（boolean值）
    def setSituation(self, rescue0):
        self.rescue = rescue0
        return 0

    # 获救状态获取函数
    def getSituation(self):
        return self.rescue

    # 智能体的逃生路径节点
    def addRoutePoint(self, point0):
        self.route.append(point0)
        return 0

    # 获取当前agent的逃生路径
    def getRoute(self):
        return self.route

    # 获取是否存在共享信息
    # 输入：时间节点
    # 输出：对应时间节点下是否存在信息共享
    def getShared(self, time):
        return self.exsistShared[time]

    # 模拟弹窗收集共享信息（用于测试）
    def window_for_getting_information_test(self):
        self.exsistShared.append(0)
        return 0

    # 弹窗收集共享信息
    def window_for_getting_information(self):
        # 定义局部函数
        def shareInformation0():
            self.exsistShared.append(0)
            window.destroy()
            return 0
        def shareInformation1():
            self.exsistShared.append(1)
            window.destroy()
            return 0
        def shareInformation2():
            self.exsistShared.append(2)
            window.destroy()
            return 0
        def shareInformation3():
            self.exsistShared.append(3)
            window.destroy()
            return 0
        window = tk.Tk()
        window.title('Emergency Information Sharing')
        window.geometry('600x440')
        var = 'Agent ' + str(self.identity) + ',If there is any obstacle in your position,\nPLEASE SHARE its information!'
        l = tk.Label(window, text=var, bg='green', font=('Arial', 16), width=50, height=3)
        l.pack()
        b1 = tk.Button(window, text='CLEAR!', font=('Arial', 16), width=50, height=3, command=shareInformation0)
        b1.pack()
        b2 = tk.Button(window, text='PASSABLE obstacle', font=('Arial', 16), width=50, height=3, command=shareInformation1)
        b2.pack()
        b3 = tk.Button(window, text='UNAVAILABLE!', font=('Arial', 16), width=50, height=3, command=shareInformation2)
        b3.pack()
        b4 = tk.Button(window, text='DANGERIOUS!', font=('Arial', 16), width=50, height=3, command=shareInformation3)
        b4.pack()

        window.mainloop()


