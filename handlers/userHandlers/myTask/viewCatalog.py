from datetime import datetime
import sys 
import os 

sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from userHandlers import keyboard as kb

from aiogram import types

from utils.function.database.task import getTaskKeyboard, countMyTask, checkTaskInDB, getTaskData




from aiogram.dispatcher import FSMContext




async def responseListTasks(message:types.Message):
    if countMyTask(message.from_user.id, cur) == 0:
        return await message.answer("Пока что у вас нет задач. Создайте их!")
    
    keyboard = getTaskKeyboard(message.from_user.id, cur)
    
    

    await message.answer("Вы в списке ваших задач", reply_markup=kb.inMenuKb)
    await message.answer("Список ваших задач:", reply_markup=keyboard)

    await States.USER_LIST_TASK.set()


async def choiceTask(call: types.CallbackQuery, state:FSMContext):
    taskId = call.data.split("|")[1]

    if not checkTaskInDB(taskId, cur):
        return await call.answer("К сожалению такой задачи не существует")
    

    taskData = getTaskData(taskId, cur)

    sendText = f"""
Задача: <b>{taskData["title"]}</b>

<code>{taskData["description"]}</code>
Время исполнения: <i>{taskData["datetime"]}</i>
Статус: {taskData["status"]}"""
    
    await call.message.answer(sendText, reply_markup=taskData["sendKeyboard"])

    await States.USER_CHECK_TASK.set()
    


    





    





    
        

    
