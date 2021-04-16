#-*- coding = utf-8 -*-
#@Time : 2020/7/8 18:12
#@Author : 陈劭涵
#@File : Comment.py
#@Software : PyCharm

#这是启动影评界面的启动文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from CommentMenu import *

class mainWin40(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin40, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)
    main_win40 = mainWin40()
    main_win40.show()
    sys.exit(app.exec_())