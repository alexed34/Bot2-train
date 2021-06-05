from loader import bot, dp
from aiogram.types import Message


@dp.message_handler()
async def echo(message: Message):
    text = f'Ты написал {message.text}'
    await bot.send_message(chat_id=message.from_user.id, text=text)
    # text = f'Ты написал 2  {message.text}'
    # await message.answer(text)
