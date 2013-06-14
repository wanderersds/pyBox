#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, Qt
from sportsman import *

filter_map = [ [91, 999], #super_heavy 
               [81,  91], #heavy 
               [75,  81], #light_heavy 
               [69,  75], #middle 
               [64,  69], #welter 
               [60,  64], #light_welter
               [56,  60], #light
               [52,  56], #bantam
               [49,  52], #fly
               [46,  49], #light_fly
             ];

class abstractTable():

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

  def removeSportsman(self):
    pos = self.table.currentRow()
    if pos > -1:
      session.query(Sportsman).filter(Sportsman.num==pos).delete()
      self.table.removeRow(pos)
      next_sportsmans = session.query(Sportsman).order_by(Sportsman.num)[pos:]
      for next_man in next_sportsmans:
        next_man.num -1 
      session.add_all(next_sportsmans)

class inputTable(abstractTable):
  def __init__(self, table):
    self.table = table
    self.sportsmans = session.query(Sportsman)[:]
    for man in self.sportsmans:
      self.addSportsman(man)

  def showSportsman(self, pos, sportsman):
    pos = self.table.rowCount() - 1
    for i in range( len(keys) ):
      item = QtGui.QTableWidgetItem()
      item.setText( str( getattr(sportsman, keys[i]) or '' ) )
      self.table.setItem(pos, i, item)

  def editSportsman(self, i, j):
    man = session.query(Sportsman).filter(Sportsman.sportsman_id == i+1).first()
    if man:
      man.set(j, self.table.item(i, j).text())
      session.add(man)

    if self.rowIsFilled(i):
      self.addSportsman()

  def addSportsman(self, man = -1, pos = -1):
    if man == -1:
      man = Sportsman()
    if pos == -1:
      pos = self.table.rowCount()
    self.table.insertRow(pos)
    man.num = pos+1 

    self.showSportsman(pos, man)
    next_sportsmans = session.query(Sportsman).order_by(Sportsman.num)[pos:]
    for next_man in next_sportsmans:
      next_man.num +1 
    session.add_all(next_sportsmans + [man])

  def countByCategory(self):
    count_by_category = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for man in session.query(Sportsman):
      for category in range( len(count_by_category) ):
        if man.weight in range( *filter_map[ category ] ):
          count_by_category[ category ] +=1
    return count_by_category

class pareTable(abstractTable):
  current_rounds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  filter_index   = 0

  def __init__(self, table):
    self.table = table
    self.sportsmans = session.query(Sportsman)[:]
    for man in self.sportsmans:
      self.showSportsman(man)
    self.drow()

  def showSportsman(self, sportsman):
    full_name = QtGui.QTableWidgetItem()
    full_name_text = (sportsman.name or '') + ' ' + (sportsman.last_name or '')
    full_name.setText(full_name_text)

    if sportsman.winner:
      color = Qt.QColor(255, 0, 0, 127)
      brush = Qt.QBrush()
      brush.setColor(color)
      full_name.setForeground(brush)
    
    club = QtGui.QTableWidgetItem()
    club.setText(sportsman.club)
    
    num = sportsman.num
    if num % 2:
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(num / 2, 0, full_name)
        self.table.setItem(num / 2, 1, club)
    else:
        self.table.setItem(num / 2 - 1, 2, full_name)
        self.table.setItem(num / 2 - 1, 3, club)

  def drow(self, only_winners=-1):
    if only_winners == -1:
      only_winners = self.current_rounds[ self.filter_index ]


    if self.current_rounds[ self.filter_index ] == 0:
      for man in session.query(Sportsman).order_by(Sportsman.num):
        man.dropped = 0
        session.add(man)

    self.table.setRowCount(0)
    num = 1
    weight_filter = range( *filter_map[ self.filter_index ] )
    query = session.query(Sportsman).\
            order_by(Sportsman.num).\
            filter(Sportsman.weight.in_( weight_filter ))
    
    for man in query:
      if only_winners == 0 or man.winner:
        if self.current_rounds[ self.filter_index ] == 0 or man.dropped == 0:
          man.num = num
          num += 1
          session.add(man)
          self.showSportsman(man)
      else:
        man.num = 0
        man.dropped = 1


  def setWinner(self):
      row  = self.table.currentRow()
      column = self.table.currentColumn()
      weight_filter = range( *filter_map[ self.filter_index ] )
      if column > 1:
        column = 2
      else:
        column = 1
      winner_num = row * 2 + column

      if winner_num % 2:
        looser_num = winner_num + 1
      else:
        looser_num = winner_num - 1

      winner = session.query(Sportsman).\
                  filter(Sportsman.num==winner_num).\
                  filter(Sportsman.weight.in_( weight_filter )).\
                  first()
      if winner:
        winner.winner = 1
        session.add(winner)
      looser = session.query(Sportsman).\
                filter(Sportsman.num==looser_num).\
                filter(Sportsman.weight.in_( weight_filter )).\
                first()
      if looser:
        print(looser.name)

        looser.winner = 0
        looser.dropped = 1
        session.add(looser)

      self.drow(only_winners=0)