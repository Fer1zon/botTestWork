import sys 
import os 

sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, cur,conn

from userHandlers import keyboard as kb

from aiogram import types

from utils.function.database.task import searchTasks




async def searchTask(message:types.Message):
    searchTitle = message.text
    sendText = "Найденные результаты:"

    result = searchTasks(searchTitle, message.from_user.id, cur)

    if not result:
        return await message.answer("По вашему запросу ничего не найдено!")
    

    await message.answer(sendText, reply_markup=result)



