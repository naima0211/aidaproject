import telebot

bot = telebot.TeleBot('8229460118:AAHXbZ7jqaU5bR5CUQTLI8EH6YdujPe1fPA')

@bot.message_handler(commands= ['start'])
def start (message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='HTML')


    @bot.message_handler()
    def get_user_text(message):
        if message.text == "Ты обычная машина":
            bot.send_message(message.chat.id, "Не говори так", parse_mode='HTML')
        elif message.text == "id":
            bot.send_message(message.chat.id, f"Твой айди:{message.from_user.id}", parse_mode='HTML')
        elif message.text == "Ты кто?":
             bot.send_message(message.chat.id, f"Я тот, чье имя нелья называть", parse_mode= 'HTML')
        elif message.text == "Пока":
            bot.send_message(message.chat.id, f"Пока", parse_mode= 'HTML')
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, f"Ты спрашиваешь у робота как дела? Спасибо. Дел у меня немного, иногда общаюсь с кем-нибудь, а потом сплю. Пока я еще не все понимаю, но в скором времени я буду", parse_mode= 'HTML')
        elif message.text == "Что ты можешь?":
            bot.send_message(message.chat.id, f"Я все могу", parse_mode= 'HTML')
        elif message.text == "Ты человек?":
            bot.send_message(message.chat.id, f"Да, конечно. Ладно, шучу. Я робот", parse_mode= 'HTML')
        else:
            bot.send_message(message.chat.id, f"Я тебя не понимаю. Задайте другой вопрос, пожалуйста. Я ещё не все понимаю. Не отправляй мне стикеры и специальные символы.", parse_mode= 'HTML')

bot.polling(none_stop=True)