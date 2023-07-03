from aiogram import types
from bot.ai.ai_response import Aimessages


async def Changerole(message: types.Message):
    Aimessages.append({"role": "system", "content": message.text})
    await message.reply("Роль поменялась")