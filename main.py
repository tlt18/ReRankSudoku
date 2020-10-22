import sys
import time
from functools import partial

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import Astar
import ReRankSudoku

list_range = [1,2,3,4,5,6,7,8,0]

def display(display_range):
    ui.label_0.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[0])))
    ui.label_1.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[1])))
    ui.label_2.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[2])))
    ui.label_3.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[3])))
    ui.label_4.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[4])))
    ui.label_5.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[5])))
    ui.label_6.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[6])))
    ui.label_7.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[7])))
    ui.label_8.setPixmap(QtGui.QPixmap(":/material/result/"+str(display_range[8])))
    sum = 0
    for num in display_range:
        sum *=10
        sum +=num
    ui.label_0.repaint()
    ui.label_1.repaint()
    ui.label_2.repaint()
    ui.label_3.repaint()
    ui.label_4.repaint()
    ui.label_5.repaint()
    ui.label_6.repaint()
    ui.label_7.repaint()
    ui.label_8.repaint()
    ui.list_end.setText(str(sum))

def inverse_number(range_l):
    flag=0
    for ind_s,s in enumerate(range_l):
        if s==0:
            continue
        for t in range_l[ind_s:]:
            if t==0:
                continue
            if t<s:
                flag +=1
    return flag

def disorganize_success():
    global list_range
    while True:
        random.shuffle (list_range)
        flag=inverse_number(list_range)
        if flag % 2 ==0:
            break
    display(list_range)
    ui.label_message.setText("随机打乱成功！")

def Astar_success():
    global list_range
    ui.label_message.setText("正在搜索，请耐心等待！")
    ui.label_message.repaint()
    display(list_range)
    tip=Astar.solution(list_range)
    if tip == -1:
        ui.label_message.setText("搜索超时，请重试！")
    else:
        ui.label_message.setText("用时"+str(tip)[:5]+"s,可以演示！")

def display_success():
    global list_range
    speed = float(ui.speed_change.currentText()[:3])
    while True:
        list_range=Astar.ans()
        if list_range == -1:
            list_range = [1,2,3,4,5,6,7,8,0]
            ui.label_message.setText("请先进行搜索！")
            break
        else:
            time.sleep(speed)
            display(list_range)
            times=Astar.times()
            ui.label_message.setText("剩余步骤："+str(times))

def manual_success():
    global list_range
    list_str=ui.list_end.text()
    list_temp=[]
    if len(list_str)!=9:
        ui.label_message.setText("请输入合法值！")
    else:
        for cha in list_str:
            try:
                list_temp.append(int(cha))
            except:
                ui.label_message.setText("请输入合法值！")
                return -1
        if sorted(list_temp)==[0,1,2,3,4,5,6,7,8]:
            if inverse_number(list_temp) % 2 ==0:
                ui.label_message.setText("手动打乱成功！")
                display(list_temp)
                list_range=list_temp
            else:
                ui.label_message.setText("此图形无法还原！")
        else :
            ui.label_message.setText("请输入合法值！")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ReRankSudoku.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.disorganize.clicked.connect(disorganize_success)
    ui.Astar.clicked.connect(Astar_success)
    ui.display.clicked.connect(display_success)
    ui.manual.clicked.connect(manual_success)
    sys.exit(app.exec_())
