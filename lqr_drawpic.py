# from lqr_ui import Ui_MainWindow
from lqr_ui3 import Ui_Dialog
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from file_operation import get_locationData
import math

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，
                                     # 这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None, width=11, height=8, dpi=80):  # dpi=80管放大缩小
        fig = Figure(figsize=(width, height), dpi=dpi)   # 创建一个Figure，注意：该Figure为matplotlib下的figure，
                                                         # 不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.axes.margins(0.05)  # 0.05是正常值
        #self.axes.margins(2, 2)


    def test(self):
        """
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        """
        list_buildings, list_basestation = get_locationData()
        # 处理数据，减去最小值得到相对最小值的数值
        x_min_temp = 0
        # 初值设定大一些，否则会在第一次就错了
        x_min_last = 10000000
        y_min_temp = 0
        y_min_last = 10000000
        # 归一化
        for i in range(len(list_buildings)):
            x_min_temp, y_min_temp = np.min(list_buildings[i], axis=0)
            if x_min_last > x_min_temp:
                x_min_last = x_min_temp
            if y_min_last > y_min_temp:
                y_min_last = y_min_temp

        for i in range(len(list_buildings)):
            # 每栋楼的顶点数
            point = len(list_buildings[i])
            # 连线, 边数=顶点数-1
            location_x = []
            location_y = []
            for j in range(point):
                location_x.append(list_buildings[i][j][0]-x_min_last)
                location_y.append(list_buildings[i][j][1]-y_min_last)
            self.axes.plot(location_x, location_y, color='b')

            #self.plot(location_x, location_y, color='r')

            # 标点
            #plt.scatter(list_buildings[i][j][0], list_buildings[i][j][1], color='b')

        for i in range(len(list_basestation)):
            location_x = list_basestation[i]['x']-x_min_last
            location_y = list_basestation[i]['y']-y_min_last
            self.axes.scatter(location_x, location_y, color='r')
    def zoomout(self):
        self.axes.margins(2, 2)
    def zoomin(self):
        # zoomin to center
        self.axes.margins(-0.4, 0.0)

    def rsrp(self):
        list_buildings, list_basestation = get_locationData()
        # 处理数据，减去最小值得到相对最小值的数值
        x_min_temp = 0
        # 初值设定大一些，否则会在第一次就错了
        x_min_last = 10000000
        y_min_temp = 0
        y_min_last = 10000000
        # 归一化
        for i in range(len(list_buildings)):
            x_min_temp, y_min_temp = np.min(list_buildings[i], axis=0)
            if x_min_last > x_min_temp:
                x_min_last = x_min_temp
            if y_min_last > y_min_temp:
                y_min_last = y_min_temp

        for i in range(len(list_buildings)):
            # 每栋楼的顶点数
            point = len(list_buildings[i])
            # 连线, 边数=顶点数-1
            location_x = []
            location_y = []
            for j in range(point):
                location_x.append(list_buildings[i][j][0] - x_min_last)
                location_y.append(list_buildings[i][j][1] - y_min_last)
            self.axes.plot(location_x, location_y, color='b')

            # self.plot(location_x, location_y, color='r')

            # 标点
            # plt.scatter(list_buildings[i][j][0], list_buildings[i][j][1], color='b')

        for i in range(len(list_basestation)):
            location_x = list_basestation[i]['x'] - x_min_last
            location_y = list_basestation[i]['y'] - y_min_last
            self.axes.scatter(location_x, location_y, color='r')
        # rsrp判断阈值
        rsrp_thr = -110
        # 工作频率，MHz为单位
        freq = 2.5e+3
        cc = ['r', 'g', 'b', 'm', 'y', 'c']
        for i in range(len(list_basestation)):
            # rsrp_distance_thr是当前循环计算的基站的覆盖范围内能完整接收信号的最小信号功率处距离基站的距离
            # 单位是KM，画图的时候要转换为图上的单位
            rsrp_distance_thr = 10 ** ((-rsrp_thr+list_basestation[i]['power']-46.3-33.9*math.log10(freq)\
            +13.82*math.log10(list_basestation[i]['height'])-3)/(44.9-6.55*math.log10(list_basestation[i]['height'])))
            # 以rsrp_distance_thr为半径画圆
            rsrp_distance_thr = rsrp_distance_thr*1e+3
            location_x = list_basestation[i]['x'] - x_min_last
            location_y = list_basestation[i]['y'] - y_min_last
            #self.axes.scatter(location_x, location_y, color='b')
            theta = np.linspace(0, 2*np.pi, 800)
            x, y = location_x+np.cos(theta)*rsrp_distance_thr, location_y+np.sin(theta)*rsrp_distance_thr
            color = np.random.randint(len(cc))
            self.axes.plot(x, y, color=cc[color], linewidth='1.0')
            # self.axes.circle(x, y, rsrp_distance_thr, cc[rsrp_distance_thr % len(cc)])
            """
            self.axes.scatter(location_x, location_y,
                              s=rsrp_distance_thr, color='g', edgecolor='y')
            

            v = np.linspace(0,1,100)
            v.shape = (100, 1)
            x1 = v * x
            y1 = v * y
            self.axes.plot(x1, y1, color='green', linewidth='1.0')
"""
    def Max_rate(self):
        list_buildings, list_basestation = get_locationData()
        # 处理数据，减去最小值得到相对最小值的数值
        x_min_temp = 0
        # 初值设定大一些，否则会在第一次就错了
        x_min_last = 10000000
        y_min_temp = 0
        y_min_last = 10000000
        # 归一化
        for i in range(len(list_buildings)):
            x_min_temp, y_min_temp = np.min(list_buildings[i], axis=0)
            if x_min_last > x_min_temp:
                x_min_last = x_min_temp
            if y_min_last > y_min_temp:
                y_min_last = y_min_temp
        x_max_last = 6000
        y_max_last = 3500
        # 对整个图片划分成小的栅格,max_rate_slot_x为小格子间隔
        total_slot = 20
        max_rate_slot_x = (x_max_last - 0) / total_slot
        max_rate_slot_y = (y_max_last - 0) / total_slot
        total_slotboxNum = total_slot * total_slot
        for i in range(len(list_buildings)):
            # 每栋楼的顶点数
            point = len(list_buildings[i])
            # 连线, 边数=顶点数-1
            location_x = []
            location_y = []
            for j in range(point):
                location_x.append(list_buildings[i][j][0] - x_min_last)
                location_y.append(list_buildings[i][j][1] - y_min_last)
            self.axes.plot(location_x, location_y, color='m')

            # self.plot(location_x, location_y, color='r')

            # 标点
            # plt.scatter(list_buildings[i][j][0], list_buildings[i][j][1], color='b')

        for i in range(len(list_basestation)):
            location_x = list_basestation[i]['x'] - x_min_last
            location_y = list_basestation[i]['y'] - y_min_last
            self.axes.scatter(location_x, location_y, color='b')
        # 系统带宽，单位：Hz
        band = 15000
        # 单位带宽的噪声功率，dBm/Hz
        N0 = -174
        # 计算总噪声功率(5E-14),单位：mW
        noise = (10 ** (N0 / 10)) * band
        # 工作频率，MHz为单位
        freq = 2.5e+3

        dataRate = np.zeros((total_slot, total_slot))

        dataRate_PerBS = []
        location_x = 0
        location_y = 0
        for i in range(total_slot):
            location_x = location_x + max_rate_slot_x
            for j in range(total_slot):
                location_y = location_y + max_rate_slot_y
                rsrp_temp = []
                # rsrp_temp单位是dBm,转换为毫瓦，用于计算信干噪比
                rsrt_temp_mW = []
                for k in range(len(list_basestation)):
                    Basestation_location_x = list_basestation[k]['x'] - x_min_last
                    Basestation_location_y = list_basestation[k]['y'] - y_min_last
                    #distance_temp = np.sqrt((Basestation_location_x-location_x) ** 2, (Basestation_location_y-location_y) ** 2)
                    distance_temp = math.sqrt((Basestation_location_x - location_x) ** 2 + (Basestation_location_y - location_y) ** 2)
                    # 单位是公里
                    distance_temp = distance_temp / 1e+3
                    # rsrp_temp 每个基站到当前坐标点的信号功率（经过衰减的）
                    rsrp_temp.append((list_basestation[k]['power'] - (46.3 + 33.9 * math.log10(freq)
                                                    - 13.82 * math.log10(list_basestation[k]['height']) +
                                                    (44.9-6.55*math.log10(list_basestation[k]['height'])) * math.log10(distance_temp)
                                                    + 3)))
                    rsrt_temp_mW.append(10 ** (rsrp_temp[k] / 10))

                # 每个基站在一个点的速率,每个坐标的时候要重新定义，赋值
                dataRate_PerBS = []
                # 计算一个基站的速率时，其他基站的功率是干扰;因此其他基站的功率要已经求出来，第一次遍历基站的时候算所有的功率，第二次遍历基站算每个基站的速率
                for t in range(len(list_basestation)):
                    if t==0:
                        # K=0会造成K-1<0,索引出错，因此单独计算k==0
                        dataRate_PerBS.append(band * math.log2(1+(rsrt_temp_mW[t] / (
                                    sum(rsrt_temp_mW[t + 1:len(list_basestation) - 1]) + noise))))
                    else:
                        dataRate_PerBS.append(band * math.log2(1+(rsrt_temp_mW[t]/(sum(rsrt_temp_mW[0:t-1])+sum(rsrt_temp_mW[t+1:len(list_basestation)-1])+noise))))

                # dataRate = np.zeros((total_slot, total_slot))
                dataRate[i, j] = sum(dataRate_PerBS)
                x_box = [location_x - max_rate_slot_x, location_x + max_rate_slot_x, location_x + max_rate_slot_x,
                         location_x - max_rate_slot_x]
                y_box = [location_y - max_rate_slot_y, location_y - max_rate_slot_y, location_y + max_rate_slot_y,
                         location_y + max_rate_slot_y]
                #self.axes.plot(x_box, y_box)

                # color_temp = '#008000'颜色应该具有的形式
                color_temp = int(dataRate[i, j] / 90)
                color_temp = str(hex(color_temp))[2:]
                if len(color_temp) == 2:
                    color_temp = '00' + color_temp + '00'
                if len(color_temp) == 1:
                    color_temp = '000' + color_temp + '00'
                color_temp = str('#'+color_temp)
                #self.axes.fill_between(location_x - max_rate_slot_x, location_x + max_rate_slot_x, location_y - max_rate_slot_y, location_y + max_rate_slot_y, color='blue')
                #self.axes.fill_between(x_box, y_box, where=(location_x - max_rate_slot_x<x_box) and (x_box<location_x + max_rate_slot_x) and
                #                                          (location_y - max_rate_slot_y<y_box) and (location_y + max_rate_slot_y<y_box), color='blue', alpha=.25)
                #self.axes.fill_between(x_box, y_box, color='#008000', alpha=.25)
                self.axes.fill(x_box, y_box, facecolor='b', alpha=0.5)

                # fill_between(X, 1, Y + 1, color='blue', alpha=.25)
                print('2')
                # print(dataRate[i, j])
                # print()







