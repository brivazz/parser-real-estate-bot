from aiogram.types.bot_command import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand('start', 'Запустить бота')
        ]
    )
