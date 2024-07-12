from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

inMenu = KeyboardButton("В меню 🏠")
inMenuKb = ReplyKeyboardMarkup(resize_keyboard=True).add(inMenu)


yes = InlineKeyboardButton("Да", callback_data="True")
no = InlineKeyboardButton("Нет", callback_data="False")

yesNoKb = InlineKeyboardMarkup().add(yes, no)
