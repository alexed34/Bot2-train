from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Первое меню')],
        [
            KeyboardButton(text='Второе меню'),
            KeyboardButton(text='Третье меню')
        ]
    ], resize_keyboard=True)
