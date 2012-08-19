#!/usr/bin/env python
# -*- coding: utf-8 -*-

Sportsmens = list()

class sportsmen():
  def __init__(self, dataList = ["", "", "", "", "", "", ""], pos = len(Sportsmens)):
    self.name, self.last_name, self.trainer, self.born, self.weight, self.category, self.club = dataList
    Sportsmens.insert(pos, self)
  
  def correct(self, dataList):
    self.name, self.last_name, self.trainer, self.born, self.weight, self.category, self.club = dataList

  
class fight():
  
  def __init__(self, a = []):
    if a:
      self.a = a
    #self.b = b
    
  def setWinner(winner):
    self.winner = winner




  
