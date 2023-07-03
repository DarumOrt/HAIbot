import openai
from aiogram import types

Aimessages = [
        {"role": "system", "content": "Ты бот помощник по python"},
        {"role": "user", "content": "Меня зовут Иван. Я студент, учусь программировать"},
        {"role": "assistant", "content": "Привет, Иван. Чем я могу вам помочь?"},
    ]


async def handle_message(message: types.Message):
    Aimessages.append({"role": "user", "content": message.text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=Aimessages
    )
    await message.answer(response['choices'][0]['message']['content'])

