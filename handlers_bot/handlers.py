import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.create_bot import dp, bot
from utils.config import MY_ID


# TODO добавить цикл событий
# TODO добавить обработчик обновлений


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        'Бот собирает объявления о недвижимости\n\
         с авито, циан и яндекс. Оповещение\n\
         с каждым новым объявлением на сайтах.'
    )
