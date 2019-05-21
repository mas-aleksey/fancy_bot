# -*- coding: utf-8 -*-
import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import logging
import Weather, vk_api

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def callback_alarm(bot, job):
     bot.send_message(chat_id=job.context, text='BEEP')

def callback_text(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s" % (user.first_name, update.message.text))
    #ans = 'обработчика этого слова еще нет('
    #if 'погода' in update.message.text.lower():
     #   ans = Weather.get()
    if 'уха' in update.message.text.lower():
        ans = vk_api.getRnd()
        bot.send_message(chat_id=update.message.chat_id, text=ans)

def yxa(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s" % (user.first_name, update.message.text))
    ans = vk_api.getRnd()
    bot.send_message(chat_id=update.message.chat_id, text=ans)

def pogoda(bot, update):
    ans = Weather.get()
    bot.send_message(chat_id=update.message.chat_id, text=ans)

def callback_timer(bot, update, job_queue):
     bot.send_message(chat_id=update.message.chat_id,
                      text='Команды:\n/yxa - случайный анекдот из контакта')
     
     #job_alarm = Job(callback_alarm,
      #               10.0,
       #              repeat=True,
        #             context=update.message.chat_id)
     #job_queue.put(job_alarm)
     #job_queue.run_repeating(callback_alarm, 10,context=update.message.chat_id)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                      text='Команды:\n"/yxa" - случайный анекдот из контакта\nДля вызова этого сообщения используй /start')
     

def main():
    updater = Updater("404672999:AAF2nOfQWL0YL8sbTwuyDsio8B9TEFuV8ZU")
    dp = updater.dispatcher
    #updater.job_queue.run_repeating(callback_alarm, 10, context = 'chat_id = 134751583')
    #timer_handler = CommandHandler('start', callback_timer, pass_job_queue=True)
    #dp.add_handler(timer_handler)
    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(CommandHandler('help', start))
    dp.add_handler(CommandHandler('yxa', yxa))
    #dp.add_handler(CommandHandler('pogoda', pogoda))
    dp.add_handler(MessageHandler(Filters.text, callback_text))
    dp.add_error_handler(error)

    updater.start_polling(poll_interval=2, timeout=20, read_latency=5)
    updater.idle()


if __name__ == '__main__':
    main()