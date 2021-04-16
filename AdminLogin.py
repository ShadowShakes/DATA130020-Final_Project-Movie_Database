#-*- coding = utf-8 -*-
#@Time : 2020/7/5 19:58
#@Author : 陈劭涵
#@File : AdminLogin.py
#@Software : PyCharm

#此文件是启动admin管理员界面并设定登陆功能的代码文件，与introduce页面连接

#导入AdminMenu和MovieChangeMenu中的ui代码内容以及必要的包和资源文件pic2
from SearchActorMenu import *
import sys
import pic2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from AdminMovieChangeMenu import *
from AdminMovieChange  import *
from AdminLoginMenu import *


class mainWin4(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin4, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit.setPlaceholderText('请输入管理员用户名')
        self.lineEdit_2.setPlaceholderText('请输入管理员密码')
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        #绑定登陆按钮
        self.pushButton.clicked.connect(self.check_login_func)
    #定义登陆函数
    def check_login_func(self):
        if USER_PWD.get(self.lineEdit.text()) == self.lineEdit_2.text():
            QMessageBox.information(self, 'Information', '登陆成功!')
            temp=1
            self.loginshow = mainWin5()
            self.loginshow.show()
        else:
            QMessageBox.critical(self, 'Wrong', '用户名或密码错误!')
            temp=2
        self.lineEdit.clear()
        self.lineEdit_2.clear()

if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)
    main_win4 = mainWin4()
    main_win4.show()
    sys.exit(app.exec_())