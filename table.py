#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, Qt
from sportsman import *

class abstractTable():

  def __init__(self, table):
    self.table = table
    self.sportsmans = list()
    if table.rowCount() == 0:
      self.addSportsman()
  
  def clear(self):
    self.table.setRowCount(0)
    del self.sportsmans[:]
  
  def getText(self, x, y):
    try:
      return(self.table.item(x, y).text())
    except AttributeError:
      return("")
      
  def rowIsFilled(self, row):
    if "" in self.rowToList(row):
      return(False)
    else:
      return(True)
      
  def rowToList(self, row):
    rowList = list()
    for x in range(0, self.table.columnCount()):
      rowList.append(self.getText(row, x))
    return(rowList)

  def showSportsman(self, pos, sportsman):
    pass
    
  def editSportsman(self, i, j):
    self.sportsmans[i][keys[j]] = self.table.item(i, j).text()
    print(self.sportsmans[i])
    if self.rowIsFilled(i):
      self.addSportsman()
      
  def addSportsman(self, man = -1, pos = -1): #NameError: name 'self' is not defined
    if man == -1:
      man = sportsman() #FTW???
    if pos == -1:
      pos = self.table.rowCount()
    self.table.insertRow(pos)
    man["num"] = pos+1
    self.showSportsman(pos, man)
    self.sportsmans.insert(pos, man)

#    for i in len(self.sportsmans) - pos:
#      self.sportsmans[i]["num"]+1
    
  def removeSportsman(self):
    row = self.table.currentRow()
    if row > -1:
      self.table.removeRow(row)
      del self.sportsmans[row]

    for i in self.sportsmans[row:]:
      i["num"]-1
      
      
class inputTable(abstractTable):
  pass

class pareTable(abstractTable):
  def showSportsman(self, pos, sportsman):
    name = QtGui.QTableWidgetItem()
    name.setText(sportsman["name"])
    last_name = QtGui.QTableWidgetItem()
    last_name.setText(sportsman["last_name"])

    num = sportsman["num"]
    if num % 2:
        self.table.setItem(num / 2, 0, name)
        self.table.setItem(num / 2, 1, last_name)
    else:
        self.table.setItem(num / 2 - 1, 2, name)
        self.table.setItem(num / 2 - 1, 3, last_name)

  def __init__(self, table):
      super().__init__(table)


  def setWinner(self):
      color = Qt.QColor(255, 0, 0, 127)
      brush = Qt.QBrush()
      brush.setColor(color)
      self.table.currentItem().setForeground(brush)
