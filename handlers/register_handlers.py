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

from handlers.register_task_kr_3 import (new_task_3,
                                         command_start_3,
                                         start_task_3,
                                         send_group_points,
                                         send_generator_group_points,
                                         send_gost,
                                         send_diffi_public,
                                         send_diffi_private,
                                         send_diffi_elliptical,
                                         send_blackly,
                                         send_shamir,
                                         send_blom)




def register_all_handlers(dp: Dispatcher):
    # handle_register_tasks(dp)
    handle_register_task_3(dp)


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
    
def handle_register_task_3(dp : Dispatcher):
    dp.register_message_handler(command_start_3, commands=['start'])
    dp.register_message_handler(start_task_3)
    dp.register_message_handler(send_group_points, state=new_task_3.group)
    dp.register_message_handler(send_generator_group_points, state=new_task_3.generator)
    dp.register_message_handler(send_gost, state=new_task_3.gost)
    dp.register_message_handler(send_diffi_public, state=new_task_3.diffi_public)
    dp.register_message_handler(send_diffi_private, state=new_task_3.diffi_private)
    dp.register_message_handler(send_diffi_elliptical, state=new_task_3.diffi_elliptical)
    dp.register_message_handler(send_blackly, state=new_task_3.blackly)
    dp.register_message_handler(send_shamir, state=new_task_3.shamir)
    dp.register_message_handler(send_blom, state=new_task_3.blom)