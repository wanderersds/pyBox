#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wanderer'
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

keys = ["name", "last_name", "trainer", "born", "weight", "category", "club", "num"]
    
Base = declarative_base()

class Sportsman(Base):
    __tablename__ = 'sportsmans'
    sportsman_id = Column(Integer, primary_key=True)
    name         = Column(String(30))
    last_name    = Column(String(30))
    trainer      = Column(String(30))
    born         = Column(String(4))
    weight       = Column(String(3))    
    category     = Column(String(10))
    club         = Column(String(30))
    year         = Column(Integer)
    num          = Column(Integer) #, unique=True, autoincrement=True, nullable=False)
    
    def set(self, num, entry ):
        if num == 0: self.name      = entry
        if num == 1: self.last_name = entry   
        if num == 2: self.club      = entry 
        if num == 3: self.weight    = entry  
        if num == 4: self.trainer   = entry    
        if num == 5: self.born      = entry   
        if num == 6: self.category  = entry 
        if num == 7: self.year      = entry 
        # if num == : self.num       = entry 

# db_engine = create_engine('postgresql:///pyBox.db', echo=True)
db_engine = create_engine('sqlite:///pyBox.db', echo=False)
Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()