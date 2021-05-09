from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, ParseMode
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from telegram_bot.models import TelegramReceiver
from .utils import log_errors


@log_errors
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    username = update.message.from_user.username
    receivers = TelegramReceiver.objects.all()

    if not receivers:
        answer_text = 'Я не смог подключить Вас к системе. Если это произошло по ошибке, просьба обратиться к администратору.'
        update.message.reply_text(text=answer_text)
        return

    accounts = [receiver for receiver in receivers]

    for account in accounts:
        if account.telegram_login == username and account.telegram_id == chat_id:
            answer_text = 'Вы уже подключены. Я буду уведомлять Вас о заявках.'
        else:
            account.telegram_id = chat_id
            account.save()
            answer_text = 'Вы были успешно подключены к системе. Я буду уведомлять Вас о заявках.'
        update.message.reply_text(text=answer_text)


@log_errors
def send_message(message):
    request = Request(connect_timeout=0.5, read_timeout=1.0)
    bot = Bot(request=request, token=settings.TOKEN)
    queryset = TelegramReceiver.objects.all()
    message = "‼️ <b>‼️ Заявка на обратную связь ‼️</b> ‼️ \n\n" + message
    for receiver in queryset:
        try:
            bot.send_message(chat_id=receiver.telegram_id, text=message, parse_mode=ParseMode.HTML)
        except:
            pass


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # 1 -- правильное подключение
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(request=request, token=settings.TOKEN)
        print(bot.get_me())

        # 2 -- обработчики
        updater = Updater(bot=bot, use_context=True)

        start_handler = CommandHandler('start', start)
        updater.dispatcher.add_handler(start_handler)

        # 3 -- запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()
