from itertools import count
from models import *
import requests
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql://spqqojmysvclhl:35e13032f8326f8b7908e52a75e65215a62437d5c0c618aaee8a14392405e188@ec2-52-204-14-80.compute-1.amazonaws.com:5432/d7jch8clhgaktb', echo=False)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

def get_collection_id(slug):
    collection = session.query(Collection).filter_by(slug=slug).first()
    if collection:
        return collection.id
    else:
        resp = requests.get(f'https://api.opensea.io/collection/{slug}/stats').json()['stats']
        floor_price = resp['floor_price']
        count = resp['count']
        print(count)
        collection = Collection(slug=slug, floor_price=floor_price,count=count)
        session.add(collection)
        session.commit()
        return collection.id