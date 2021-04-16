#-*- coding = utf-8 -*-
#@Time : 2020/7/5 19:58
#@Author : 陈劭涵
#@File : AdminLogin.py
#@Software : PyCharm

import sys
import pic2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QApplication
#此文件是admin登陆界面的ui设计文件，包含用户名密码登陆功能
#默认的管理员用户名与密码admin与admin
USER_PWD = {'admin': 'admin'}
#类
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(964, 580)
        #固定窗口大小
        Form.setFixedSize(964, 580)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-47vmoy.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 60, 301, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        #设置登陆按钮pushButton
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 400, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100),stop:1\n"
"rgba(158,150,200,10));\n"
"border_radius:5px;\n"
"border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(460, 230, 161, 31))
        self.lineEdit.setStyleSheet("\n"
"*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100),stop:1\n"
"rgba(158,150,200,10));\n"
"border_radius:5px;\n"
"border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 220, 81, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 310, 161, 31))
        self.lineEdit_2.setStyleSheet("\n"
"*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100),stop:1\n"
"rgba(158,150,200,10));\n"
"border_radius:5px;\n"
"border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(400, 130, 181, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        #设置返回按钮pushButton_2
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
                                      "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                      "rgba(214,249,255,100),stop:1\n"
                                      "rgba(158,150,200,10));\n"
                                      "border_radius:5px;\n"
                                      "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_2.setObjectName("pushButton_2")
        #控件设置完毕

        self.retranslateUi(Form)
        #将返回按钮绑定到返回事件上
        self.pushButton_2.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #初始登陆界面
    def lineedit_init(self):
        self.lineEdit.setPlaceholderText('请输入管理员用户名')
        self.lineEdit_2.setPlaceholderText('请输入管理员密码')
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit.textChanged.connect(self.check_input_func)
        self.lineEdit_2.textChanged.connect(self.check_input_func)
    #初始登陆按钮
    def pushbutton_init(self):
        self.pushButton.setEnabled(False)
        self.pushButtonlicked.connect(self.check_login_func)
    #核准登录信息函数
    def check_login_func(self):
        if USER_PWD.get(self.lineEdit.text()) == self.lineEdit_2.text():
            QMessageBox.information(self, 'Information', '登陆成功!')
        else:
            QMessageBox.critical(self, 'Wrong', '用户名或密码错误!')

        self.lineEdit.clear()
        self.lineEdit_2.clear()
    #获取输入信息函数
    def check_input_func(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    #控件初始化信息
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员页面"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">欢迎来到管理员页面</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "登陆"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">用户名</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">密码</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">请输入管理员信息</span></p></body></html>"))



