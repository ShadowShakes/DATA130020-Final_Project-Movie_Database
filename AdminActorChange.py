#-*- coding = utf-8 -*-
#@Time : 2020/7/7 11:48
#@Author : 陈劭涵
#@File : AdminActorChange.py
#@Software : PyCharm

#该文件是用于启动管理员演员修改界面的文件
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from AdminActorChangeMenu import *

class mainWin7(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin7, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)

    main_win7 = mainWin7()
    main_win7.show()
    sys.exit(app.exec_())