#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sportsmen import *

class table():
  
  sportsmens = list()

  def __init__(self, table):
    self.table = table
    if table.rowCount() == 0:
      self.addSportsmen()

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
    
  def editSportsmen(self, i):
    self.sportsmens[i].correct(self.rowToList(i))
    if self.rowIsFilled(i):
      self.addSportsmen()
    print(self.sportsmens, i, self.rowToList(i)) #Debug
    
  def addSportsmen(self, pos = -1): #NameError: name 'self' is not defined
    if pos == -1:
      pos = self.table.rowCount()
    self.table.insertRow(pos)
    self.sportsmens.insert(pos, sportsmen())
    
  def removeSportsmen(self):
    row = self.table.currentRow()
    if row > -1:
      self.table.removeRow(row)
      del self.sportsmens[row]