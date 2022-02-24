from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import *
from uuid import uuid4
from models import *
from sqlalchemy.orm import *
import requests
from sqlalchemy import create_engine

engine = create_engine('postgresql://spqqojmysvclhl:35e13032f8326f8b7908e52a75e65215a62437d5c0c618aaee8a14392405e188@ec2-52-204-14-80.compute-1.amazonaws.com:5432/d7jch8clhgaktb', echo=True)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()



TOKEN = '5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k'

#message handling command
def handle_message(update,context):
    message = update.message.text
    print(update.effective_user.id)
    print(update.effective_user.username)
    if message in ("Hi","Hii","hii","hello","Hello"):
        update.message.reply_text(f"{message}, there")
    else:
        update.message.reply_text("Invalid Text , use /help ")


#bot start command    
def start (update, context):
    update.message.reply_text("""hello,welcome
   For more Commands use - /help""")

#bot help command
def help (update, context):
    update.message.reply_text("""
    Commands:
    /help - to view commands
    /collection - write the nft collection name 
    """)

#chat id function
def chat_id_(update, context):
    id_value=update.effective_user.id
    return id_value

def username_id(update, context):
    username_value=update.effective_user.username
    return username_value

#get link bot command
def collection_name(update, context):
    value = update.message.text.partition(' ')[2]
    update.message.reply_text(f"LINK GIVEN BY YOU - {value}")
    response = requests.get(value)
    
    if response.status_code == True:

        main_chat_id = chat_id_(update, context)
        new_chat_id = User(chat_id=main_chat_id)
        db_chat_id = session.query(User).filter_by(chat_id=main_chat_id).first()
        if new_chat_id not in db_chat_id:
            session.add(new_chat_id)

        main_username_id = username_id(update, context)
        new_username_id = User(username=main_username_id)
        db_username_id = session.query(User).filter_by(username=main_username_id).first()
        if new_username_id not in db_username_id:
            session.add(new_username_id)

        
        new_collection = Collection(slug=value)
        db_collection = session.query(Collection).filter_by(slug=value).first()
        if new_collection not in db_collection:
            session.add(new_collection)

        #for row in session.query(User, User.username).all():
        #    print(row.User, row.username)
        session.commit()


    else:
        update.message.reply_text('which is invalid or not a link please try other link')
   
    
    
  
    

#database handling
def db_fun(update, context):
    main_id = chat_id_(update, context)
    ed_user = User(username='ed')
    our_user = session.query(User).filter_by(name='ed').first()
    
    if ed_user not in our_user:
        session.add(ed_user)

    ed_collection = Collection(Collection_link='random')

    our_collection = session.query(Collection).filter_by(Collection_link='ed').first()
    
    if ed_collection not in our_collection:
        session.add(ed_collection)

    #for row in session.query(User, User.username).all():
    #    print(row.User, row.username)
    session.commit()


'''def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = value
    # Send the key to the user
    update.message.reply_text(key)
'''


def get(update, context):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = context.args[0]

    # Load value and send it to the user
    value = context.user_data.get(key, 'Not found')
    update.message.reply_text(value)




if __name__ == '__main__':
    updater = Updater('5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k', use_context=True)
    dp = updater.dispatcher
    print("started")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("collection", collection_name))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    
    #dp.add_handler(CommandHandler('put', put))
    #dp.add_handler(CommandHandler('get', get))

    updater.start_polling()
    updater.idle()
