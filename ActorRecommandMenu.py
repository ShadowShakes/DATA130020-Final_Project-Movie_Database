#-*- coding = utf-8 -*-
#@Time : 2020/7/8 13:35
#@Author : 陈劭涵
#@File : ActorRecommandMenu.py
#@Software : PyCharm


#这是随机推荐演员的UI界面代码
import sys
import pyodbc
import pic2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#该UI界面从演员搜索界面修改而来，因而有大量注释内容，这些内容大多没有解释性，请适当忽略
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1313, 870)
        Form.setFixedSize(1313, 870)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-kwzpwm.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(460, 40, 400, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        '''self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(470, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")'''
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 205, 151, 41))
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
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(860, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        '''self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(600, 260, 351, 31))
        self.textEdit_2.setObjectName("textEdit_2")'''
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(670, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(670, 150, 87, 22))
        self.comboBox_3.setStyleSheet("\n"
                                      "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                      "rgba(214,249,255,100),stop:1\n"
                                      "rgba(158,150,200,10));\n"
                                      "border_radius:5px;\n"
                                      "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 120, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(260, 220, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        '''self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(600, 210, 351, 31))
        self.textEdit.setObjectName("textEdit")'''
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(470, 150, 87, 22))
        self.comboBox.setStyleSheet("\n"
                                    "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                    "rgba(214,249,255,100),stop:1\n"
                                    "rgba(158,150,200,10));\n"
                                    "border_radius:5px;\n"
                                    "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        '''self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(470, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")'''
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(860, 150, 87, 22))
        self.comboBox_4.setStyleSheet("\n"
                                      "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                      "rgba(214,249,255,100),stop:1\n"
                                      "rgba(158,150,200,10));\n"
                                      "border_radius:5px;\n"
                                      "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(620, 260, 91, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 320, 1211, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 795 , 151, 41))
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
        #绑定各功能按钮
        self.pushButton.clicked.connect(self.search_actor)
        self.pushButton_2.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #搜索函数
    def search_actor(self):
        sex = self.comboBox.currentText()
        age = self.comboBox_3.currentText()
        birth_place = self.comboBox_4.currentText()
        #rep_work = self.textEdit.toPlainText()
        #actor_name = self.textEdit_2.toPlainText()
        if sex == '' and age == '' and birth_place == '' :
            sql = """SELECT  TOP 10 * FROM (SELECT DISTINCT 演员.* FROM 演员 inner join 参演 on 演员.演员编号 = 参演.演员编号
                 inner join 电影 on 电影.电影编号 = 参演.电影编号) AS TEMP
                 ORDER by NEWID()"""
        else:
            sql = """SELECT  TOP 10 * FROM (SELECT DISTINCT 演员.* FROM 演员 inner join 参演 on 演员.演员编号 = 参演.演员编号
                 inner join 电影 on 电影.电影编号 = 参演.电影编号  WHERE """


            isini = 0

            if sex == '':
                pass
            else:
                if isini == 1:
                    sql += " AND "
                sql += "演员.演员性别='" + sex + "'"
                isini = 1

            if age == '':
                pass
            else:
                if isini == 1:
                    sql += " AND "
                if age == "10岁以下":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '2010-1-1'"
                if age == "10岁-20岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '2000-1-1' AND 演员.出生日期 < '2010-1-1'"
                if age == "20岁-30岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '1990-1-1' AND 演员.出生日期 < '2000-1-1'"
                if age == "30岁-40岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '1980-1-1' AND 演员.出生日期 < '1990-1-1'"
                if age == "40岁-50岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '1970-1-1' AND 演员.出生日期 < '1980-1-1'"
                if age == "50岁-60岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '1960-1-1' AND 演员.出生日期 < '1970-1-1'"
                if age == "60岁-70岁":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 > '1950-1-1' AND 演员.出生日期 < '1960-1-1'"
                if age == "70岁以上":
                    sql += "演员.出生日期 is not null AND 演员.出生日期 <> '' AND 演员.出生日期 < '1950-1-1'"
                isini = 1

            if birth_place == '':
                pass
            else:
                if isini == 1:
                    sql += " AND "
                sql += "演员.出生地 = '" + birth_place + "'"
                isini = 1
            '''if rep_work == '':
                pass
            else:
                if isini == 1:
                    sql += " AND "
                sql += "电影.电影名称 like '%" + rep_work + "%'"
                isini = 1
            if actor_name == '':
                pass
            else:
                if isini == 1:
                    sql += " AND "
                sql += "演员.演员姓名 like '%" + actor_name + "%'"
                isini = 1'''

            sql += ")AS TEMP ORDER by NEWID() "
        flag = 0

        try:
            conn = pyodbc.connect(
                'DRIVER=SQL Server Native Client 10.0;SERVER=DESKTOP-9A1SGRN;DATABASE=电影行业数据库;UID=CSHtest;PWD=111111')
            cursor = conn.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            if row[1] == '':
                pass
            num = self.tableWidget.rowCount()

            for i in range(0, num)[::-1]:
                self.tableWidget.removeRow(i)
            while row:
                number = self.tableWidget.rowCount()
                self.tableWidget.insertRow(number)
                item_0 = QTableWidgetItem(row[1])
                item_1 = QTableWidgetItem(row[2])  # 我们要求它可以修改，所以使用默认的状态即可
                item_2 = QTableWidgetItem(row[3])
                item_3 = QTableWidgetItem(row[4])
                item_4 = QTableWidgetItem(row[5])
                item_5 = QTableWidgetItem(row[6])
                item_6 = QTableWidgetItem(row[7])
                self.tableWidget.setItem(number, 0, item_0)
                self.tableWidget.setItem(number, 1, item_1)
                self.tableWidget.setItem(number, 2, item_2)
                self.tableWidget.setItem(number, 3, item_3)
                self.tableWidget.setItem(number, 4, item_4)
                self.tableWidget.setItem(number, 5, item_5)
                self.tableWidget.setItem(number, 6, item_6)
                row = cursor.fetchone()
            conn.close()
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clear()
                #item_error = QTableWidgetItem('未找到满足条件的演员')
                QMessageBox.information(self.pushButton, "提醒", "无相应查询记录", QMessageBox.Yes)
                #self.tableWidget.setItem(1, 1, item_error)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "随机演员介绍"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">欢迎来到随机演员介绍页面</span></p></body></html>"))
        self.label_4.setText(
            _translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">演员性别</span></p></body></html>"))
        '''self.label_9.setText(
            _translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">代表作品</span></p></body></html>"))'''
        self.pushButton.setText(_translate("Form", "刷一刷"))
        self.label_7.setText(
            _translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">出生地区</span></p></body></html>"))
        '''self.textEdit_2.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))'''
        self.label_6.setText(
            _translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">演员年龄</span></p></body></html>"))
        self.comboBox_3.setItemText(1, _translate("Form", "10岁以下"))
        self.comboBox_3.setItemText(2, _translate("Form", "10岁-20岁"))
        self.comboBox_3.setItemText(3, _translate("Form", "20岁-30岁"))
        self.comboBox_3.setItemText(4, _translate("Form", "30岁-40岁"))
        self.comboBox_3.setItemText(5, _translate("Form", "40岁-50岁"))
        self.comboBox_3.setItemText(6, _translate("Form", "50岁-60岁"))
        self.comboBox_3.setItemText(7, _translate("Form", "60岁-70岁"))
        self.comboBox_3.setItemText(8, _translate("Form", "70岁以上"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">分类刷刷</span></p></body></html>"))
        '''self.label_8.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">关键字查询</span></p></body></html>"))'''
        '''self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))'''
        self.comboBox.setItemText(1, _translate("Form", "男"))
        self.comboBox.setItemText(2, _translate("Form", "女"))
        '''self.label_10.setText(
            _translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">演员姓名</span></p></body></html>"))'''
        self.comboBox_4.setItemText(1, _translate("Form", "中国"))
        self.comboBox_4.setItemText(2, _translate("Form", "美国"))
        self.comboBox_4.setItemText(3, _translate("Form", "日本"))
        self.comboBox_4.setItemText(4, _translate("Form", "韩国"))
        self.comboBox_4.setItemText(5, _translate("Form", "意大利"))
        self.comboBox_4.setItemText(6, _translate("Form", "英国"))
        self.comboBox_4.setItemText(7, _translate("Form", "法国"))
        self.comboBox_4.setItemText(8, _translate("Form", "中国香港"))
        self.comboBox_4.setItemText(9, _translate("Form", "印度"))
        self.comboBox_4.setItemText(10, _translate("Form", "澳大利亚"))
        self.comboBox_4.setItemText(11, _translate("Form", "加拿大"))
        self.comboBox_4.setItemText(12, _translate("Form", "中国台湾"))
        self.comboBox_4.setItemText(13, _translate("Form", "德国"))
        self.comboBox_4.setItemText(14, _translate("Form", "俄罗斯"))
        self.comboBox_4.setItemText(15, _translate("Form", "西班牙"))
        self.comboBox_4.setItemText(16, _translate("Form", "泰国"))
        self.comboBox_4.setItemText(17, _translate("Form", "新西兰"))
        self.comboBox_4.setItemText(18, _translate("Form", "爱尔兰"))
        self.comboBox_4.setItemText(19, _translate("Form", "波兰"))
        self.comboBox_4.setItemText(20, _translate("Form", "伊朗"))
        self.comboBox_4.setItemText(21, _translate("Form", "其他地区"))
        self.label_12.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">刷刷结果</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "返回前面"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "演员姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "演员性别"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出生日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "出生地"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "代表作1"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "代表作2"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "代表作3"))
