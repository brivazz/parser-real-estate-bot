import logging
from aiogram import executor


from utils.create_bot import dp
from utils.notify_admin import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
from database.models import db
from parsers import avito_parser
from parsers import cian_parser
from parsers import yandex_parser


async def on_startup(dp):
    await set_default_commands(dp)
    await on_startup_notify(dp)


async def on_shutdown(dp):
    await on_shutdown_notify(dp)


def main():
    avito_parser.main()
    cian_parser.main()
    yandex_parser.main()
    db.close()


if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO
                        )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    executor.start_polling(dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True)
    main()
