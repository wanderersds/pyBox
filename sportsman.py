#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wanderer'
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

keys = ["name", "last_name", "trainer", "born", "weight", "category", "club", "num"]
    
def sportsman():
  return {}.fromkeys(keys, "")

Base = declarative_base()

class Sportsman(Base):
    __tablename__ = 'sportsmans'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(30))
    trainer = Column(String(30))
    born = Column(String(4))
    weight = Column(String(3))
    category = Column(String(10))
    club = Column(String(30))
    num = Column(Integer)
