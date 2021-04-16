#-*- coding = utf-8 -*-
#@Time : 2020/7/6 21:36
#@Author : 陈劭涵
#@File : Develop.py
#@Software : PyCharm

#该文件是开发人员信息的UI信息文件
from PyQt5 import QtCore, QtGui, QtWidgets

import pic2
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1142, 860)
        Form.setFixedSize(1142, 860)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-q6ggqd.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 30, 251, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 90, 831, 91))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 190, 851, 141))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 660, 731, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(200, 340, 891, 311))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 760, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "开发人员信息"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">感谢您的支持！</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">本作品系复旦大学大数据学院2020年春季学期数据库及实现课程的期末项目，由</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">陈劭涵、王忠洋、詹远瞩、赵宇轩四位同学共同完成，并于最后进行调试与展示。</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">本作品是基于Pyqt5、Qtdesigner、SQL Server 2008等软件和软件包共同开发而成，</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">在开发过程中，我们边学习、摸索，边尝试实现预定的一系列功能。而在使用软件</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">与开发过程中未免我们也暴露了不少局限性与瑕疵，因此在很多方面仍需继续努力。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">在这里再次感谢您的支持！</span></p><p><span style=\" font-size:14pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">若您对我们的作品有意见或建议，我们随时欢迎与您交流。</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">若您想联系我们，可以发送邮件至17300180049@fudan.edu.cn</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">开发者与开发工作：</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">赵宇轩：SQL核心数据查询与修改函数编写，Python内的SQL查询函数编写与实现，</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">SQL查询与修改结果可视化编写</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">王忠洋：电影数据获取与爬取，电影数据修改与数据导入，后期SQL数据库数据结构</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">优化，SQL总脚本设计与导出</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">詹远瞩：SQL初期电影数据库的设计与搭建，SQL电影与演员数据界面的查询函数编写</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">与修改，SQL修改结果可视化</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">陈劭涵：;Pyqt5与SQL联合的GUI图形交互界面开发，Py-SQL联合实现方式的调研，Py</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">-SQL连接，SQL查询编程辅助</span></p><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "返回主页面"))

