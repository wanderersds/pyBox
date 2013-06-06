#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, uic
from sportsman import *
from table import *

class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        uic.loadUi("mainform.ui", self)

        self.pareTable = pareTable(self.tableWidget_pare)
        self.inputTable = inputTable(self.tableWidget)

        shortcut = QtGui.QShortcut(self.tableWidget_pare)
        shortcut.setKey(QtGui.QKeySequence("SPACE"))

        #self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.drowTable)
        self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.inputTable.editSportsman)
        self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.pareTable.drow)
        self.connect(self.toolButton_Plus, QtCore.SIGNAL("clicked()"), self.inputTable.addSportsman)
        self.connect(self.toolButton_Minus, QtCore.SIGNAL("clicked()"), self.inputTable.removeSportsman)
        self.connect(shortcut, QtCore.SIGNAL("activated()"), self.pareTable.setWinner)
        self.connect(self.save, QtCore.SIGNAL("activated()"), save )
        self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.changeTab )
        self.connect(self.nextButton, QtCore.SIGNAL("clicked()"), self.next_round )
        self.connect(self.resetButton, QtCore.SIGNAL("clicked()"), self.reset_round )
        self.connect(self.about, QtCore.SIGNAL("activated()"), self.show_about )

    def changeTab(self, num):
        session.commit()
        self.pareTable.drow()
  
    def next_round(self):
        self.lcdNumber.display(self.lcdNumber.intValue() + 1)
        self.pareTable.drow('only_winners')

    def reset_round(self):
        self.lcdNumber.display(0)
        self.pareTable.current_round = 0
        self.pareTable.drow()        

    def show_about(self):
        QtGui.QDialog.show(self, 'test')
