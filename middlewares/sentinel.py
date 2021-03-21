import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware, BaseMiddleware

from utils.db_api.models import User


class SentinelController(BaseMiddleware):
    allowed_updates = ["callback_query", "message"]

    async def trigger(self, action, args):

        obj, *args, data = args
        if not any(update in action for update in self.allowed_updates):
            return False

        if not action.startswith('process_'):
            return False

        user: User = data.get('user')

        handler = current_handler.get()
        if not handler:
            return

        allow = getattr(handler, 'allow', False)
        if allow:
            return

        if not user.allowed:
            message = obj.message if isinstance(obj, types.CallbackQuery) else obj
            await message.reply("Доступ к боту запрещен")
            raise CancelHandler()
