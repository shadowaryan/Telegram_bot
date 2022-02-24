from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50)) #shadowaryan 
    chat_id = Column(Integer) #123456789
    collections = relationship('Collection',secondary = 'user_collection', back_populates='user')

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    slug = Column(String(512))
    users = relationship('User',secondary = 'user_collection', back_populates='collection')


class User_Collection(Base):
    __tablename__ = 'user_collection'
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'),primary_key=True)

print('hii')
'''
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    collections = relationship('Collection',secondary = 'user_collection', back_populates='user')

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(512))
    #slug = 
    users = relationship('User',secondary = 'user_collection', back_populates='collection')


class User_collection(Base):
    __tablename__ = 'user_collection'
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'),primary_key=True)
'''