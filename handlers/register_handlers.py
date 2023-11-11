from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType


from handlers.register_task import (new_task,
                                    command_start,
                                    start_task,
                                    send_encrypt_rsa,
                                    send_miller,
                                    send_sign_rsa,
                                    send_decrypt_rsa,
                                    send_encrypt_gamale,
                                    send_sign_gamale,
                                    curve_with_ab,)


def register_all_handlers(dp: Dispatcher):
    handle_register_tasks(dp)


def handle_register_tasks(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(start_task)
    dp.register_message_handler(send_encrypt_rsa, state=new_task.enc_rsa)
    dp.register_message_handler(send_miller, state=new_task.miller)
    dp.register_message_handler(send_sign_rsa, state=new_task.sign_rsa)
    dp.register_message_handler(send_decrypt_rsa, state=new_task.dec_rsa)
    dp.register_message_handler(send_encrypt_gamale, state=new_task.enc_gamale)
    dp.register_message_handler(send_sign_gamale, state=new_task.sign_gamale)
    dp.register_message_handler(curve_with_ab, state=new_task.curve_1)