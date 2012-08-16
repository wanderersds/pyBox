#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
from sportsmen import *
# прототип главной формы

class MainForm(QtGui.QMainWindow):
  def __init__(self):
    super(MainForm, self).__init__()
    uic.loadUi("mainform.ui", self)
    # Рабочий пример связи одного виджета с другим
    #self.connect(self.tableWidget, QtCore.SIGNAL("cellActivated(int, int)"), self.label, QtCore.SLOT("clear()")) 
    #Рабочий пример связи сигнала и метода на питоне!
    #self.connect(self.tableWidget, QtCore.SIGNAL("cellActivated(int, int)"), self.setLabelText)
    self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.drowDiagram)
    self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.sportsmenEdit)
    self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.newSportsmen)
    first = sportsmen(self.rowToList(0))
    
  def getText(self, x, y):
    try:
      return(self.tableWidget.item(x, y).text())
    except AttributeError:
      return("")
  
  def rowIsFilled(self, row):
    if "" in self.rowToList(row):
      return(False)
    else:
      return(True)

  def sportsmenEdit(self, i, j):
    Sportsmens[i].correct(self.rowToList(i))
    print(Sportsmens, i, self.rowToList(i))
  
  def rowToList(self, row):
    rowList = list()
    for x in range(0, self.tableWidget.columnCount()):
      rowList.append(self.getText(row, x))
    return(rowList)
  
  def newSportsmen(self, i, j):
    if self.rowIsFilled(i):
      self.tableWidget.insertRow(self.tableWidget.rowCount())
      tmp = sportsmen(self.rowToList(i+1))
      
  def drowDiagram(self):
    print("drowDiagram")
    #for i in self.tableWidget.rowCount():
      #for j in self.tableWidget.columnCount():
