#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from sportsmen import *

class abstractTable():

  def __init__(self, table):
    self.table = table
    self.sportsmens = list()
    if table.rowCount() == 0:
      self.addSportsmen()
  
  def clear(self):
    self.table.setRowCount(0)
    del self.sportsmens[:]
  
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
    
  def showSportsmen(self, pos, sportsmen):
    pass
    
  def editSportsmen(self, i, j):
    self.sportsmens[i][keys[j]] = self.table.item(i, j).text()
    print(self.sportsmens[i])
    if self.rowIsFilled(i):
      self.addSportsmen()
      
  def addSportsmen(self, man = -1, pos = -1): #NameError: name 'self' is not defined
    if man == -1:
      man = sportsmen() #FTW???
    if pos == -1:
      pos = self.table.rowCount()
    self.table.insertRow(pos)
    self.showSportsmen(pos, man)
    self.sportsmens.insert(pos, man)
    
  def removeSportsmen(self):
    row = self.table.currentRow()
    if row > -1:
      self.table.removeRow(row)
      del self.sportsmens[row]
      
      
class inputTable(abstractTable):
  pass

class pareTable(abstractTable):
  def showSportsmen(self, pos, sportsmen):
    name = QtGui.QTableWidgetItem()
    name.setText(sportsmen["name"])
    last_name = QtGui.QTableWidgetItem()
    last_name.setText(sportsmen["last_name"])
    self.table.setItem(pos, 0, name)
    self.table.setItem(pos, 1, last_name)