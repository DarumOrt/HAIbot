from aiogram import types


async def start(message: types.Message) -> None:
    await message.answer('Привет! Я бот помощник, у которого ты можешь менять роль!')
