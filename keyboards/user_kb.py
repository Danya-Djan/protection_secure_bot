from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("Подтвердить данные")
b2 = KeyboardButton("Ввести новые")

kb_apply = ReplyKeyboardMarkup(resize_keyboard=True)

kb_apply.row(b1, b2)

b3 = KeyboardButton("Зарегистрироваться")
kb_register = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_register.add(b3)


b5 = KeyboardButton("Поделиться номером", request_contact=True)
kb_number = ReplyKeyboardMarkup(resize_keyboard=True)
kb_number.add(b5)

kb_qr = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b6 = KeyboardButton("Получить QR-код")
kb_qr.add(b6)
