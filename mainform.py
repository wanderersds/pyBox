#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, uic
from sportsmen import *
from table import *

class MainForm(QtGui.QMainWindow):
  def __init__(self):
    super(MainForm, self).__init__()
    uic.loadUi("mainform.ui", self)

    self.inputTable = inputTable(self.tableWidget)
    self.pareTable = pareTable(self.tableWidget_pare)
    
    self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.drowTable)
    self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.inputTable.editSportsmen)
    
    self.connect(self.toolButton_Plus, QtCore.SIGNAL("clicked()"), self.inputTable.addSportsmen)
    self.connect(self.toolButton_Minus, QtCore.SIGNAL("clicked()"), self.inputTable.removeSportsmen)
  
  def drowTable(self):
    self.pareTable.clear()
    for x in self.inputTable.sportsmens:  
      self.pareTable.addSportsmen(x)
      #print("x = ", x)
      #item = QtGui.QTableWidgetItem()
      #item.setText("ololo")
      #self.pareTable.table.setItem(0,0,item)
    

