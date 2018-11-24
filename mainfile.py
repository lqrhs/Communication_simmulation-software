from PyQt5 import QtCore, QtGui, QtWidgets
from lqr_drawpic import My_Main_window
import sys



if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication类，作为GUI主程序入口，需要import sys，可紧放在这句之前，也可放在代码最前面部分
        widget = QtWidgets.QMainWindow()  # 因为Qt Designer默认继承的object类，不提供show()显示方法，所以我们生成一个QWidget（窗口）对象来重载我们设计的Ui_Dialog类，达到显示效果。
        mywindow = My_Main_window()  # 实例化之前定义的窗口类
        mywindow.setupUi(widget)  # 设置布局Ui，布局的对象是刚才生成的widget（窗口）

        mywindow.push_max.clicked.connect(lambda: mywindow.max_operation(widget))
        mywindow.push_min.clicked.connect(lambda: mywindow.min_operation(widget))

        mywindow.setupBusi(widget)  # 设置业务

        # radioButton是计算RSRP的按钮，忘了改名字了
        mywindow.radioButton.clicked.connect(lambda: mywindow.RSRP_showtext(widget))
        mywindow.radioButton.clicked.connect(lambda: mywindow.rsrp_draw(widget))

        # radioButton_2是计算最大下行速率的按钮
        mywindow.radioButton_2.clicked.connect(lambda: mywindow.Max_rate(widget))


        widget.show()  # 使用 show() 方法
        """
        freq = mywindow.input_freq.text()
        if freq:
                print(freq)
        mywindow.display_box.setText(str(freq))
        mywindow.display_box.setText("123", freq)
        """
        sys.exit(app.exec_())
        # mywindow.other_operation(widget)
        """
        # 获取文本框中的内容
        self.lineEdit.text()

        # 设置内容
        self.lineEdit.setText()

        # 清空文本框中的内容就可以通过设置内容为空就行了
        self.lineEdit.setText("")


        widget.show()  # 使用 show() 方法
        sys.exit(app.exec_())
        """