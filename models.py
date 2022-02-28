from urllib import response
from sqlalchemy import INTEGER, Column, Integer, String, Sequence, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TIMESTAMP

from postgresql_json import JSON
from datetime import datetime


Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class User(CustomBase):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50)) #shadowaryan 
    chat_id = Column(Integer) #123456789
    collections = relationship('Collection', secondary = 'user_collection', back_populates='users')

class Collection(CustomBase):
    __tablename__ = 'collection'
    id = Column(Integer, Sequence('collection_id_seq'), primary_key=True)
    slug = Column(String(512))
    floor_price = Column(Float(10,5))
    count = Column(Float(10,5),nullable=False)

    users = relationship('User', secondary = 'user_collection', back_populates='collections')
    history = relationship('History', back_populates='collection')

class User_Collection(CustomBase):
    __tablename__ = 'user_collection'
    id = Column(Integer, Sequence('user_collection_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    collection_id = Column(Integer, ForeignKey('collection.id'))

class History(CustomBase):
    __tablename__ = 'history'
    id = Column(Integer,Sequence('history_id_seq'), primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'))
    collection = relationship('Collection', back_populates='history')
    one_day_volume = Column(Float(10,5),nullable=False)
    one_day_change = Column(Float(10,5),nullable=False)
    one_day_sales = Column(Float(10,5),nullable=False)
    one_day_average_price = Column(Float(10,5),nullable=False)
    seven_day_volume = Column(Float(10,5),nullable=False)
    seven_day_change = Column(Float(10,5),nullable=False)
    seven_day_sales = Column(Float(10,5),nullable=False)
    seven_day_average_price = Column(Float(10,5),nullable=False)
    thirty_day_volume = Column(Float(10,5),nullable=False)
    thirty_day_change = Column(Float(10,5),nullable=False)
    thirty_day_sales = Column(Float(10,5),nullable=False)
    thirty_day_average_price = Column(Float(10,5),nullable=False)
    total_volume = Column(Float(10,5),nullable=False)
    total_sales = Column(Float(10,5),nullable=False)
    total_supply = Column(Float(10,5),nullable=False)
    count = Column(Float(10,5),nullable=False)
    num_owners = Column(Float(10,5),nullable=False)
    average_price = Column(Float(10,5),nullable=False)
    num_reports = Column(Float(10,5),nullable=False)
    market_cap = Column(Float(10,5),nullable=False)
    floor_price = Column(Float(10,5),nullable=False)
    # response_json = Column(JSON)
 