from aiogram import types, Dispatcher

async def set_default_command(dp:Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('menu', 'Текстовое меню'),
            types.BotCommand('start', 'Заапустить бота'),
            types.BotCommand('help', 'Поомощь'),
            types.BotCommand('items', 'меню инлайн кнопки')
        ]

    )
