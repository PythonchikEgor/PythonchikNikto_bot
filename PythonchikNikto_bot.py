from telebot import TeleBot

token = "7486590486:AAH2CmGzyD1HIRG9gP318YYcZAuhyWOz2Ug"
bot = TeleBot(token)


# @bot.message_handler(commands=["help"])
# def help(message):
#     bot.send_message(message.chat.id, "Типо помощь")


@bot.message_handler(content_types=['sticker'])
def send_welcome(message):
    # Отправляем сообщение
    #sent_message = bot.send_message(message.chat.id, "Привет! Это тестовое сообщение")

    # Удаляем сообщение
    bot.delete_message(message.chat.id, message.message_id)


bot.polling()