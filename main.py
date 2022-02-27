from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from uuid import uuid4
from models import *
from sqlalchemy.orm import Session, sessionmaker
import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import exists
import json

from utils import get_collection_id

# def get_collection_id(slug):
#     collection = session.query(Collection).filter_by(slug=slug).first()
#     if collection:
#         return collection.id
#     else:
#         floor_price = requests.get(f'https://api.opensea.io/collection/{slug}/stats').json()['stats']['floor_price']
#         collection = Collection(slug=slug, floor_price=floor_price)
#         session.add(collection)
#         session.commit()
#         return collection.id



engine = create_engine('postgresql://spqqojmysvclhl:35e13032f8326f8b7908e52a75e65215a62437d5c0c618aaee8a14392405e188@ec2-52-204-14-80.compute-1.amazonaws.com:5432/d7jch8clhgaktb', echo=False)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()



TOKEN = '5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k'


#bot start command    
def start(update, context):

    update.message.reply_text("""hello,welcome
    For more Commands use - /help""")

    user_chat_id = update.effective_user.id

    user = User(username=update.effective_user.username,chat_id=user_chat_id)
    # db_chat_id = session.query(User).filter_by(chat_id=user_chat_id).first()

    if not session.query(session.query(User).filter_by(chat_id=user_chat_id).exists()).scalar():
        session.add(user)
        print('done')

    
    session.commit()
   


#bot help command
def help (update, context):
    update.message.reply_text("""
    Commands:
    /help - to view commands
    /add_collection <YOUR_COLLECTION_NAME> - to add collection
    """)

        
#bot command to get collection data 
def add_collection(update, context):
    url = update.message.text.partition(' ')[2]
    slug = url.split('/')[-1]
    update.message.reply_text(f"NFT Collection Name - {slug}")
    
    # floor_price = response_json['stats']['floor_price']
    
    # if response.status_code == 200:
    user = session.query(User).filter_by(chat_id=update.effective_user.id).first()
    collection_id = get_collection_id(slug)
    #db_collection = session.query(Collection).filter_by(slug=slug).first()
    resp = requests.get(f'https://api.opensea.io/collection/{slug}/stats').json()['stats']

    if not session.query(session.query(Collection, User).filter(User_Collection.collection_id==collection_id, User_Collection.user_id==user.id).exists()).scalar():
        collection = session.query(Collection).filter_by(id=collection_id).first()
        user.collection.append(collection)
        print('hello')
        History(resp)
        session.commit()
    else:
        update.message.reply_text("invaild text")

def History(**kwargs):
    for key,value in kwargs.items():
        stats = History(key=value)
        session.add(stats)
        session.commit()




    # res = f'https://api.opensea.io/collection/{slug}/stats'
    # response = requests.get(res)
    # response_data = response.json()
    # response_json = response_data['stats'] 
    # #for x in 

# res = 'https://api.opensea.io/collection/lostpoets/stats'
# response = requests.get(res)
# response_data = response.json()
# response_json = response_data['stats'] 
# session.query(History_Collection).filter_by(response_json=**kwargs).first() 



#message handling command
def handle_message(update,context):
    message = update.message.text
    print(update.effective_user.id)
    print(update.effective_user.username)
    if message in ("Hi","Hii","hii","hello","Hello"):
        update.message.reply_text(f"{message}, there")
    else:
        update.message.reply_text("Invalid Text , use /help ")


if __name__ == '__main__':
    updater = Updater('5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k', use_context=True)
    dp = updater.dispatcher
    print("started")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("add_collection", add_collection))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    updater.start_polling()
    updater.idle()


