from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



getPhoneNumber = KeyboardButton("Предоставить номер", request_contact=True)
getNumberKb = ReplyKeyboardMarkup(resize_keyboard=True).add(getPhoneNumber)