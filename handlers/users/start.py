import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from filters import SomeF
from loader import dp
from utils.db_api.models import User
from utils.misc import rate_limit


# Можно запускать раз в 10 сек
@rate_limit(limit=10)
@dp.message_handler(CommandHelp())
async def bothelp(message: types.Message):
    await message.answer("/block_me - Заблокироваться, /unblock_me - Разблокироваться")


# @rate_limit(5, key="start")
@dp.message_handler(CommandStart(), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter, user: User):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{middleware_data=} \n{from_filter=}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Простая кнопка", callback_data="button")
                                 ]
                             ]
                         ))
    logging.info(f"6. Handler")
    logging.info("Следующая точка: Post Process Message")
    return {"from_handler": "Данные из хендлера"}


@dp.callback_query_handler(text="button")
async def get_button(call: types.CallbackQuery):
    await call.message.answer("Вы нажали на кнопку")
