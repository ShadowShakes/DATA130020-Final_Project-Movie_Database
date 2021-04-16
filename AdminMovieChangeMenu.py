#-*- coding = utf-8 -*-
#@Time : 2020/7/5 22:38
#@Author : 陈劭涵
#@File : AdminChange.py
#@Software : PyCharm

#这是电影数据修改界面的UI代码文件
import sys
import pic2
import pyodbc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton

from AdminMovieChangeMenu import *
from AdminActorChange import *

from MovieChangeNote import *
from MovieChangeNoteMenu import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1313, 1008)
        Form.setFixedSize(1313,1008)
        Form.setStyleSheet("#Form{background-image:url(:/wallhaven-4vo31p.png);}")
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
        self.label_8.setGeometry(QtCore.QRect(220, 90, 251, 41))
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
        self.pushButton_5.setGeometry(QtCore.QRect(570, 940, 241, 41))
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
        self.pushButton_4.setGeometry(QtCore.QRect(950, 880, 111, 41))
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
        self.label_6.setGeometry(QtCore.QRect(80, 720, 81, 21))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 830, 721, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(690, 770, 54, 21))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(80, 770, 81, 20))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 670, 441, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 670, 431, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(680, 620, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(680, 670, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(790, 770, 431, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 720, 441, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 610, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 880, 111, 41))
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
        self.lineEdit.setGeometry(QtCore.QRect(190, 620, 441, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 670, 61, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 769, 441, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(790, 620, 431, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 880, 111, 41))
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
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(220, 820, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(690, 720, 41, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 720, 431, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        #设置tableWidget用于展示
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(80, 180, 1141, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(950, 940, 111, 41))
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
        self.pushButton_6.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(1100, 95, 110, 30))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("\n"
                                        "*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
                                        "rgba(214,249,255,100),stop:1\n"
                                        "rgba(158,150,200,10));\n"
                                        "border_radius:5px;\n"
                                        "border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        #将各按钮绑定至相应函数功能上
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.insert)
        self.pushButton_3.clicked.connect(self.updatemovie)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.jump_to_actorchange)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(lambda:self.jump_to_movienote())
        QtCore.QMetaObject.connectSlotsByName(Form)

    #跳转至电影修改指南界面
    def jump_to_movienote(self):
        self.loginshow =mainWin11()
        self.loginshow.show()
    #跳转回演员数据修改界面
    def jump_to_actorchange(self):
        self.loginshow = mainWin7()
        self.loginshow.show()
    #查询函数
    def search(self):
        name = self.textEdit_2.toPlainText()
        sql = "select * from 电影 where 电影名称 like "
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
                item_8 = QTableWidgetItem(row[8])
                self.tableWidget.setItem(number, 0, item_0)
                self.tableWidget.setItem(number, 1, item_1)
                self.tableWidget.setItem(number, 2, item_2)
                self.tableWidget.setItem(number, 3, item_3)
                self.tableWidget.setItem(number, 4, item_4)
                self.tableWidget.setItem(number, 5, item_5)
                self.tableWidget.setItem(number, 6, item_6)
                self.tableWidget.setItem(number, 7, item_7)
                self.tableWidget.setItem(number, 8, item_8)
                row = cursor.fetchone()
            conn.close()
            flag = 1
        except Exception:
            if flag == 0:
                self.tableWidget.clearContents()
                #item_error = QTableWidgetItem('未找到满足条件的电影')
                #self.tableWidget.setItem(0, 0, item_error)
                QMessageBox.information(self.pushButton, "提醒", "未找到满足条件的电影", QMessageBox.Yes)
    #插入函数
    def insert(self):
        movie = self.lineEdit_2.text()
        writer_1 = self.lineEdit_3.text()
        writer_2 = self.lineEdit_4.text()
        year = self.lineEdit_5.text()
        time = self.lineEdit_6.text()
        company = self.lineEdit_7.text()
        language = self.lineEdit_8.text()
        comment = self.lineEdit_9.text()

        sql = "insert into 电影 values("

        sql += "'" + movie + "'"

        if writer_1 != '':
            sql += ",'" + writer_1 + "'"
        else:
            sql += ",null"

        if writer_2 != '':
            sql += ",'" + writer_2 + "'"
        else:
            sql += ",null"

        if year != '':
            sql += ",'" + year + "'"
        else:
            sql += ",null"

        if time != '':
            sql += ",'" + time + "'"
        else:
            sql += ",null"

        if company != '':
            sql += ",'" + company + "'"
        else:
            sql += ",null"

        if language != '':
            sql += ",'" + language + "'"
        else:
            sql += ",null"

        if comment != '':
            sql += ",'" + comment + "')"
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
    #修改函数（！不可使用update！会占用关键字！）
    def updatemovie(self):
        mnum = self.lineEdit.text()
        umovie = self.lineEdit_2.text()
        uwriter_1 = self.lineEdit_3.text()
        uwriter_2 = self.lineEdit_4.text()
        uyear = self.lineEdit_5.text()
        utime = self.lineEdit_6.text()
        ucompany = self.lineEdit_7.text()
        ulanguage = self.lineEdit_8.text()
        ucomment = self.lineEdit_9.text()

        sql = "update 电影 set "
        isini = 1

        if umovie != '':
            if isini == 0:
                sql += ","
            sql += "电影名称 = '" + umovie + "'"
            isini = 0

        if uwriter_1 != '':
            if isini == 0:
                sql += ","
            sql += "编剧1 = '" + uwriter_1 + "'"
            isini = 0

        if uwriter_2 != '':
            if isini == 0:
                sql += ","
            sql += "编剧2 = '" + uwriter_2 + "'"
            isini = 0

        if uyear != '':
            if isini == 0:
                sql += ","
            sql += "发行年份 = '" + uyear + "'"
            isini = 0

        if utime != '':
            if isini == 0:
                sql += ","
            sql += "时长_分钟 = '" + utime + "'"
            isini = 0

        if ucompany != '':
            if isini == 0:
                sql += ","
            sql += "出品公司编号 = '" + ucompany + "'"
            isini = 0

        if ulanguage != '':
            if isini == 0:
                sql += ","
            sql += "语言 = '" + ulanguage + "'"
            isini = 0

        if ucomment != '':
            if isini == 0:
                sql += ","
            sql += "影评 = '" + ucomment + "'"
            isini = 0

        sql += " where 电影编号=" + mnum

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
    #删除函数
    def delete(self):
        dnum = self.lineEdit.text()
        sql = "delete from 电影 where 电影编号=" + dnum
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

    #配置控件信息
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据修改页面"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">欢迎来到电影数据修改页面</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "查询记录"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">电影名关键字查询</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">数据记录将展示如下</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "进入演员数据修改页面"))
        self.pushButton_4.setText(_translate("Form", "删除记录"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">发行年份</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">语言</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">出品公司编号</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">电影名称</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">编剧2</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">电影编号</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "修改记录"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">编剧1</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "插入记录"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">影评与备注</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">时长</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "电影编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "电影名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "编剧1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "编剧2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "发行年份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "时长"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "出品公司编号"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "语言"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "影评"))

        self.pushButton_6.setText(_translate("Form", "退出"))
        self.pushButton_7.setText(_translate("Form", "修改指南"))
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(lambda :self.jump_to_movienote())

