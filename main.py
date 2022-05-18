#Para probar el bot debera descargar este archivo, ejecutarlo en PyCharm y luego abrir la app de telegram y
#escribir "/help" o "/custom" o "/start". De momento esta configurado con tres unicos comandos.

import logging
from telegram.ext import *
import responses

API_KEY ='5210490820:AAE7CoOEf3EiyxLEgy1w4qCIO0xQvEzdXDQ'

#SetUp Loggin
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def start_commadn(update, context):
    update.message.reply_text('Hello! I am a bot!')

def help_commadn(update, context):
    update.message.reply_text('Don\'t worry, I am for help you. Tell me your problem.')

def custom_commadn(update, context):
    update.message.reply_text('Can i help you in any way?')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'({update.message.chat.id}) says: {text}')

    #Bot repsonde
    update.message.reply_text(text)

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__' :
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_commadn))
    dp.add_handler(CommandHandler('custom', custom_commadn))
    dp.add_handler(CommandHandler('help', help_commadn))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling(0)
    updater.idle()