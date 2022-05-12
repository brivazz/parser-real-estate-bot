import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

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


async def offer_every_hour():
    await asyncio.sleep(5)

    while True:
        avito = avito_parser.main()
        await send_to_me(avito)
        print('avito==None')

        cian = cian_parser.main()
        await send_to_me(cian)
        print('cian==None')

        yandex = yandex_parser.main()
        await send_to_me(yandex)
        print('yandex==None')

        await asyncio.sleep(60 * 60)


async def send_to_me(items: list):
    try:
        if len(items) >= 1:
            for item in items:
                title = item['title']
                price = item['price']
                url = item['url']
                description = item['description']
                geo = item['geo']
                date = item['date']

                offer = f'{title}\n{price}\n{url}\n{description}\n{geo}\n{date}'

                await bot.send_message(MY_ID, offer)
    except Exception as err:
        print('Ошибка: ', err)
