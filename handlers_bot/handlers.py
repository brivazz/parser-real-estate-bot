import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.create_bot import dp, bot
from utils.config import MY_ID
from parsers import avito_parser
from parsers import cian_parser
from parsers import yandex_parser


# TODO добавить цикл событий
# TODO добавить обработчик обновлений


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        'Бот собирает объявления о недвижимости\n\
         с авито, циан и яндекс. Оповещение\n\
         с каждым новым объявлением на сайтах.'
    )


async def offer_every_hour():
    await asyncio.sleep(5)

    while True:
        try:
            avito = await avito_parser.main()
            if avito:
                await send_to_me(avito)
        except Exception:
            continue
        try:
            cian = await cian_parser.main()
            if cian:
                await send_to_me(cian)
        except Exception:
            continue
        try:
            yandex = await yandex_parser.main()
            if yandex:
                await send_to_me(yandex)
        except Exception:
            continue

        await asyncio.sleep(60 * 60)


async def send_to_me(items: list):
    if len(offer_every_hour()) >= 1:
        for item in items:
            id = item['id']
            title = item['title']
            price = item['price']
            url = item['url']
            description = item['description']
            geo = item['geo']
            date = item['date']

            offer = f'{id}\n{title}\n{price}\n{url}\n{description}\n{geo}\n{date}'

            await bot.send_message(MY_ID, offer)
