from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler
from apps.telegram.handlers import commands, common, registration
from apps.telegram import states
from django.conf import settings

bot = Bot(token=settings.BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

start_handler = CommandHandler('start', commands.start)

conversation_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        states.PHONE: [MessageHandler(Filters.all, registration.get_phone)],
        states.FULL_NAME: [MessageHandler(Filters.all, registration.get_full_name)],
        states.PASSPORT: [MessageHandler(Filters.all, registration.get_passport)],
        states.PINFL: [MessageHandler(Filters.all, registration.get_pinfl)],
        states.GENDER: [MessageHandler(Filters.all, registration.get_gender)],
        states.BIRTH_DATE: [MessageHandler(Filters.all, registration.get_birth_date)],
        states.FACULTY: [MessageHandler(Filters.all, registration.get_faculty)],
        states.DIRECTION: [MessageHandler(Filters.all, registration.get_direction)],
        states.REGION: [MessageHandler(Filters.all, registration.get_region)],
        states.DISTRICT: [MessageHandler(Filters.all, registration.get_district)],
    },
    fallbacks=[start_handler],
)

dispatcher.add_handler(conversation_handler)