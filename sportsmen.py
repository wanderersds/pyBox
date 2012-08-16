#!/usr/bin/env python
# -*- coding: utf-8 -*-

Sportsmens = list()

class sportsmen():
  def __init__(self, dataList):
    self.name, self.last_name, self.trainer, self.born, self.weight, self.category, self.club = dataList
    Sportsmens.append(self)
  
class fight():
  a = ""
  b = ""
  winner = ""
  
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
  def setWinner(winner):
    self.winner = winner




  
