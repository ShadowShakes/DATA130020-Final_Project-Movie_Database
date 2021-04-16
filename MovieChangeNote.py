#-*- coding = utf-8 -*-
#@Time : 2020/7/8 0:00
#@Author : 陈劭涵
#@File : MovieChangeNote.py
#@Software : PyCharm

#这是电影修改界面指南的启动函数
import sys
import pic2

from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from MovieChangeNoteMenu import *


class mainWin11(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin11, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win11 = mainWin11()
    main_win11.show()
    sys.exit(app.exec_())