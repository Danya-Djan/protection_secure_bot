from random import random
from aiogram import Dispatcher, types
from create_bot import bot, user_list
from keyboards import kb_apply, kb_register, kb_number, kb_qr
from aiogram.dispatcher.filters import Text
import re
import random
import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from defs import rsa_encrypt, miller, rsa_sign, rsa_decrypt, gamal, elliptical
from aiogram.types import InputFile
import uuid
import time



class new_task(StatesGroup):
        enc_rsa = State()
        miller = State()
        sign_rsa = State()
        dec_rsa = State()
        enc_gamale = State()
        sign_gamale = State()
        sign_gamale = State()
        curve_1 = State()
    
b1 = KeyboardButton("Зашифровать RSA")
b2 = KeyboardButton("Простота по Миллеру")
b3 = KeyboardButton("Подпись RSA")
b4 = KeyboardButton("Расшифровать RSA")
b5 = KeyboardButton("Зашифровать Эль-Гамаля")
b6 = KeyboardButton("Подпись Эль-Гамаля")
b7 = KeyboardButton("Элиптическая кривая с a и b")

kb_tasks = ReplyKeyboardMarkup(resize_keyboard=True)

kb_tasks.row(b1)
kb_tasks.row(b2)
kb_tasks.row(b3)
kb_tasks.row(b4)
kb_tasks.row(b5)
kb_tasks.row(b6)
kb_tasks.row(b7)

def generate_short_uuid():
    full_uuid = str(uuid.uuid4())
    short_uuid = full_uuid[:5]
    return str(short_uuid)


async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Выберите, какую задачу будем решать:", reply_markup=kb_tasks)

async def start_task(message : types.Message, state:FSMContext):
    if message.from_user.username in user_list:
        if message.text == "Зашифровать RSA":
            await new_task.enc_rsa.set()
            await bot.send_message(message.from_user.id, "Введите числа(n, e, m) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Простота по Миллеру":
            await new_task.miller.set()
            await bot.send_message(message.from_user.id, "Введите числа и p через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Подпись RSA":
            await new_task.sign_rsa.set()
            await bot.send_message(message.from_user.id, "Введите числа(n, d, m) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Расшифровать RSA":
            await new_task.dec_rsa.set()
            await bot.send_message(message.from_user.id, "Введите числа(n, e, c) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Зашифровать Эль-Гамаля":
            await new_task.enc_gamale.set()
            await bot.send_message(message.from_user.id, "Введите числа(p, g, y, m, k) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Подпись Эль-Гамаля":
            await new_task.sign_gamale.set()
            await bot.send_message(message.from_user.id, "Введите числа(p, g, y, m, k) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Элиптическая кривая с a и b":
            await new_task.curve_1.set()
            await bot.send_message(message.from_user.id, "Введите числа(x, y, a, b, F и c(если вдруг надо посчитать не 3A)) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        else:
            await bot.send_message(message.from_user.id, "Нормально пиши да, что ты меньжуешься\nКлацай /start", reply_markup=types.ReplyKeyboardRemove())
    
async def send_encrypt_rsa(message : types.Message, state:FSMContext):
    try:
        n, e, m = message.text.split()
        filename = f'files/rsa_encrypt-{generate_short_uuid()}.docx'
        rsa_encrypt.rsa_encrypt(int(n), int(e), int(m), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
async def send_miller(message : types.Message, state:FSMContext):
    try:
        lis = list(map(int, message.text.split()))
        p = lis[-1]
        l = lis[:-1]
        filename = f'files/miller-{generate_short_uuid()}.docx'
        miller.miller(l, p, filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
        
async def send_sign_rsa(message : types.Message, state:FSMContext):
    try:
        n, d, m = message.text.split()
        filename = f'files/rsa_sign-{generate_short_uuid()}.docx'
        rsa_sign.rsa_sign(int(n), int(d), int(m), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
async def send_decrypt_rsa(message : types.Message, state:FSMContext):
    try:
        n, e, c = message.text.split()
        filename = f'files/decrypt_rsa-{generate_short_uuid()}.docx'
        rsa_decrypt.rsa_decrypt(int(n), int(e), int(c), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
async def send_encrypt_gamale(message : types.Message, state:FSMContext):
    try:
        p, g, y, m, k = message.text.split()
        filename = f'files/encrypt_gamale-{generate_short_uuid()}.docx'
        gamal.encrypt_gamal(int(p), int(g), int(y), int(k), int(m), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
async def send_sign_gamale(message : types.Message, state:FSMContext):
    try:
        p, g, y, m, k = message.text.split()
        filename = f'files/sign_gamale-{generate_short_uuid()}.docx'
        gamal.sign_gamal(int(p), int(g), int(y), int(k), int(m), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
        
async def curve_with_ab(message : types.Message, state:FSMContext):
    try:
        lis = message.text.split()
        filename = f'files/curve_with_ab-{generate_short_uuid()}.docx'
        if len(lis) == 5:
            elliptical.elliptical(filename, int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3]), int(lis[4]))
        if len(lis) == 6:
            elliptical.elliptical(filename, int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3]), int(lis[4]), int(lis[5]))
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks)