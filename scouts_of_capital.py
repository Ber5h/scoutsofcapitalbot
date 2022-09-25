import telebot
from telebot import types
list_of_adm = []
if __name__ == "__main__":
  @bot.message_handler(commands=['start'])
  def start_message(message):
	  bot.send_message(message.chat.id,'Приветствую. Это бот-предложка для канала https://t.me/scouts_capital\nЗдесь вы '
                                     'можете предложить новость на рассмотрение модерации канала' )
  @bot.message_handler(commands = ['help'])
  def help_message (message):
      bot.send_message(message.chat.id, 'Чтобы предложить новость, просто напишите ее в сообщения боту, ваша запись'
                                      'будет отправлена модераторам канала.\nЧтобы стать модератором введите команду '
                                      '/become_moder')
#@bot.message_handler(commands = ['become_moder'])
#def become_moder (message):
#    bot.send_message(message.chat.id, 'Введите пароль')
 #   moder_ready = True
  @bot.message_handler(commands = ['give_me_products'])
  def moder (message):
              list_of_adm.append(message.chat.id)
              bot.send_message(message.chat.id, 'Вы успешно стали модератором. Отменить это действие пока '
                         'нельзя, так как код я буду дописывать')
  @bot.message_handler(content_types = ['text'])
  def offers (message):
          for i in list_of_adm:
              bot.send_message(i, message.text)
          bot.send_message(message.chat.id, 'Ваша запись отправлена, и будет рассмотрена в ближайшем времени')
  bot.polling(none_stop=True, interval=0)
