#-*- coding = utf-8 -*-
#@Time : 2020/7/7 23:59
#@Author : 陈劭涵
#@File : ActorChange.py
#@Software : PyCharm

#该文件是管理员演员修改界面指南界面的启动文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from ActorChangeNoteMenu import *

class mainWin10(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin10, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win10 = mainWin10()
    main_win10.show()
    sys.exit(app.exec_())