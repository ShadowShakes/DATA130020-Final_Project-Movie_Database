#-*- coding = utf-8 -*-
#@Time : 2020/7/6 21:36
#@Author : 陈劭涵
#@File : Develop.py
#@Software : PyCharm

#这是欢迎页面，同时也是主界面，通过各pushButton连接到多个不同的页面

#必要的包导入
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import pic

#ROOT_DIR = os.path.abspath('D:\PythonCEDemo\SQL\Movie UI')
#sys.path.append(ROOT_DIR)

from SearchMovie import *
from SearchActor import *

from AdminLogin import *
from AdminMovieChange import *

from Develop import *
from Multi import *
#定义一个类
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 580)
        #固定窗口大小，不允许拉伸
        Form.setFixedSize(900,580)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        #设置背景图片
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-0172q1.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(280, 75, 331, 51))
        self.label.setMaximumSize(QtCore.QSize(900, 600))
        palette = QtGui.QPalette()
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 155, 91, 21))
        self.label_2.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 235, 131, 51))
        self.pushButton.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
                                      "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                      "rgba(214,249,255,100),stop:1\n"
                                      "rgba(158,150,200,10));\n"
                                      "border_radius:5px;\n"
                                      "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 235, 131, 51))
        self.pushButton_2.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 355, 131, 51))
        self.pushButton_3.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 355, 131, 51))
        self.pushButton_4.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 465, 71, 31))
        self.pushButton_5.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_5.setObjectName("pushButton_5")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎界面"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">欢迎您来到电影数据库</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">快捷导航</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "我想找电影"))
        self.pushButton_2.setText(_translate("Form", "我想找演员"))
        self.pushButton_3.setText(_translate("Form", "多功能页面"))
        self.pushButton_4.setText(_translate("Form", "我是管理员"))
        self.pushButton_5.setText(_translate("Form", "关于我们"))
        #以上pushButton分别是四个跳转页面的实现按钮，以下是具体连接
        #连接电影查询跳转函数
        self.pushButton.clicked.connect((lambda :self.jump_to_searchmovie()))
        #连接演员查询跳转函数
        self.pushButton_2.clicked.connect(( lambda :self.jump_to_searchactor()))
        #连接多功能页面函数
        self.pushButton_3.clicked.connect((lambda:self.jump_to_multi()))
        #连接管理员登陆界面函数
        self.pushButton_4.clicked.connect((lambda: self.jump_to_admin()))
        #连接开发者界面函数
        self.pushButton_5.clicked.connect((lambda :self.jump_to_develop()))

    #定义跳转至电影查询界面的函数
    def jump_to_searchmovie(self):
    #mainWin即在searchmovie文件中定义的类mainWin，可去文件里查看
        self.loginshow = mainWin()
        self.loginshow.show()
    #定义跳转至演员查询界面的函数
    def jump_to_searchactor(self):
    # mainWin2即在searchactor文件中定义的类mainWin2，可去文件里查看
        self.loginshow = mainWin2()
        self.loginshow.show()
    #定义跳转至多功能页面的函数
    def jump_to_multi(self):
        self.loginshow=mainWin30()
        self.loginshow.show()
    #定义跳转至管理员登陆界面的函数
    def jump_to_admin(self):
    # mainWin即在adminlogin文件中定义的类mainWin4，可去文件里查看
        self.loginshow = mainWin4()
        self.loginshow.show()
    #定义跳转至开发者信息页面的函数
    def jump_to_develop(self):
        self.loginshow = mainWin6()
        self.loginshow.show()


#主函数，用于展示UI界面
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QWidget = QtWidgets.QWidget()
    ui = Ui_Form() # 这是原py中的类
    ui.setupUi(QWidget)
    QWidget.show()
    sys.exit(app.exec_())
