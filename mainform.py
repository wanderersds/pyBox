#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
from sportsmen import *
from table import *

class MainForm(QtGui.QMainWindow):
  def __init__(self):
    super(MainForm, self).__init__()
    uic.loadUi("mainform.ui", self)

    self.inputTable = table(self.tableWidget)
    self.pareTable = table(self.tableWidget_pare)
    
    self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.drowTable)
    self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.inputTable.editSportsmen)
    
    self.connect(self.toolButton_Plus, QtCore.SIGNAL("clicked()"), self.inputTable.addSportsmen)
    self.connect(self.toolButton_Minus, QtCore.SIGNAL("clicked()"), self.inputTable.removeSportsmen)
  
  def drowTable(self):
    self.tableWidget_pare.insertRow(0)
    

