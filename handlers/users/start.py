import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from filters import SomeF
from loader import dp
from utils.misc import rate_limit


# Можно запускать раз в 10 сек
@rate_limit(limit=10)
@dp.message_handler(CommandHelp())
async def bothelp(message: types.Message):
    await message.answer("/block_me - Заблокироваться, /unblock_me - Разблокироваться")


@dp.message_handler(CommandStart(), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter):
    logging.info(f"5. Handler! {middleware_data=}, {from_filter=}")
    logging.info("Следующая точка: post process message\n")

    await message.answer(f'Привет, {message.from_user.full_name}!\n',
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Простая кнопка", callback_data="button")
                                 ]
                             ]
                         ))

    return {"from_handler": "Данные из хендлера!"}
