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
        self.label.setGeometry(QtCore.QRect(380, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 130, 1041, 501))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(480, 650, 151, 41))
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
        Form.setWindowTitle(_translate("Form", "影评指南"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">用户撰写影评电影指南</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">在撰写影评操作界面，我们允许根据关键字进行查询以及插入和修改影评的功能。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">查询框中只支持用户输入电影名称的关键字进行查询，并且查询结果会被展示在表中。</span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:14pt; color:#ffffff;\">用户在撰写新影评时，需输入电影编号，在提示框对应的文本框内撰写自己的评论等文字，</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">再点击“添加或修改您的评论”按钮，即可将自己的评论文字插入到对应的电影影评列下</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:14pt; color:#ffffff;\">用户在修改影评时，同样输入电影编号，在提示框对应的文本框内修改自己的评论等文字，</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">再点击“添加或修改您的评论”按钮，即可将自己的评论文字在对应的电影影评列下进行</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">修改</span><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:14pt; color:#ffffff;\">用户在删除影评时，同样输入电影编号，在提示框对应的文本框内将自己的评论等文字改为</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">空格，（注意：直接将评论框清空为0会导致报错，所以请用空格！），再点击“添加或修</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">改您的评论”按钮，即可将自己的评论文字在对应的电影影评列下进行删除（即转变为空格）</span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" font-size:14pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "返回"))