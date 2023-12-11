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
from defs import diffi, diffi2, elliptical, gost, group_points, blackly, shamir, blom
from aiogram.types import InputFile
import uuid
import time



class new_task_3(StatesGroup):
        group = State()
        generator = State()
        gost = State()
        diffi_public = State()
        diffi_private = State()
        diffi_elliptical = State()
        blackly = State()
        shamir = State()
        blom = State()

b1 = KeyboardButton("Группа точек")
b2 = KeyboardButton("Генератор группы точек")
b3 = KeyboardButton("ГОСТ")
b4 = KeyboardButton("Диффи (даны открытые ключи)")
b5 = KeyboardButton("Диффи (даны закрытые ключи)")
b6 = KeyboardButton("Диффи эллептическая кривая")
b7 = KeyboardButton("Блэкли")
b8 = KeyboardButton("Шамир")
b9 = KeyboardButton("Блом")

kb_tasks_3 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_tasks_3.row(b1)
kb_tasks_3.row(b2)
kb_tasks_3.row(b3)
kb_tasks_3.row(b4)
kb_tasks_3.row(b5)
kb_tasks_3.row(b6)
kb_tasks_3.row(b7)
kb_tasks_3.row(b8)
kb_tasks_3.row(b9)

def generate_short_uuid():
    full_uuid = str(uuid.uuid4())
    short_uuid = full_uuid[:5]
    return str(short_uuid)

async def command_start_3(message : types.Message):
    if message.from_user.id in user_list:
        await bot.send_message(message.from_user.id, "Выберите, какую задачу будем решать:", reply_markup=kb_tasks_3)

async def start_task_3(message : types.Message, state:FSMContext):
    if message.from_user.username in user_list:
        if message.text == "Группа точек":
            await new_task_3.group.set()
            await bot.send_message(message.from_user.id, "Введите числа(a, b, n) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Генератор группы точек":
            await new_task_3.generator.set()
            await bot.send_message(message.from_user.id, "Введите числа(x, y, a, b, F и c(если вдруг надо посчитать не 3A)) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "ГОСТ":
            await new_task_3.gost.set()
            await bot.send_message(message.from_user.id, "Введите числа(m, a, b, F, g_1, g_2, n(размер подгруппы), q_1, q_2, k) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Диффи (даны открытые ключи)":
            await new_task_3.diffi_public.set()
            await bot.send_message(message.from_user.id, "Введите числа(g(генератор), p(модуль), a, b) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Диффи (даны закрытые ключи)":
            await new_task_3.diffi_private.set()
            await bot.send_message(message.from_user.id, "Введите числа(g(генератор), p(модуль), a, b) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Диффи эллептическая кривая":
            await new_task_3.diffi_elliptical.set()
            await bot.send_message(message.from_user.id, "Введите числа(g_1, g_2, a, b, F, alisa, bob) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Блэкли":
            await new_task_3.blackly.set()
            await bot.send_message(message.from_user.id, "Введите числа(p, n(число следов) и 12 чисел(каждый след по очереди)) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Шамир":
            await new_task_3.shamir.set()
            await bot.send_message(message.from_user.id, "Введите числа(p, x1, y1, x2, y2, x3, y3)(любые 3 следа) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == "Блом":
            await new_task_3.blom.set()
            await bot.send_message(message.from_user.id, "Введите числа(p, Ax, Ay(идентификатор), AxClosed, AyClosed(закрытый ключ), Bx, By(открытый ключ), BxClosed, ByClosed(закрытый ключ Боба)) через пробел:", reply_markup=types.ReplyKeyboardRemove())
        else:
            await bot.send_message(message.from_user.id, "Нормально пиши да, что ты меньжуешься\nКлацай /start", reply_markup=types.ReplyKeyboardRemove())
    
async def send_group_points(message : types.Message, state:FSMContext):
    try:
        a, b, n = message.text.split()
        filename = f'files/group_points-{generate_short_uuid()}.docx'
        ans = group_points.group_points(int(a), int(b), int(n), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_generator_group_points(message : types.Message, state:FSMContext):
    try:
        lis = message.text.split()
        filename = f'files/generator_group_points-{generate_short_uuid()}.docx'
        if len(lis) == 5:
            ans = elliptical.elliptical(filename, int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3]), int(lis[4]))
        if len(lis) == 6:
            ans = elliptical.elliptical(filename, int(lis[0]), int(lis[1]), int(lis[2]), int(lis[3]), int(lis[4]), int(lis[5]))
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
async def send_gost(message : types.Message, state:FSMContext):
    try:
        m, a, b, f, g_1, g_2, n, q_1, q_2, k = message.text.split()
        filename = f'files/gost-{generate_short_uuid()}.docx'
        ans = gost.gost(int(m), int(a), int(b), int(f), int(g_1), int(g_2), int(n), int(q_1), int(q_2), int(k), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_diffi_public(message : types.Message, state:FSMContext):
    try:
        g, p, a, b = message.text.split()
        filename = f'files/diffi_public-{generate_short_uuid()}.docx'
        ans = diffi.diffi_public(int(g), int(p), int(a), int(b), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_diffi_private(message : types.Message, state:FSMContext):
    try:
        g, p, a, b = message.text.split()
        filename = f'files/diffi_private-{generate_short_uuid()}.docx'
        ans = diffi.diffi_private(int(g), int(p), int(a), int(b), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_diffi_elliptical(message : types.Message, state:FSMContext):
    try:
        generator1, generator2, a, b, F, alisa, bob = message.text.split()
        filename = f'files/diffi_elliptical-{generate_short_uuid()}.docx'
        ans = diffi2.diffi2(int(generator1), int(generator2), int(a), int(b), int(F), int(alisa), int(bob), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_blackly(message : types.Message, state:FSMContext):
    try:
        p, numbers_in_sled, a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4 = message.text.split()
        l1 = [int(a1), int(a2), int(a3), int(a4)]
        l2 = [int(b1), int(b2), int(b3), int(b4)]
        l3 = [int(c1), int(c2), int(c3), int(c4)]
        two_dimension = [l1, l2, l3]
        filename = f'files/blackly-{generate_short_uuid()}.docx'
        ans = blackly.blackly(int(p), int(numbers_in_sled), two_dimension, filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_shamir(message : types.Message, state:FSMContext):
    try:
        p, x1, y1, x2, y2, x3, y3 = message.text.split()
        filename = f'files/shamir-{generate_short_uuid()}.docx'
        ans = shamir.Shamir(int(p), int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            await bot.send_message(message.from_user.id, ans)
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
        
async def send_blom(message : types.Message, state:FSMContext):
    try:
        p, Ax, Ay, AxClosed, AyClosed, Bx, By, BxClosed, ByClosed = message.text.split()
        filename = f'files/blom-{generate_short_uuid()}.docx'
        ans = blom.Blom(int(p), int(Ax), int(Ay), int(AxClosed), int(AyClosed), int(Bx), int(By), int(BxClosed), int(ByClosed), filename)
        await state.finish()
        with open(filename, 'rb') as file:
            await bot.send_document(message.from_user.id, document=InputFile(file))
            os.remove(filename)
            time.sleep(0.75)
            await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)
    except Exception as e:
        await state.finish()
        await bot.send_message(message.from_user.id, f"Ошибка {e} при вводе данных", reply_markup=types.ReplyKeyboardRemove())
        time.sleep(0.75)
        await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать:", reply_markup=kb_tasks_3)