import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold, hlink

from utils.create_bot import dp, bot
from utils.config import MY_ID
from parsers import avito_parser
from parsers import cian_parser
from parsers import yandex_parser


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        'Бот собирает объявления о недвижимости\n\
        с авито, циан и яндекс. Оповещение\n\
        с каждым новым объявлением на сайтах.'
    )


async def offers_every_hour():
    await asyncio.sleep(5)

    while True:
        avito = avito_parser.main()
        await send_to_me(avito)

        cian = cian_parser.main()
        await send_to_me(cian)

        yandex = yandex_parser.main()
        await send_to_me(yandex)

        await asyncio.sleep(60 * 60)


async def send_to_me(items: list):
    if items:
        for item in items:
            title = f"{hlink(item['title'], item['url'])}"
            price = hbold('{:,d}'.format(item['price'])) + ' руб.'
            description = item['description']
            geo = hbold(item['geo'])
            date = hbold(item['date'])

            offer = f'{price}\n\n{title}\n\n{geo}\n\n{description}\n\n{date}\n'

            await bot.send_message(MY_ID, offer)
