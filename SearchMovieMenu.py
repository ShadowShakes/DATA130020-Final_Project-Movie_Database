#-*- coding = utf-8 -*-
#@Time : 2020/7/2 21:56
#@Author : 陈劭涵
#@File : SearchMENU.py
#@Software : PyCharm

#这是电影查询页面的具体UI设计代码，直接运行没有结果，需要运行Searchmovie.py才有用


from PyQt5.QtWidgets import QApplication
#定义一个类Ui_Form
import pyodbc
import sys
import pic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1313, 920)
        Form.setFixedSize(1313,920)
        Form.setStyleSheet("#Form{background-image: url(:/wallhaven-nry961.png);}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(510, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(460, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(460, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 371, 151, 41))
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
        self.label_7.setGeometry(QtCore.QRect(740, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(590, 250, 381, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(590, 300, 381, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(600, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(880, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(600, 150, 87, 22))
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
        self.label_8.setGeometry(QtCore.QRect(260, 240, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(590, 200, 381, 31))
        self.textEdit.setObjectName("textEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(880, 150, 87, 22))
        self.comboBox_2.setStyleSheet("\n"
"*{background-color:qlineargradient(spread:pad,x1:0.5,y1:0,x2:0.5,y2:1,stop:0\n"
"rgba(214,249,255,100),stop:1\n"
"rgba(158,150,200,10));\n"
"border_radius:5px;\n"
"border-color: rgb(170, 170, 255);color:rgb(255, 255, 255)}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(460, 150, 87, 22))
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(460, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(460, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(740, 150, 87, 22))
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
        self.label_12.setGeometry(QtCore.QRect(610, 420, 91, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(15, 472, 1281, 361))
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 855, 151, 41))
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
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search(self):
        category = self.comboBox.currentText()
        company = self.comboBox_3.currentText()
        language = self.comboBox_4.currentText()
        year = self.comboBox_2.currentText()
        name = self.textEdit.toPlainText()
        actor = self.textEdit_2.toPlainText()
        director = self.textEdit_3.toPlainText()
        if category == '' and company == '' and language == '' and year == '' and name == '' and actor == '' and director == '':
                sql = """select distinct * from 电影 inner join 电影分类 on 电影.电影编号=电影分类.电影编号
                    inner join 出品公司 on 电影.出品公司编号=出品公司.公司编号
                    inner join 参演 on 电影.电影编号=参演.电影编号
                    inner join 执导 on 电影.电影编号=执导.电影编号
                    inner join 导演 on 执导.导演编号=导演.导演编号
                    inner join 演员 on 参演.演员编号=演员.演员编号"""
        else:
                sql = """select distinct * from 电影 inner join 电影分类 on 电影.电影编号=电影分类.电影编号
    inner join 出品公司 on 电影.出品公司编号=出品公司.公司编号
    inner join 参演 on 电影.电影编号=参演.电影编号
    inner join 执导 on 电影.电影编号=执导.电影编号
    inner join 导演 on 执导.导演编号=导演.导演编号
    inner join 演员 on 参演.演员编号=演员.演员编号 where """

                isini = 0

                if category == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "(电影分类.类别编号1=(select  类别编号 from 类别 where 类别名称='" + category + "') or 电影分类.类别编号2=(select  类别编号 from 类别 where 类别名称='" + category + "'))"
                        isini = 1

                if company == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "出品公司.公司名称='" + company + "'"
                        isini = 1

                if language == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "电影.语言 like '%" + language + "%'"
                        isini = 1

                if year == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "电影.发行年份 = '" + year + "'"
                        isini = 1

                if name == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "电影.电影名称 like '%" + name + "%'"
                        isini = 1

                if actor == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "演员.演员姓名 like '%" + actor + "%'"
                        isini = 1

                if director == '':
                        pass
                else:
                        if isini == 1:
                                sql += " and "
                        sql += "导演.导演姓名 like '%" + director + "%'"
                        isini = 1

        flag = 0
        try:
                conn = pyodbc.connect(
                                'DRIVER=SQL Server Native Client 10.0;SERVER=DESKTOP-9A1SGRN;DATABASE=电影行业数据库;UID=CSHtest;PWD=111111')
                cursor = conn.cursor()
                cursor.execute(sql)
                row = cursor.fetchone()
                if  row[1]== '':
                        pass
                num = self.tableWidget.rowCount()

                for i in range(0, num)[::-1]:
                        self.tableWidget.removeRow(i)

                while row:
                                number = self.tableWidget.rowCount()
                                self.tableWidget.insertRow(number)
                                item_0 = QTableWidgetItem(row[1])
                                item_1 = QTableWidgetItem(row[20])
                                item_2 = QTableWidgetItem(row[22])
                                item_3 = QTableWidgetItem(row[2])
                                item_4 = QTableWidgetItem(row[4])
                                item_5 = QTableWidgetItem(row[5])
                                item_6 = QTableWidgetItem(row[7])
                                item_7 = QTableWidgetItem(row[13])
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
                                #item_error = QTableWidgetItem('未找到满足条件的电影')
                                QMessageBox.information(self.pushButton,"提醒","无相应查询记录",QMessageBox.Yes)
                                #self.tableWidget.setItem(0, 0, item_error)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "电影查询页面"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">欢迎来到电影查询页面</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">电影类型</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">电影名字</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">电影语言</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">发行公司</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">发行年份</span></p></body></html>"))
        self.comboBox_3.setItemText(1, _translate("Form", "芜湖出品有限公司"))
        self.comboBox_3.setItemText(2, _translate("Form", "起飞出品有限公司"))
        self.comboBox_3.setItemText(3, _translate("Form", "404有限公司"))
        self.comboBox_3.setItemText(4, _translate("Form", "小陈有限公司"))
        self.comboBox_3.setItemText(5, _translate("Form", "轩哥有限公司"))
        self.comboBox_3.setItemText(6, _translate("Form", "17张牌有限公司"))
        self.comboBox_3.setItemText(7, _translate("Form", "克里斯关下门有限公司"))
        self.comboBox_3.setItemText(8, _translate("Form", "靓仔王有限公司"))
        self.comboBox_3.setItemText(9, _translate("Form", "洋仔有限公司"))
        self.comboBox_3.setItemText(10, _translate("Form", "老詹有限公司"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">分类查询</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">关键字查询</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox_2.setItemText(1, _translate("Form", "2020"))
        self.comboBox_2.setItemText(2, _translate("Form", "2019"))
        self.comboBox_2.setItemText(3, _translate("Form", "2018"))
        self.comboBox_2.setItemText(4, _translate("Form", "2017"))
        self.comboBox_2.setItemText(5, _translate("Form", "2016"))
        self.comboBox_2.setItemText(6, _translate("Form", "2015"))
        self.comboBox_2.setItemText(7, _translate("Form", "2014"))
        self.comboBox_2.setItemText(8, _translate("Form", "2013"))
        self.comboBox_2.setItemText(9, _translate("Form", "2012"))
        self.comboBox_2.setItemText(10, _translate("Form", "2011"))
        self.comboBox_2.setItemText(11, _translate("Form", "2010"))
        self.comboBox_2.setItemText(12, _translate("Form", "2009"))
        self.comboBox_2.setItemText(13, _translate("Form", "2008"))
        self.comboBox_2.setItemText(14, _translate("Form", "2007"))
        self.comboBox_2.setItemText(15, _translate("Form", "2006"))
        self.comboBox_2.setItemText(16, _translate("Form", "2005"))
        self.comboBox_2.setItemText(17, _translate("Form", "2004"))
        self.comboBox_2.setItemText(18, _translate("Form", "2003"))
        self.comboBox_2.setItemText(19, _translate("Form", "2002"))
        self.comboBox_2.setItemText(20, _translate("Form", "2001"))
        self.comboBox_2.setItemText(21, _translate("Form", "2000"))
        self.comboBox_2.setItemText(22, _translate("Form", "1999"))
        self.comboBox_2.setItemText(23, _translate("Form", "1998"))
        self.comboBox_2.setItemText(24, _translate("Form", "1997"))
        self.comboBox_2.setItemText(25, _translate("Form", "1996"))
        self.comboBox_2.setItemText(26, _translate("Form", "1995"))
        self.comboBox_2.setItemText(27, _translate("Form", "1994"))
        self.comboBox_2.setItemText(28, _translate("Form", "1993"))
        self.comboBox_2.setItemText(29, _translate("Form", "1992"))
        self.comboBox_2.setItemText(30, _translate("Form", "1991"))
        self.comboBox_2.setItemText(31, _translate("Form", "1990"))
        self.comboBox_2.setItemText(32, _translate("Form", "1989"))
        self.comboBox_2.setItemText(33, _translate("Form", "1988"))
        self.comboBox_2.setItemText(34, _translate("Form", "1987"))
        self.comboBox_2.setItemText(35, _translate("Form", "1986"))
        self.comboBox_2.setItemText(36, _translate("Form", "1985"))
        self.comboBox_2.setItemText(37, _translate("Form", "1984"))
        self.comboBox_2.setItemText(38, _translate("Form", "1983"))
        self.comboBox_2.setItemText(39, _translate("Form", "1982"))
        self.comboBox_2.setItemText(40, _translate("Form", "1981"))
        self.comboBox_2.setItemText(41, _translate("Form", "1980"))
        self.comboBox.setItemText(1, _translate("Form", "剧情"))
        self.comboBox.setItemText(2, _translate("Form", "悬疑"))
        self.comboBox.setItemText(3, _translate("Form", "爱情"))
        self.comboBox.setItemText(4, _translate("Form", "惊悚"))
        self.comboBox.setItemText(5, _translate("Form", "科幻"))
        self.comboBox.setItemText(6, _translate("Form", "恐怖"))
        self.comboBox.setItemText(7, _translate("Form", "历史"))
        self.comboBox.setItemText(8, _translate("Form", "冒险"))
        self.comboBox.setItemText(9, _translate("Form", "奇幻"))
        self.comboBox.setItemText(10, _translate("Form", "情色"))
        self.comboBox.setItemText(11, _translate("Form", "同性"))
        self.comboBox.setItemText(12, _translate("Form", "武侠"))
        self.comboBox.setItemText(13, _translate("Form", "喜剧"))
        self.comboBox.setItemText(14, _translate("Form", "传记"))
        self.comboBox.setItemText(15, _translate("Form", "音乐"))
        self.comboBox.setItemText(16, _translate("Form", "运动"))
        self.comboBox.setItemText(17, _translate("Form", "灾难"))
        self.comboBox.setItemText(18, _translate("Form", "战争"))
        self.comboBox.setItemText(19, _translate("Form", "动画"))
        self.comboBox.setItemText(20, _translate("Form", "动作"))
        self.comboBox.setItemText(21, _translate("Form", "儿童"))
        self.comboBox.setItemText(22, _translate("Form", "犯罪"))
        self.comboBox.setItemText(23, _translate("Form", "歌舞"))
        self.comboBox.setItemText(24, _translate("Form", "古装"))
        self.comboBox.setItemText(25, _translate("Form", "家庭"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">导演名字</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">主演名字</span></p></body></html>"))
        self.comboBox_4.setItemText(1, _translate("Form", "汉语普通话"))
        self.comboBox_4.setItemText(2, _translate("Form", "闽南语"))
        self.comboBox_4.setItemText(3, _translate("Form", "上海话"))
        self.comboBox_4.setItemText(4, _translate("Form", "四川话"))
        self.comboBox_4.setItemText(5, _translate("Form", "粤语"))
        self.comboBox_4.setItemText(6, _translate("Form", "英语"))
        self.comboBox_4.setItemText(7, _translate("Form", "日语"))
        self.comboBox_4.setItemText(8, _translate("Form", "阿拉伯语"))
        self.comboBox_4.setItemText(9, _translate("Form", "韩语"))
        self.comboBox_4.setItemText(10, _translate("Form", "法语"))
        self.comboBox_4.setItemText(11, _translate("Form", "意大利语"))
        self.comboBox_4.setItemText(12, _translate("Form", "德语"))
        self.comboBox_4.setItemText(13, _translate("Form", "西班牙语"))
        self.comboBox_4.setItemText(14, _translate("Form", "印地语"))
        self.comboBox_4.setItemText(15, _translate("Form", "希伯来语"))
        self.comboBox_4.setItemText(16, _translate("Form", "俄语"))
        self.comboBox_4.setItemText(17, _translate("Form", "泰语"))
        self.comboBox_4.setItemText(18, _translate("Form", "波斯语"))
        self.comboBox_4.setItemText(19, _translate("Form", "葡萄牙语"))
        self.comboBox_4.setItemText(20, _translate("Form", "拉丁语"))
        self.comboBox_4.setItemText(21, _translate("Form", "越南语"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">查询结果</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "返回主页面"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "电影名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "导演"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "主演"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "编剧"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "发行年份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "时长"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "语言"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "制片公司"))

