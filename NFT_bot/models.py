from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    collections = relationship('Collection',secondary = 'link', back_populates='user')

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    collection_link = Column(String(512))
    users = relationship('User',secondary = 'link', back_populates='collection')


class Link(Base):
    __tablename__ = 'link'
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'),primary_key=True)
