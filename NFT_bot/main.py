from telegram import Update
from telegram.ext import *


TOKEN = '5221341356:AAF5D4OKX3rEHv5M3KvyY6Sg9caipj0ej-k'


def handle_message(update,context):
    message = update.message.text

    if message in ("Hi","Hii","hii","hello","Hello"):
        update.message.reply_text(f"{message}, there")
    else:
        update.message.reply_text("Invalid Text , use /help ")

    
def start (update, context):
    update.message.reply_text("""hello,welcome
    For more Commands use - /help""")

def help (update, context):
    update.message.reply_text("""
    Commands:
    /help - to view commands
    """)


updater = Updater(TOKEN)
disp = updater.dispatcher

disp.add_handler(CommandHandler("start", start))
disp.add_handler(CommandHandler("help", help))
disp.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling()
updater.idle