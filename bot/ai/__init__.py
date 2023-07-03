__all__ = ['user_ai']

from aiogram import Router

from bot.ai.ai_response import handle_message


def user_ai(router: Router) -> None:
    router.message.register(handle_message)
