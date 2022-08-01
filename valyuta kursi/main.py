from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler,Filters,ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
import requests

btn2 = ReplyKeyboardMarkup([
    ['Uz','Ru','Eng']
    
],resize_keyboard=True)

b = {
    'lang':'',
    
}
a=str()
lan=''
btn = InlineKeyboardMarkup([ 
    [InlineKeyboardButton('UZS ⏩ RUB',callback_data='UZS-RUB'),
    InlineKeyboardButton('RUB ⏩ UZS',callback_data='RUB-UZS')],

    [InlineKeyboardButton('UZS ⏩ EUR',callback_data='UZS-EUR'),
    InlineKeyboardButton('EUR ⏩ UZS',callback_data='EUR-UZS')],

    [InlineKeyboardButton('UZS ⏩ USD',callback_data='UZS-USD'),
    InlineKeyboardButton('USD ⏩ UZS',callback_data='USD-UZS')],
    
])

STATE_LANG=1
STATE_BUTTON=2
STATE_CHANE=3


def start(up,ct):
    up.message.reply_text('Salom Tilni Tanlang', reply_markup=btn2)
    return STATE_LANG

def uzb(up,ct):
    up.message.reply_text('Assalomu alykum', reply_markup=ReplyKeyboardRemove())
    up.message.reply_text(' Valyutalar Kursini Botiga Hush Kelibsiz', reply_markup=btn)
    global lan
    lan='uz'
    return STATE_BUTTON

def ru(up,ct):
    up.message.reply_text('Привет и добро пожаловать в обменный курс', reply_markup=btn)
    global lan
    lan='ru'
    return STATE_BUTTON
    

def eng(up,ct):
    up.message.reply_text('Hello and welcome to the Exchange Rate', reply_markup=btn)
    global lan
    lan='eng'
    return STATE_BUTTON






def course(up,ct):
    global a, lan
    print(a)
    query = up.callback_query
    if query.data=="UZS-RUB":
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kiriting')
            a='UZS-RUB'
            print(a)
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='UZS-RUB'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='UZS-RUB'
            return STATE_CHANE

    elif query.data=='RUB-UZS':
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kriting')
            a='RUB-UZS'
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='RUB-UZS'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='RUB-UZS'
            return STATE_CHANE


    elif query.data=="UZS-EUR":
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kiriting')
            a='UZS-EUR'
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='UZS-EUR'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='UZS-EUR'
            return STATE_CHANE
    elif query.data=='EUR-UZS':
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kiriting')
            a='EUR-UZS'
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='EUR-UZS'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='EUR-UZS'
            return STATE_CHANE


    elif query.data=="UZS-USD":
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kiriting')
            a='UZS-USD'
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='UZS-USD'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='UZS-USD'
            return STATE_CHANE
    elif query.data=='USD-UZS':
        if lan=='uz':
            ct.bot.send_message(up.callback_query.message.chat.id,'Summani Kiriting')
            a='USD-UZS'
            return STATE_CHANE
        elif lan=='ru':
            ct.bot.send_message(up.callback_query.message.chat.id,'Введите сумму')
            a='USD-UZS'
            return STATE_CHANE
        elif lan=='eng':
            ct.bot.send_message(up.callback_query.message.chat.id,'Enter the amount')
            a='USD-UZS'
            return STATE_CHANE

def change(up,ct):
    try:
        summa = float(up.message.text)
        if a=='UZS-RUB':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/UZS'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['RUB']*summa)
        elif a=='RUB-UZS':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/RUB'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['UZS']*summa)


        elif a=='UZS-EUR':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/UZS'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['EUR']*summa)
        elif a=='EUR-UZS':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/EUR'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['UZS']*summa)


        elif a=='UZS-USD':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/UZS'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['USD']*summa)
        elif a=='USD-UZS':
            url = 'https://v6.exchangerate-api.com/v6/97fc9e643e60e7d4dcc9f621/latest/USD'
            response = requests.get(url)
            data = response.json()
            up.message.reply_text(data['conversion_rates']['UZS']*summa)
    except:
           up.message.reply_text('Raqam Kriting')

    


    
def main():
    updater = Updater("5598607839:AAFwEa_RVx1OhwWBws6Fo40rf0LCD8Q7bfk")
    dp= updater.dispatcher
    conv_hand= ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            STATE_LANG:[
            MessageHandler(Filters.regex('Uz'),uzb),
            MessageHandler(Filters.regex('Ru'),ru),
            MessageHandler(Filters.regex('Eng'),eng),
            ],
            STATE_BUTTON:[
              CallbackQueryHandler(course)
            ],
            STATE_CHANE:[
                CallbackQueryHandler(course),
                CommandHandler('start',start),
                MessageHandler(Filters.text,change),

            ]

           },
           fallbacks=[CommandHandler('start',start)]
    )
    dp.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()

main()