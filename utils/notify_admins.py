from aiogram import Dispatcher

from data.config import admins
import logging

async def on_startup_notify(dp:Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, 'Бот2 учебный Запущен и готов к работе с хендлерами и фильтрами!')
        except Exception as err:
            logging.exception(err)

