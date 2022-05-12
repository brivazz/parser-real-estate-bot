import logging
import asyncio
from aiogram import executor

from utils.create_bot import dp
from utils.notify_admin import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
from database.models import db
from handlers_bot.handlers import offer_every_hour


async def on_startup(dp):
    await set_default_commands(dp)
    await on_startup_notify(dp)


async def on_shutdown(dp):
    await on_shutdown_notify(dp)
    db.close()


if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO
                        )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.create_task(offer_every_hour())
    executor.start_polling(dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True,
                           loop=loop)
