import subprocess
import sys
import threading
import time

import telebot

TOKEN = sys.argv[1]
print(TOKEN)

global counter
counter = 0

bot = telebot.TeleBot(TOKEN)


def say(msg):
    def run_sub(msg):
        global counter
        counter += 1
        subprocess.run(["python3", "Speeker.py", msg, str(counter)])

    x = threading.Thread(target=run_sub, args=(msg,))
    x.start()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    say('Привет')

    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    say(msg)

    bot.send_message(message.chat.id, "Сказано: \"{}\"".format(msg))


def run():
    print("Started...")
    while True:
        try:
            bot.polling()
        except Exception as e:
            print("Exception polling")
            time.sleep(15)


if __name__ == "__main__":
    run()
