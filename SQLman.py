__author__ = 'wanderer'
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
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

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)