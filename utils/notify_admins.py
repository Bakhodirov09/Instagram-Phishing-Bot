import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot faollashdi!")
        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot Toxtadi!")

        except Exception as err:
            logging.exception(err)