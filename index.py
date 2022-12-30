from pyChatGPT import ChatGPT #pip install -U pyChatGPT 
# pip install python-telegram-bot --upgrade
# pip install ffmpeg_downloader PyPasser pocketsphinx
# _mr_bot_007
# mr_bot_221B

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


telegram_token = 'telegram_token'
api = ChatGPT(auth_type='openai', email='your_email', password='your_pass')

# resp = api.send_message('Hello, world!')
# print(resp['message'])

updater = Updater(telegram_token, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the ChatGPT-Bot.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Talk to the bot!""")

def unknown_text(update: Update, context: CallbackContext):
    resp = api.send_message(update.message.text)
    update.message.reply_text(resp['message'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
