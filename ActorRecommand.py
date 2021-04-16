#-*- coding = utf-8 -*-
#@Time : 2020/7/8 15:31
#@Author : 陈劭涵
#@File : ActorRecommand.py
#@Software : PyCharm

#这是随机推荐演员界面的启动文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from ActorRecommandMenu import *

class mainWin25(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin25, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win25 = mainWin25()
    main_win25.show()
    sys.exit(app.exec_())