import telegram
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater
import logging

TOKEN = '1862015564:AAE48fZEwLRKgeSF681eP9pt7g_jcivn68U'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

welcome ="""
Hola amig@, este bot está en construccion. 😅

Los comandos actuales son:

1. /caps Frase -> FRASE

Cualquier otro mensaje será devuelto en forma de eco. 

El bot deberia tener un modo __inline__...

autor: @Flakula
"""
def start(update, context):
    logging.info("start")

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=welcome
        )


def echo(update, context):
    logging.info("echo")

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=update.message.text
        )


def caps(update, context):
    logging.info("caps")

    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=text_caps
        )


def inline_caps(update, context):
    logging.info("inline_caps")

    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update, context):
    logging.info("unknown")

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Sorry, I didn't understand that command."
    )

	
if __name__ == '__main__':
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    start_h           = CommandHandler('start', start)
    caps_h            = CommandHandler('caps', caps)
    echo_h            = MessageHandler(Filters.text & (~Filters.command), echo)
    inline_caps_h     = InlineQueryHandler(inline_caps)
    unknown_h         = MessageHandler(Filters.command, unknown)
    
    dispatcher.add_handler(start_h)
    dispatcher.add_handler(echo_h)
    dispatcher.add_handler(caps_h)
    dispatcher.add_handler(inline_caps_h)
    dispatcher.add_handler(unknown_h)

    print(bot.get_me())
    # updater.idle()
    updater.start_polling()
    # updater.stop() # para detenerlo