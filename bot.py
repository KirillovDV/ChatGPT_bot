import os
import telebot
import openai
from telebot import types
from config import openai_api_key, BOT_API


openai.api_key = openai_api_key

# Bot Token obtained from BotFather
bot = telebot.TeleBot(BOT_API)

# Help information
help_text = "Hi. This bot is just a way to communicate with Chat-GPT via OpnaAI API. You can find source code of this bot here: https://github.com/KirillovDV/ChatGPT_bot  \n If you have any questions, please contact @KirillovDV"

# Handling messages from Telegram users
@bot.message_handler(content_types=['text'])
def handle_message(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Bot: ' + message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    markup = types.InlineKeyboardMarkup()
    itembtn = types.InlineKeyboardButton('Help', callback_data='help')
    markup.add(itembtn)
    bot.send_message(chat_id=message.chat.id, text=response, reply_markup=markup)

# Handling inline buttons
@bot.callback_query_handler(func=lambda call: call.data == 'help')
def callback_help(call):
    bot.send_message(chat_id=call.message.chat.id, text=help_text)

# Starting bot
bot.polling()
