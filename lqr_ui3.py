# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lqri_ui3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 508)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 351, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_3.setObjectName("label_3")

        # 用于输入中心频率的文本框
        self.input_freq = QtWidgets.QLineEdit(Dialog)
        self.input_freq.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.input_freq.setObjectName("input_freq")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 70, 60, 16))
        self.label_4.setObjectName("label_4")

        # 用于输入系统带宽的文本框
        self.input_bandwidth = QtWidgets.QLineEdit(Dialog)
        self.input_bandwidth.setGeometry(QtCore.QRect(300, 70, 113, 21))
        self.input_bandwidth.setObjectName("input_bandwidth")

        # 用于输入RSRP门限的文本框
        self.input_rsrp = QtWidgets.QLineEdit(Dialog)
        self.input_rsrp.setGeometry(QtCore.QRect(500, 70, 113, 21))
        self.input_rsrp.setText("")
        self.input_rsrp.setObjectName("input_rsrp")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(430, 70, 60, 16))
        self.label_5.setObjectName("label_5")

        # 用于承载matplot组件的graphicsView
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(40, 100, 461, 331))
        self.graphicsView.setObjectName("graphicsView")

        # 用于放大图像的单击按钮
        self.push_max = QtWidgets.QPushButton(Dialog)
        self.push_max.setGeometry(QtCore.QRect(530, 120, 113, 32))
        self.push_max.setObjectName("push_max")

        # 用于缩小图像的单击按钮
        self.push_min = QtWidgets.QPushButton(Dialog)
        self.push_min.setGeometry(QtCore.QRect(530, 170, 113, 32))
        self.push_min.setObjectName("push_min")

        # 用于计算RSRP的radioButton
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(540, 230, 100, 20))
        self.radioButton.setObjectName("radioButton")

        # 用于计算最大下行速率的radioButton
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 270, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        # 用于呈现计算结果的display_box
        self.display_box = QtWidgets.QTextBrowser(Dialog)
        self.display_box.setGeometry(QtCore.QRect(40, 450, 461, 41))
        self.display_box.setObjectName("display_box")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(500, 30, 111, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    """
    def RSRP(self):
        freq = self.input_freq.text()
        bandwidth = self.input_bandwidth.text()
        RSRP_threshold = self.input_rsrp.text()

        if freq and bandwidth and RSRP_threshold:
            #self.display_box.setText('系统中心频率：' + str(freq) + 'GHz, 带宽：' + str(bandwidth)+ 'MHz, RSRP门限：'+
            #                        str(RSRP_threshold)+'dBm\n RSRP: '+ str(RSRP_ratio)+'%')
            self.display_box.setText('系统中心频率：' + str(freq) + 'GHz, 带宽：' + str(bandwidth) + 'MHz, RSRP门限：' +
                                                            str(RSRP_threshold)+'dBm\n')
            self.display_box.update()
            self.input_freq.clear()

            # self.text.clear()
        else:
            self.display_box.setText("请输入系统中心频率")
        print('ok')
    """
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "通信仿真软件v1.0 著作人：刘启瑞、刘艳强、陈柯宇"))
        self.label_2.setText(_translate("Dialog", "请配置参数"))
        self.label_3.setText(_translate("Dialog", "系统中心频率"))
        self.label_4.setText(_translate("Dialog", "系统带宽"))
        self.label_5.setText(_translate("Dialog", "RSRP门限"))
        self.push_max.setText(_translate("Dialog", "放大"))
        self.push_min.setText(_translate("Dialog", "缩小"))
        self.radioButton.setText(_translate("Dialog", "RSRP概率"))
        self.radioButton_2.setText(_translate("Dialog", "最大下行速率"))
        self.label_6.setText(_translate("Dialog", "指导老师：皇甫伟"))