class My_Main_window(Ui_Dialog):
    def setupBusi(self, Ui_MainWindow):
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        dr.test()  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 第一步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第二步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        #self.pushButton.clicked.connect(self.dr.zoomin())
        self.graphicsView.setScene(graphicscene)  # 第三步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形
    def max_operation(self, Ui_MainWindow):
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        dr.test()
        dr.zoomin()
        graphicscene = QtWidgets.QGraphicsScene()  # 第一步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第二步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        # self.pushButton.clicked.connect(self.dr.zoomin())
        self.graphicsView.setScene(graphicscene)  # 第三步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形
    def min_operation(self, Ui_MainWindow):
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        dr.test()
        dr.zoomout()
        graphicscene = QtWidgets.QGraphicsScene()  # 第一步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第二步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        # self.pushButton.clicked.connect(self.dr.zoomin())
        self.graphicsView.setScene(graphicscene)  # 第三步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
    def rsrp_draw(self, Ui_MainWindow):
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        dr.test()
        dr.rsrp()
        graphicscene = QtWidgets.QGraphicsScene()  # 第一步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第二步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        # self.pushButton.clicked.connect(self.dr.zoomin())
        self.graphicsView.setScene(graphicscene)  # 第三步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形

    def RSRP_showtext(self, Ui_MainWindow):
        freq = self.input_freq.text()
        bandwidth = self.input_bandwidth.text()
        RSRP_threshold = self.input_rsrp.text()

        if freq and bandwidth and RSRP_threshold:
            # self.display_box.setText('系统中心频率：' + str(freq) + 'GHz, 带宽：' + str(bandwidth)+ 'MHz, RSRP门限：'+
            #                        str(RSRP_threshold)+'dBm\n RSRP: '+ str(RSRP_ratio)+'%')
            self.display_box.setText('系统中心频率：' + str(freq) + 'GHz, 带宽：' + str(bandwidth) + 'MHz, RSRP门限：' +
                                     str(RSRP_threshold) + 'dBm\n')
            self.display_box.update()
            self.input_freq.clear()

            # self.text.clear()
        else:
            self.display_box.setText("请输入系统中心频率")
        print('ok')

    def Max_rate(self, Ui_MainWindow):
        freq = self.input_freq.text()
        bandwidth = self.input_bandwidth.text()
        RSRP_threshold = self.input_rsrp.text()
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        dr.test()
        dr.Max_rate()
        graphicscene = QtWidgets.QGraphicsScene()  # 第一步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第二步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        # self.pushButton.clicked.connect(self.dr.zoomin())
        self.graphicsView.setScene(graphicscene)  # 第三步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形