#-*- coding = utf-8 -*-
#@Time : 2020/7/6 21:36
#@Author : 陈劭涵
#@File : Develop.py
#@Software : PyCharm

#该文件是触发开发人员信息界面的类与主函数文件，mainWin6类被连接到introduce文件中
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
#导入SearchActorMenu中的ui代码内容
from SearchActorMenu import *

from DevelopMenu import *

class mainWin6(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin6, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)
    main_win6 = mainWin6()
    main_win6.show()
    sys.exit(app.exec_())

