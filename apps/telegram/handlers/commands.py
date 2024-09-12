from apps.telegram.models import Telegram
from apps.telegram.keyboards import replies
from apps.telegram import states


def start(update, contex):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    telegram_id = user.id

    Telegram.objects.update_or_create(
        telegram_id=telegram_id,
        defaults={
            "first_name": first_name,
            "last_name": last_name,
        }
    )

    message = "Hello welcome to https://tift-uz.onrender.com boti send your phone number to leave an application "
    update.message.reply_text(message, reply_markup=replies.get_contact())
    return states.PHONE