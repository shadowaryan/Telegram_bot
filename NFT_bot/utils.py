from models import *
from main import session
import requests


def get_collection_id(slug):
    collection = session.query(Collection).filter_by(slug=slug).first()
    if collection:
        return collection.id
    else:
        floor_price = requests.get(f'https://api.opensea.io/collection/{slug}/stats').json()['stats']['floor_price']
        collection = Collection(slug=slug, floor_price=floor_price)
        session.add(collection)
        session.commit()
        return collection.id