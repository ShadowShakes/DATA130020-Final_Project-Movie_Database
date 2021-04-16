#-*- coding = utf-8 -*-
#@Time : 2020/7/8 0:00
#@Author : 陈劭涵
#@File : MovieChangeNote.py
#@Software : PyCharm

#这是电影修改界面指南的UI设计函数

from PyQt5 import QtCore, QtGui, QtWidgets
import pic2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1142, 760)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-4211zg.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 40, 421, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 1041, 501))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 630, 151, 41))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改指南"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">管理员修改电影数据指南</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">在管理员操作界面，我们允许根据关键字进行查询以及插入、修改、删除等功能。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">查询框中只支持管理员输入电影名称的关键字进行查询，并且查询结果会被展示在表中。</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:14pt; color:#ffffff;\">管理员在插入数据时，无需输入电影编号，只需输入其它八项数据，并且允许为空。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">点击插入按钮，即可实现插入数据的功能，该条数据的电影编号为当前最大编号加一，</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">编号的插入为自动实现。</span></p><p><br/><span style=\" font-size:14pt; color:#ffffff;\">管理员在修改数据时，必须输入电影编号，电影编号的查询由查询功能实现。想要</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">修改某部电影的信息，只需输入相应的电影编号，然后根据需求在其他八项中输入修改</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">后的内容，允许为空。输入完毕后点击修改按钮即可。</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:14pt; color:#ffffff;\">管理员在删除数据时，必须输入电影编号，电影编号的查询由查询功能实现。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">想要删除某部电影的数据，只需输入相应的电影编号，点击删除按钮即可。</span></p><p><br/></p><p><span style=\" font-size:14pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "返回"))
