from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import *
from uuid import uuid4

TOKEN = '5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k'


def handle_message(update,context):
    message = update.message.text

    if message in ("Hi","Hii","hii","hello","Hello"):
        update.message.reply_text(f"{message}, there")
   # else:
    #    update.message.reply_text("Invalid Text , use /help ")

    
def start (update, context):
    update.message.reply_text("""hello,welcome
   For more Commands use - /help""")

def help (update, context):
    update.message.reply_text("""
    Commands:
    /help - to view commands
    """)

def get_link(update, context):
    value = update.message.text.partition(' ')[2]
    update.message.reply_text(f"LINK GIVEN BY YOU - {value}")


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
    dp.add_handler(CommandHandler("link", get_link))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    
    #dp.add_handler(CommandHandler('put', put))
    #dp.add_handler(CommandHandler('get', get))

    updater.start_polling()
    updater.idle()




'''

from uuid import uuid4
from telegram.ext import Updater, CommandHandler

def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = value
    # Send the key to the user
    update.message.reply_text(key)

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
    print("sad") 
    dp.add_handler(CommandHandler('put', put))
    dp.add_handler(CommandHandler('get', get))

    updater.start_polling()
    updater.idle()

   '''