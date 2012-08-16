#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
from sportsmen import *
# прототип главной формы
class MainForm(QtGui.QDialog):
  def __init__(self):
    super(MainForm, self).__init__()
    uic.loadUi("mainform.ui", self)
    # Рабочий пример связи одного виджета с другим
    #self.connect(self.tableWidget, QtCore.SIGNAL("cellActivated(int, int)"), self.label, QtCore.SLOT("clear()")) 
    #Рабочий пример связи сигнала и метода на питоне!
    #self.connect(self.tableWidget, QtCore.SIGNAL("cellActivated(int, int)"), self.setLabelText)
    self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.drowDiagram)
    #self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.sportsmenEdit)
    self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.newSportsmen)
  
  #def cellIsFilled(self, x, y):
    #cell = self.tableWidget.itemAt(x, y)
    #if cell == None or cell.text == "":
      #return(False)
    #else:
      #return(True)
  
  def rowIsFilled(self, row):
    rowList = list()
    for x in range(0, self.tableWidget.columnCount()):
      rowList.append(self.tableWidget.item(row, x).text())
    if "" in rowList:
      return(False)
    else:
      return(True)

  def sportsmenEdit(self, i, j):
    print("sportsmenEdit")
    
  def newSportsmen(self, i, j):
    if self.rowIsFilled(i):
      self.tableWidget.insertRow(self.tableWidget.rowCount())
      tmp = sportsmen([1,2,3,4,5,6,7])
      
  def drowDiagram(self):
    print("drowDiagram")
    #for i in self.tableWidget.rowCount():
      #for j in self.tableWidget.columnCount():
