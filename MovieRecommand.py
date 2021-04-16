#-*- coding = utf-8 -*-
#@Time : 2020/7/8 12:09
#@Author : 陈劭涵
#@File : MovieRecommand.py
#@Software : PyCharm

#这是电影随机界面的启动文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from MovieRecommandMenu import *

class mainWin20(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin20, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win20 = mainWin20()
    main_win20.show()
    sys.exit(app.exec_())