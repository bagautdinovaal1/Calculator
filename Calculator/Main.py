import telebot
import telepot as telepot
from telepot.loop import MessageLoop

TOKEN = 'token'
bot = telepot.Bot(TOKEN)

START_MESSAGE = "Это калькулятор /nНачните вводить пример  "

def handle(msg):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Я не знаю что это"
    bot.sendMessage(chat_id, "answer: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break