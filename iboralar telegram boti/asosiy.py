from telegram.ext import ConversationHandler,CallbackQueryHandler
from methods import *

update=Updater(token='5509271062:AAHb_9cfMYs_uQtR8ATPH8WGgT7V_UDfaLk', use_context=True)
dispatcher=update.dispatcher


start_handler=CommandHandler('start',start)
inline = CallbackQueryHandler(inline_callback)
massage_handler=MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(massage_handler)
dispatcher.add_handler(inline)

update.start_polling()
