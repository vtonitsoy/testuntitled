import telebot
import config
import re
from telebot import types
from datetime import datetime	

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Добро пожаловать! Я упрощу твою жизнь.")

@bot.message_handler(content_types=['text'])

def func(message):
	string = message.text + ' '
	newstring =''
	i=0
	j=1
	while (i<len(string)) and (j<len(string)):
		newstring+=string[i].lower()
		i=i+2
		newstring+=string[j].upper()
		j=j+2
	

	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M:%S - %b %d %Y")
	f = open("logs.txt", "a")
	f.write('Chat user - t.me/'+message.from_user.username+' '+timestampStr+'\n')
	f.close()
	bot.send_message(message.chat.id, newstring)




@bot.inline_handler(func=lambda query: len(query.query) > 0)

def query_text(query):
    string = query.query + ' '
    newquerystr =''
    i=0
    j=1
    while (i<len(string)) and (j<len(string)):
    	newquerystr+=string[i].lower()
    	i=i+2
    	newquerystr+=string[j].upper()
    	j=j+2
    outpt = types.InlineQueryResultArticle(
            id='1', title="Пляскашрифт",
            description=newquerystr,
            input_message_content=types.InputTextMessageContent(
            message_text=newquerystr)
    )

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%H:%M:%S - %b %d %Y")
    fl = open("logs.txt", "a")
    fl.write('Inline user '+timestampStr+'\n')
    fl.close()
    bot.answer_inline_query(query.id, [outpt], cache_time=1)


#RUN
bot.polling(none_stop=True)