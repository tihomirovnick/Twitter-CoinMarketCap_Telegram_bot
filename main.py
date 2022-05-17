from aiogram.utils import executor
from create import dp
from aiogram import types
from data_base import sqlite_db

async def on_startup(dp):
	print('Bot online...')
	sqlite_db.sql_start()
	await dp.bot.set_my_commands([
		types.BotCommand("start", "Запустить бота")])


from handlers import client

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)