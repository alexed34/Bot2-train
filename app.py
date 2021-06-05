from aiogram import executor
from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_command import set_default_command
from handlers import dp


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_command(dp)





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

