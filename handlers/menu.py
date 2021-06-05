from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message

from keyboards.default import menu
from loader import dp



@dp.message_handler(Command('menu'))
async def show_menu(message:Message):
    await message.answer(f'Выберете товар из меню', reply_markup=menu)

@dp.message_handler(Text(equals=['Первое меню', 'Второе меню', 'Третье меню']))
async def get_foods(message:Message):
    await message.answer(f'Отличный выбор {message.text}')