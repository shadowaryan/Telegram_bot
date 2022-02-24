from urllib import response
from flask import Response
from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import *
from uuid import uuid4
from models import *
from sqlalchemy.orm import *
import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import exists
import json

engine = create_engine('postgresql://spqqojmysvclhl:35e13032f8326f8b7908e52a75e65215a62437d5c0c618aaee8a14392405e188@ec2-52-204-14-80.compute-1.amazonaws.com:5432/d7jch8clhgaktb', echo=False)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()



TOKEN = '5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k'


#bot start command    
def start (update, context):

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
def collection_name(update, context):
    value = update.message.text.partition(' ')[2]
    update.message.reply_text(f"NFT Collection Name - {value}")
    res= 'https://api.opensea.io/collection/'+value+'/stats'
    response = requests.get(res)
    data = response.json()
    stats=data['stats']['floor_price']
    
    if response.status_code == 200:
        
        new_collection = Collection(floor_price=stats,slug=value)
        db_collection = session.query(Collection).filter_by(slug=value).first()
        
        if db_collection is None:
            session.add(new_collection)

        #for row in session.query(User, User.username).all():
        #    print(row.User, row.username)
        session.commit()
    else:
        update.message.reply_text('invalid input')
   

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
    dp.add_handler(CommandHandler("collection", collection_name))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    updater.start_polling()
    updater.idle()
