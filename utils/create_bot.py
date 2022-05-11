from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from utils.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
