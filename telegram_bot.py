import os
import telebot
import random

class Bot:
    def __init__(self):
        self.BOT_TOKEN = os.environ.get('BOT_TOKEN')
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        self.user_names = {}

    def start(self):
        self.bot.message_handler(commands=['start', 'selam'])(self.send_welcome)
        self.bot.message_handler(commands=['isimler'])(self.set_names)
        self.bot.message_handler(commands=['göster'])(self.get_names)
        self.bot.message_handler(commands=['ekle'])(self.add_name)
        self.bot.message_handler(commands=['sil'])(self.remove_name)
        self.bot.message_handler(func=lambda msg: True)(self.echo_all)
        self.bot.infinity_polling()

    def send_welcome(self, message):
        self.bot.reply_to(message, "Arkadaşlarınz hakkında merak ettiğiniz soruları bana sorabilirsiniz? \n Başlangıçta chat kısmına /isimler yazarak arkadaşlarınızın ismini girebilirsiniz. \n /goster komutu ile kaydedilen isimleri görebilirsiniz. \n /ekle komutu ile yeni isim ekleyebilir /sil komutu ile eklenen ismi çıkartabilirsiniz.")

    def set_names(self, message):
        chat_id = message.chat.id
        self.bot.reply_to(message, "İsimleri aralarına virgül koyarak girin:")
        self.bot.register_next_step_handler(message, self.process_names, chat_id)

    def process_names(self, message, chat_id):
        names = [name.strip() for name in message.text.split(",")]
        self.user_names[chat_id] = names
        self.bot.reply_to(message, "İsimler kaydedildi.")

    def get_names(self, message):
        chat_id = message.chat.id
        if chat_id in self.user_names:
            names = '\n'.join(self.user_names[chat_id])
            self.bot.reply_to(message, f"İsimler:\n{names}")
        else:
            self.bot.reply_to(message, "Henüz isimler kaydedilmemiş.")

    def add_name(self, message):
        chat_id = message.chat.id
        self.bot.reply_to(message, "Eklemek istediğiniz ismi girin:")
        self.bot.register_next_step_handler(message, self.process_add_name, chat_id)

    def process_add_name(self, message, chat_id):
        name = message.text.strip()
        if chat_id in self.user_names:
            self.user_names[chat_id].append(name)
        else:
            self.user_names[chat_id] = [name]
        self.bot.reply_to(message, f"{name} ismi eklendi.")

    def remove_name(self, message):
        chat_id = message.chat.id
        self.bot.reply_to(message, "Silmek istediğiniz ismi girin:")
        self.bot.register_next_step_handler(message, self.process_remove_name, chat_id)

    def process_remove_name(self, message, chat_id):
        name = message.text.strip()
        if chat_id in self.user_names and name in self.user_names[chat_id]:
            self.user_names[chat_id].remove(name)
            self.bot.reply_to(message, f"{name} ismi silindi.")
        else:
            self.bot.reply_to(message, f"{name} ismi bulunamadı veya kaydedilmemiş.")

    def echo_all(self, message):
        chat_id = message.chat.id
        if chat_id in self.user_names:
            self.bot.reply_to(message, random.choice(self.user_names[chat_id]))
        else:
            self.bot.reply_to(message, "Henüz isimler kaydedilmemiş.")

bot = Bot()
bot.start()
