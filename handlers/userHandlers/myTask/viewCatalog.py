from datetime import datetime
import sys 
import os 

sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from userHandlers import keyboard as kb

from aiogram import types

from utils.function.database.task import getMyTask, countMyTask


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




async def responseListTasks(message:types.Message):
    if countMyTask(message.from_user.id, cur) == 0:
        return await message.answer("Пока что у вас нет задач. Создайте их!")
    
    keyboard = InlineKeyboardMarkup(row_width=1)
    for data in getMyTask(message.from_user.id, cur):
        taskId = data[0]
        taskTitle = data[1]
        taskDatetime = data[2]
        taskStatus = data[3]
        
        buttonText = f"{taskTitle} - {taskDatetime}"
        if taskStatus == "Ожидает":
            buttonText += "⚪"

        elif taskStatus == "Закрыто":
            buttonText += "🔴"

        button = InlineKeyboardButton(buttonText, callback_data=f"task|{taskId}")
        keyboard.add(button)

    await message.answer("Вы в списке ваших задач", reply_markup=kb.inMenuKb)
    await message.answer("Список ваших задач:", reply_markup=keyboard)

    await States.USER_LIST_TASK.set()

    
        

    
