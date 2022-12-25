import telebot
import model
import abc_key

bot = telebot.TeleBot(abc_key.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введи текст, где вычеркнуть абв")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, model.abc_del(message.text))
print('Server run')
bot.infinity_polling()