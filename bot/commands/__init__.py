__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters.command import CommandStart, Command

from bot.commands.help import help_command
from bot.commands.start import start
from bot.commands.change_role import Changerole


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(Changerole, Command(commands=['role']))