import telebot
import os
import time
from keep_alive import keep_alive

bot_token = BOT_TOKEN
bot = telebot.TeleBot(bot_token)


def brain(code):
    lines = code
    lines.insert(0, "import sys")
    lines.insert(1, "sys.stdout = open('output.txt', 'w')")
    lines.insert(2, "try:")
    lines.append('except:')
    lines.append('    print("Error")')

    for i in range(3, len(lines) - 2):
        lines[i] = '    ' + lines[i]
    code_to_run = '\n'.join(lines)

    with open('code.py', 'w+') as f:
        f.write(code_to_run)

    os.system('python code.py')

    f = open('output.txt', 'r')
    return f.read()


@bot.message_handler(commands=['start'])
def welcome_user(msg):
    bot.reply_to(msg, "Hi, my name is 01000101!\nwhat is my purpose in life?, user.")


@bot.message_handler(commands=['why_donate'])
def convence_user(msg):
    bot.reply_to(msg, "Why should you donate?\n•To help me feed my secret wife and 4 children.\n"
                 + "•So I can upgrade this bot's host to br more practical  for large number of users.\n"
                 + "•to help me add more features , patches and more upgrades to this bot and build other ones.\n"
                 + "•Give me your money, thank you!❤️❤️ ")


@bot.message_handler(commands=['donate'])
def get_user_donation(msg):
    bot.reply_to(msg, "This part hasn't been implemented yet,as this is the beta version, thank you!")


@bot.message_handler(commands=['info'])
def send_info(msg):
    bot.reply_to(msg, "This part hasn't been implemented yet.")


@bot.message_handler(commands=['help'])
def help_user(msg):
    bot.reply_to(msg, "This part hasn't been implemented yet.")


@bot.message_handler(commands=['code'])
def entering_code(message):
    bot.reply_to(message, 'please send your code so I can run it!')

    @bot.message_handler(func=lambda msg: msg.text is not None)
    def input_code_text(code):
        lines = [line for line in code.text.split('\n')]
        bot.reply_to(code, str(brain(lines)))

        with open('output.txt', 'w+') as f:
            f.write('')


keep_alive()

# updater loop
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
