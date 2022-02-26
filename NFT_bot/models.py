from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TIMESTAMP

from datetime import datetime

Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=True)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

class User(CustomBase):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50)) #shadowaryan 
    chat_id = Column(Integer) #123456789
    collection = relationship('Collection',secondary = 'user_collection', back_populates='user')

class Collection(CustomBase):
    __tablename__ = 'collection'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    slug = Column(String(512))
    floor_price = Column(Float(10,5))
    user = relationship('User',secondary = 'user_collection', back_populates='collection')


class User_Collection(CustomBase):
    __tablename__ = 'user_collection'
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'),primary_key=True)

