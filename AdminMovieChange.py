#-*- coding = utf-8 -*-
#@Time : 2020/7/5 22:38
#@Author : 陈劭涵
#@File : AdminChange.py
#@Software : PyCharm

#这是启动电影数据修改界面的代码文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from AdminMovieChangeMenu import *

class mainWin5(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin5, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)
    main_win5 = mainWin5()
    main_win5.show()
    sys.exit(app.exec_())