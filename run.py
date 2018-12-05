#-*- coding: utf-8 -*-
from __future__ import division
import ctypes
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
__author__ = 'Administrator'
from PyQt4 import QtGui,QtCore
import sys

#from canard import can
#from canard.hw import cantact
import locale
import time
import re
import datetime

from ui.ui import Ui_MainWindow
from ui.deviceUi import Ui_Dialog

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.createActions()
        self.createMenus()
        self.createToolBar()
        #self.connect(self.ui.commandLinkButton, QtCore.SIGNAL("clicked()"),self.SendMessage)
        #self.ui.fileMenu.addAction(self.zoominAction)

    def createActions(self):
        self.zoominAction=QtGui.QAction(QtGui.QIcon("tes.png"),self.trUtf8("放大"),self)
        #self.zoominAction=QtGui.QAction(self.trUtf8('放大'),self)
        self.zoominAction.setShortcut("Ctrl+P")
        self.zoominAction.setToolTip(self.trUtf8("放大"))
        #self.connect(self.zoominAction,QtCore.SIGNAL("triggered()"),self.anotherWindow)

        self.zoomoutAction=QtGui.QAction(QtGui.QIcon("tes.png"),self.trUtf8("缩小"),self)
        #self.zoominAction=QtGui.QAction(self.trUtf8('放大'),self)
        self.zoomoutAction.setShortcut("Ctrl+P")
        self.zoomoutAction.setToolTip(self.trUtf8("缩小"))


    def SendMessage(self):
        self.ui.textBrowser.setPlainText(u'你按了按钮！')

    def createToolBar(self):
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.zoominAction)
        #self.toolbar = self.addToolBar('out')
        self.toolbar.addAction(self.zoomoutAction)

    def createMenus(self):
        self.ui.menu.addAction(self.zoominAction)


    def Set(self):
        self.ui.textBrowser.setPlainText(u'你想设置设备参数！')
        #self.ui.add

    def anotherWindow(self):
        self.WChild = Ui_Dialog()
        self.Dialog = QtGui.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.WChild.setupUi(self.Dialog)
        self.WChild.pushButton.clicked.connect(self.GetLine)
        #self.WChild.pushButtonCancel.clicked.connect(self.APPclose)
        self.Dialog.exec_()

    def GetLine(self):
        lineData=self.WChild.lineEdit.text()
        self.setWindowTitle(lineData)
        self.Dialog.close()




def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    

