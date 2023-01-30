import os
import telebot
import openai
from telebot import types
from config import openai_api_key, BOT_API


openai.api_key = openai_api_key

# Bot Token obtained from BotFather
bot = telebot.TeleBot(BOT_API)

# Help information
help_msg_en = "Hi. This bot is just a way to communicate with Chat-GPT via OpnaAI API. You can find source code of this bot here: https://github.com/KirillovDV/ChatGPT_bot  \n If you have any questions, please contact @KirillovDV"
welcome_msg = "Hi, I'm a ChatGPT bot. Click the Info button to learn more about me. To start chatting with me, just send me any message."
switch_to_English_msg = 'Switch to English'
switch_to_Russian_msg = 'Переключиться на Русский язык'



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn_info = types.KeyboardButton('Info')
    itembtn_en = types.KeyboardButton(switch_to_English_msg)
    itembtn_ru = types.KeyboardButton(switch_to_Russian_msg)
    markup.add(itembtn_info)
    markup.add(itembtn_en)
    markup.add(itembtn_ru)
    bot.send_message(chat_id=message.chat.id, text=welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Info')
def send_help(message):
        bot.send_message(chat_id=message.chat.id, text=help_msg)

# функция для отправки сообщения в зависимости от языка
def send_message(message, lang="select en"):
    bot.send_message(chat_id=message.chat.id, text=texts[lang])

# обработчик команды на переключение языка
@bot.message_handler(commands=["switch_lang"])
def switch_language(message):
    if message.text == "/switch_lang en":
        send_message(message, switch_to_English_msg)
    elif message.text == "/switch_lang ru":
        send_message(message, switch_to_Russian_msg)
    else:
        bot.send_message(chat_id=message.chat.id, text="Language not supported \n Язык не поддерживается")








@bot.message_handler(func=lambda message: message.text == 'Info')
def send_help(message):
        bot.send_message(chat_id=message.chat.id, text=help_msg_en)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Bot: ' + message.text,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    bot.send_message(chat_id=message.chat.id, text=response)

bot.polling()
