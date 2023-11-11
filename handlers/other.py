from aiogram import types, Dispatcher
from create_bot import bot


async def echo_send(message : types.Message):
    await message.answer(message.text)

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(echo_send)