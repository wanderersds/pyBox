#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wanderer'
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

keys = [ "name", "last_name", "club", "weight", "trainer", "born", "category", "year" ]
    
Base = declarative_base()

class Sportsman(Base):
    __tablename__ = 'sportsmans'
    sportsman_id = Column(Integer, primary_key=True, nullable=False)
    name         = Column(String(30), nullable=False, default='')
    last_name    = Column(String(30), nullable=False, default='')
    trainer      = Column(String(30), nullable=False, default='')
    born         = Column(String(4), nullable=False, default='')
    weight       = Column(String(3), nullable=False, default='')
    category     = Column(String(10), nullable=False, default='')
    club         = Column(String(30), nullable=False, default='')
    year         = Column(Integer, nullable=False, default='')
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

def flush():
    session.commit()
    session.flush()