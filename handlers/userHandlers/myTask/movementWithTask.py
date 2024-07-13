from datetime import datetime
import sys 
import os 

sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from userHandlers import keyboard as kb

from aiogram import types


from utils.function.database.task import getTaskKeyboard, countMyTask, checkTaskInDB, getTaskData, deleteTaskFromDB
from utils.function.getMessageContent import getMainMenuContent


async def deleteTask(call:types.CallbackQuery):
    taskId = call.data.split('|')[1]

    if not checkTaskInDB(taskId, cur):
        return await call.answer("Такой таски не существует")
    
    await call.message.delete()

    deleteTaskFromDB(taskId, cur, conn)

    if countMyTask(call.from_user.id, cur) == 0:
        content = getMainMenuContent()

        await call.message.answer("У вас больше нет задач")
        await call.message.answer(content["sendText"], reply_markup=content['sendKeyboard'])

    else:
        keyboard = getTaskKeyboard(call.from_user.id, cur)

        await call.message.answer("Таска удалена", reply_markup=keyboard)
