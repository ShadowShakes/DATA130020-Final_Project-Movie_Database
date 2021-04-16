#-*- coding = utf-8 -*-
#@Time : 2020/7/2 22:46
#@Author : 陈劭涵
#@File : Search.py
#@Software : PyCharm


#该文件是触发电影查询界面的类与主函数文件，mainWin类被连接到introduce文件中
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
#导入SearchMoiveMenu中的ui代码内容
from SearchMovieMenu import *
import pic2
# 创建mainWin类并传入Ui_Form；QMainWindow和QtWidgets.QMainwindow效果一样，但不加前缀会产生错误
# 在introduce界面中连接mainWin类，触发pushbutton连接到此页面
class mainWin(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    # PyQt5主函数的固定用法
    app = QApplication(sys.argv)
    main_win = mainWin()
    main_win.show()
    sys.exit(app.exec_())