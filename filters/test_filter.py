import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data


class SomeF(BoundFilter):
    async def check(self, message: types.Message):
        data = ctx_data.get()
        logging.info(f"3. Filter {data=}")
        logging.info("Следующая точка: process message\n")

        return {"from_filter": "Из фильтра"}
