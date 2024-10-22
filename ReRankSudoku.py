# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReRankSudoku.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 412)
        MainWindow.setStyleSheet("background-image: url(:/material/background);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 332, 332))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_0 = QtWidgets.QLabel(self.groupBox)
        self.label_0.setText("")
        self.label_0.setPixmap(QtGui.QPixmap(":/material/result/1"))
        self.label_0.setScaledContents(True)
        self.label_0.setObjectName("label_0")
        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap(":/material/result/2"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/material/result/3"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/material/result/4"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/material/result/5"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/material/result/6"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/material/result/7"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/material/result/8"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/material/result/0"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 121, 331))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_end = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.list_end.setFont(font)
        self.list_end.setStyleSheet("")
        self.list_end.setObjectName("list_end")
        self.verticalLayout.addWidget(self.list_end)
        self.speed_change = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.speed_change.setFont(font)
        self.speed_change.setStyleSheet("background-color: rgb(246, 211, 117);")
        self.speed_change.setObjectName("speed_change")
        self.speed_change.addItem("")
        self.speed_change.addItem("")
        self.speed_change.addItem("")
        self.speed_change.addItem("")
        self.verticalLayout.addWidget(self.speed_change)
        self.disorganize = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disorganize.setFont(font)
        self.disorganize.setObjectName("disorganize")
        self.verticalLayout.addWidget(self.disorganize)
        self.manual = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.manual.setFont(font)
        self.manual.setObjectName("manual")
        self.verticalLayout.addWidget(self.manual)
        self.Astar = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Astar.setFont(font)
        self.Astar.setObjectName("Astar")
        self.verticalLayout.addWidget(self.Astar)
        self.display = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(20, 342, 461, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_message.setFont(font)
        self.label_message.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_message.setText("")
        self.label_message.setObjectName("label_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "重排九宫"))
        self.list_end.setText(_translate("MainWindow", "123456780"))
        self.speed_change.setItemText(0, _translate("MainWindow", "0.1s/Step"))
        self.speed_change.setItemText(1, _translate("MainWindow", "0.2s/Step"))
        self.speed_change.setItemText(2, _translate("MainWindow", "0.5s/Step"))
        self.speed_change.setItemText(3, _translate("MainWindow", "1.0s/Step"))
        self.disorganize.setText(_translate("MainWindow", "随机打乱"))
        self.manual.setText(_translate("MainWindow", "手动打乱"))
        self.Astar.setText(_translate("MainWindow", "A*搜索"))
        self.display.setText(_translate("MainWindow", "效果演示"))
import resource
