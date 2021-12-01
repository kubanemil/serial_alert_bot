import telebot
import ts_note

bot = telebot.TeleBot("TOKEN")
bot_info = bot.get_me()
print(bot_info)
chat_id = #Your chat ID

def send(text):
    bot.send_message(chat_id, text)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(chat_id, 'Yes, bitch, I am in.')
    bot.send_message(chat_id, 'Every new episode of your show list - new message.')
    send('/shows \n/new_episode')

@bot.message_handler(commands=['shows'])
def showy(message):
    i = 0
    send('ВЫ СМОТРИТЕ:')
    for link in ts_note.shows_link_list():
        i += 1
        send(str(i) + '.' +ts_note.get_title(link))

@bot.message_handler(commands=['new_episode'])
def newy(message):
    send('Serching for new episode...')
    found_new_episode = False
    for link in ts_note.shows_link_list():
        if ts_note.new_episode(link):
            if found_new_episode == False:
                send('New episodes for:')
            send(ts_note.get_title(link) + '\n' + ts_note.new_episode(link))
            ts_note.add_to_watched(ts_note.new_episode(link))
            found_new_episode = True
    send('End.')

# newy('ll')

bot.infinity_polling()