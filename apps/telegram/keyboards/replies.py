from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_contact():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("Telefon raqamni yuborish", request_contact=True)
            ]
        ], resize_keyboard=True
    )


def get_gender_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Erkak")],
            [KeyboardButton("Ayol")]
        ], resize_keyboard=True
    )


def get_items(items, key):
    keyboard = []

    for item in items:
        keyboard.append(
            [
                KeyboardButton(getattr(item, key))
            ]
        )
    return ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True
    )