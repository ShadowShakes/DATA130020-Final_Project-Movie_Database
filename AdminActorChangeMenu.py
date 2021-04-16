#-*- coding = utf-8 -*-
#@Time : 2020/7/7 11:48
#@Author : 陈劭涵
#@File : AdminActorChange.py
#@Software : PyCharm

#该文件是管理员演员修改界面的UI设计文件
import sys
import pic2
import pyodbc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton

from ActorChangeNote import *
from ActorChangeNoteMenu import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1313, 1008)
        Form.setFixedSize(1313,1008)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-73xdq9.jpg);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(460, 20, 451, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(900, 90, 151, 41))
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
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 90, 351, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(210, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(550, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 930, 241, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100),stop:1\n"
"rgba(158,150,200,10));\n"
"border_radius:5px;\n"
"border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 850, 111, 41))
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
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 730, 81, 21))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(680, 780, 71, 21))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(80, 780, 81, 20))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 680, 441, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 680, 431, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(680, 630, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(680, 680, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(790, 780, 431, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 730, 441, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 620, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 850, 111, 41))
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
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 630, 441, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 680, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 779, 441, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(790, 630, 431, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 850, 111, 41))
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
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(680, 730, 71, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 730, 431, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        #展示框tablewidget控件设置
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 1271, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #跳转至演员修改界面的按钮设置
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1100, 95, 110, 30))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_6.setObjectName("pushButton_6")
        #控件设置完成

        self.retranslateUi(Form)
        #将各按钮绑定至对应的函数功能上
        self.pushButton.clicked.connect(self.searchactor)
        self.pushButton_2.clicked.connect(self.insert)
        self.pushButton_3.clicked.connect(self.updateactor)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.close)
        self.pushButton_6.clicked.connect(lambda :self.jump_to_actornote())
        QtCore.QMetaObject.connectSlotsByName(Form)

    #定义跳转至指南界面的函数
    def jump_to_actornote(self):
        self.loginshow =mainWin10()
        self.loginshow.show()

    #以下几个函数即为连接到数据库并进行SQL增删修改操作的实现
    #搜索
    def searchactor(self):
        name = self.textEdit_2.toPlainText()
        sql = "select * from 演员 where 演员姓名 like "
        sql += "'%" + name + "%'"

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
                item_0 = QTableWidgetItem(str(row[0]))
                item_1 = QTableWidgetItem(row[1])
                item_2 = QTableWidgetItem(row[2])
                item_3 = QTableWidgetItem(row[3])
                item_4 = QTableWidgetItem(row[4])
                item_5 = QTableWidgetItem(row[5])
                item_6 = QTableWidgetItem(row[6])
                item_7 = QTableWidgetItem(row[7])
                self.tableWidget.setItem(number, 0, item_0)
                self.tableWidget.setItem(number, 1, item_1)
                self.tableWidget.setItem(number, 2, item_2)
                self.tableWidget.setItem(number, 3, item_3)
                self.tableWidget.setItem(number, 4, item_4)
                self.tableWidget.setItem(number, 5, item_5)
                self.tableWidget.setItem(number, 6, item_6)
                self.tableWidget.setItem(number, 7, item_7)
                row = cursor.fetchone()
            conn.close()
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clearContents()
                #item_error = QTableWidgetItem('未找到满足条件的演员')
                #self.tableWidget.setItem(0, 0, item_error)
                QMessageBox.information(self.pushButton, "提醒", "未找到满足条件的演员", QMessageBox.Yes)
    #插入
    def insert(self):
        actor = self.lineEdit_2.text()
        sex = self.lineEdit_3.text()
        birth = self.lineEdit_4.text()
        place = self.lineEdit_5.text()
        work1 = self.lineEdit_6.text()
        work2 = self.lineEdit_7.text()
        work3 = self.lineEdit_8.text()

        sql = "insert into 演员 values("

        sql += "'" + actor + "'"

        if sex != '':
            sql += ",'" + sex + "'"
        else:
            sql += ",null"

        if birth != '':
            sql += ",'" + birth + "'"
        else:
            sql += ",null"

        if place != '':
            sql += ",'" + place + "'"
        else:
            sql += ",null"

        if work1 != '':
            sql += ",'" + work1 + "'"
        else:
            sql += ",null"

        if work2 != '':
            sql += ",'" + work2 + "'"
        else:
            sql += ",null"

        if work3 != '':
            sql += ",'" + work3 + "')"
        else:
            sql += ",null)"

        conn = pyodbc.connect(
            'DRIVER=SQL Server Native Client 10.0;SERVER=DESKTOP-9A1SGRN;DATABASE=电影行业数据库;UID=CSHtest;PWD=111111')
        cursor = conn.cursor()
        flag = 0
        try:
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.tableWidget.clearContents()
            #item_success = QTableWidgetItem('插入成功')
            #self.tableWidget.setItem(0, 0, item_success)
            QMessageBox.information(self.pushButton, "提醒", "插入成功", QMessageBox.Yes)
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clearContents()
                #item_error = QTableWidgetItem('插入失败，检查输入')
                #self.tableWidget.setItem(0, 0, item_error)
                QMessageBox.information(self.pushButton, "提醒", "插入失败，请检查输入", QMessageBox.Yes)
    #更新
    def updateactor(self):
        anum = self.lineEdit.text()
        uactor = self.lineEdit_2.text()
        usex = self.lineEdit_3.text()
        ubirth = self.lineEdit_4.text()
        uplace = self.lineEdit_5.text()
        uwork1 = self.lineEdit_6.text()
        uwork2 = self.lineEdit_7.text()
        uwork3 = self.lineEdit_8.text()

        sql = "update 演员 set "
        isini = 1

        if uactor != '':
            if isini == 0:
                sql += ","
            sql += "演员姓名 = '" + uactor + "'"
            isini = 0

        if usex != '':
            if isini == 0:
                sql += ","
            sql += "演员性别 = '" + usex + "'"
            isini = 0

        if ubirth != '':
            if isini == 0:
                sql += ","
            sql += "出生日期 = '" + ubirth + "'"
            isini = 0

        if uplace != '':
            if isini == 0:
                sql += ","
            sql += "出生地 = '" + uplace + "'"
            isini = 0

        if uwork1 != '':
            if isini == 0:
                sql += ","
            sql += "代表作1 = '" + uwork1 + "'"
            isini = 0

        if uwork2 != '':
            if isini == 0:
                sql += ","
            sql += "代表作2 = '" + uwork2 + "'"
            isini = 0

        if uwork3 != '':
            if isini == 0:
                sql += ","
            sql += "代表作3 = '" + uwork3 + "'"
            isini = 0

        sql += " where 演员编号=" + anum

        conn = pyodbc.connect(
            'DRIVER=SQL Server Native Client 10.0;SERVER=DESKTOP-9A1SGRN;DATABASE=电影行业数据库;UID=CSHtest;PWD=111111')
        cursor = conn.cursor()
        flag = 0
        try:
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.tableWidget.clearContents()
            #item_success = QTableWidgetItem('修改成功')
            #self.tableWidget.setItem(0, 0, item_success)
            QMessageBox.information(self.pushButton, "提醒", "修改成功", QMessageBox.Yes)
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clearContents()
                #item_error = QTableWidgetItem('修改失败，检查输入')
                #self.tableWidget.setItem(0, 0, item_error)
                QMessageBox.information(self.pushButton, "提醒", "修改失败，请检查输入", QMessageBox.Yes)
    #删除
    def delete(self):
        dnum = self.lineEdit.text()
        sql = "delete from 演员 where 演员编号=" + dnum
        conn = pyodbc.connect(
            'DRIVER=SQL Server Native Client 10.0;SERVER=DESKTOP-9A1SGRN;DATABASE=电影行业数据库;UID=CSHtest;PWD=111111')
        cursor = conn.cursor()
        flag = 0
        try:
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.tableWidget.clearContents()
            #item_success = QTableWidgetItem('删除成功')
            #self.tableWidget.setItem(0, 0, item_success)
            QMessageBox.information(self.pushButton, "提醒", "删除成功", QMessageBox.Yes)
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clearContents()
                #item_error = QTableWidgetItem('删除失败，检查输入')
                #self.tableWidget.setItem(0, 0, item_error)
                QMessageBox.information(self.pushButton, "提醒", "删除失败，请检查输入", QMessageBox.Yes)


    #控件初始化及信息
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "演员数据修改页面"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">欢迎来到演员数据修改页面</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "查询记录"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">演员名字关键字查询</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">数据记录将展示如下</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "返回电影数据修改页面"))
        self.pushButton_4.setText(_translate("Form", "删除记录"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">出生地</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">代表作3</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">代表作2</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">演员姓名</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">出生日期限</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">演员编号</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "修改记录"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">演员性别</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "插入记录"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">代表作1</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "演员编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "演员姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "演员性别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "出生日期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "出生地"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "代表作1"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "代表作2"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "代表作3"))
        self.pushButton_6.setText(_translate("Form", "修改指南"))
        self.pushButton_6.clicked.connect(lambda: self.jump_to_actornote())

