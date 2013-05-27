#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, Qt
from sportsman import *

class abstractTable():

  def __init__(self, table):
    self.table = table
    self.sportsmans = session.query(Sportsman)[:]
    for man in self.sportsmans:
      self.addSportsman(man)

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

  def editSportsman(self, i, j):
    man = session.query(Sportsman).filter(Sportsman.num == i+1).first()
    man.set(j, self.table.item(i, j).text())
    session.add(man)

    if self.rowIsFilled(i):
      self.addSportsman()

    flush()
      
  def addSportsman(self, man = -1, pos = -1): #NameError: name 'self' is not defined
    if man == -1:
      man = Sportsman() #FTW???
    if pos == -1:
      pos = self.table.rowCount()
    self.table.insertRow(pos)
    man.num = pos+1 

    self.showSportsman(pos, man)
    next_sportsmans = session.query(Sportsman).order_by(Sportsman.num)[pos:]
    for next_man in next_sportsmans:
      next_man.num +1 
    next_sportsmans.append(man)
    session.add_all(next_sportsmans)  
    flush()
    
  def removeSportsman(self):
    row = self.table.currentRow()
    if row > -1:
      self.table.removeRow(row)
      session.query(Sportsman).filter(Sportsman.num==row).delete()

      for instance in session.query(Sportsman).order_by(Sportsman.num)[row:]:
        instance.num -1      

    flush()

class inputTable(abstractTable):
  def showSportsman(self, pos, sportsman):
    pos = self.table.rowCount() - 1
    for i in range( len(keys) ):
      item = QtGui.QTableWidgetItem()
      item.setText( str( getattr(sportsman, keys[i]) or '' ) )
      self.table.setItem(pos, i, item)

class pareTable(abstractTable):
  def showSportsman(self, pos, sportsman):
    full_name = QtGui.QTableWidgetItem()
    full_name_text = (sportsman.name or '') + ' ' + (sportsman.last_name or '')
    full_name.setText(full_name_text)
    
    club = QtGui.QTableWidgetItem()
    club.setText(sportsman.club)

    num = sportsman.num
    if num % 2:
        self.table.setItem(num / 2, 0, full_name)
        self.table.setItem(num / 2, 1, club)
    else:
        self.table.setItem(num / 2 - 1, 2, full_name)
        self.table.setItem(num / 2 - 1, 3, club)

  def drow(self):
    self.clear()
    for instance in session.query(Sportsman).order_by(Sportsman.num):
      self.addSportsman(instance)


  def setWinner(self):
      color = Qt.QColor(255, 0, 0, 127)
      brush = Qt.QBrush()
      brush.setColor(color)
      self.table.currentItem().setForeground(brush)
