import logging
from utils.config import MY_ID


async def on_startup_notify(dp):
    if MY_ID:
        try:
            await dp.bot.send_message(
                text='Бот запущен',
                chat_id=MY_ID,
                disable_notification=True
            )
        except Exception as err:
            logging.error(err)


async def on_shutdown_notify(dp):
    if MY_ID:
        await dp.bot.send_message(
            text='Бот упал',
            chat_id=MY_ID,
            disable_notification=True
        )
