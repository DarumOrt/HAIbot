import os
import asyncio
import logging
import openai
from aiogram import Dispatcher, Bot, types
from aiogram.types import BotCommand

from bot.commands.bcommands import bot_commands
from bot.commands import register_user_commands
from bot.ai import user_ai


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    openai.api_key = os.getenv('ai_token')
    bot = Bot(token=os.getenv('token'))
    dp = Dispatcher()
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    user_ai(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')
