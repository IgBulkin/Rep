import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users


class BigBrother(BaseMiddleware):

    # 1.
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info(f"[----------------------Новый апдейт!----------------------]")
        logging.info(f"1. PRE process update")
        logging.info("Следующая точка: Process update\n")
        data["middleware_data"] = "Это пройдет до on_post_process_update"

        user = update.message.from_user.id if update.message else update.callback_query.from_user.id
        if user in banned_users:
            raise CancelHandler()

    # 2.
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2. Process update, {data=}")
        logging.info("Следующая точка: Pre process message\n")

    # 3.
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. PRE process message, {data=}")
        logging.info("Следующая точка: Filter, Process message\n")
        data["middleware_data"] = "Это пройдет в on_process_message"

    # 4. Filters

    # 5.
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info(f"4. Process message, {data=}")
        logging.info("Следующая точка: handler\n")
        data["middleware_data"] = "Это пройдет в Handler"

    # 6. Handler

    # 7.
    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data):
        logging.info(f"6. Post process message, {data=} {data_from_handler=}")
        logging.info("Следующая точка: Post process Update\n")

    # 8.
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data):
        logging.info(f"7. Post process update, {data=} {data_from_handler=}")
        logging.info(f"[----------------------Выход------------------------------]\n")

    async def on_pre_process_callback_query(self, cq: types.CallbackQuery, data: dict, *args):
        # Уберем часики.
        await cq.answer()
