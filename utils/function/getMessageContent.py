from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from pathlib import Path








def getMainMenuContent():
    

    addTask = KeyboardButton("Добавить задачу 📝")
    taskList = KeyboardButton("Список задач 📋")

    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(addTask, taskList)

    sendText = "Добро пожаловать в бота"


    return {
        "sendText": sendText,
        "sendKeyboard" : keyboard
    }
    