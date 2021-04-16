#-*- coding = utf-8 -*-
#@Time : 2020/7/8 12:21
#@Author : 陈劭涵
#@File : Multi.py
#@Software : PyCharm


#这是多功能页面的启动文件，连接至introduce
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from MultiMenu import *

class mainWin30(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin30, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win30 = mainWin30()
    main_win30.show()
    sys.exit(app.exec_())