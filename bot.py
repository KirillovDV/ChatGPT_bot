import os
import telebot
import openai
from telebot import types
from config import openai_api_key, BOT_API


openai.api_key = openai_api_key

# Bot Token obtained from BotFather
bot = telebot.TeleBot(BOT_API)

# Help information
help_msg= "Hi. This bot is just a way to communicate with Chat-GPT via OpnaAI API. You can find source code of this bot here: https://github.com/KirillovDV/ChatGPT_bot  \n If you have any questions, please contact @KirillovDV"
welcome_msg = "Hi, I'm a ChatGPT bot. Click the Info button to learn more about me. To start chatting with me, just send me any message."



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('Info')
    markup.add(itembtn1)
    bot.send_message(chat_id=message.chat.id, text=welcome_msg, reply_markup=markup)




@bot.message_handler(func=lambda message: message.text == 'Info')
def send_help(message):
        bot.send_message(chat_id=message.chat.id, text=help_msg)

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
