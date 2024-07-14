from datetime import datetime
import sys 
import os 

sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from userHandlers import keyboard as kb

from aiogram import types


from utils.function.database.task import getTasksKeyboard, countMyTask, checkTaskInDB, changeTaskStatus, deleteTaskFromDB, getTaskData
from utils.function.getMessageContent import getMainMenuContent

from appShedulerFunc.Sample import removeJob


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
        await States.USER_MAIN_MENU.set()

    else:
        keyboard = getTasksKeyboard(call.from_user.id, cur)

        await call.message.answer("Таска удалена", reply_markup=keyboard)
        await States.USER_LIST_TASK.set()


async def completeTask(call:types.CallbackQuery):
    taskId = call.data.split('|')[1]

    if not checkTaskInDB(taskId, cur):
        return await call.answer("Такой таски не существует")
    
    changeTaskStatus(taskId, "Выполнено", cur, conn)

    newContent = getTaskData(taskId, cur)
    sendText = f"""
Задача: <b>{newContent["title"]}</b>

<code>{newContent["description"]}</code>
Время исполнения: <i>{newContent["datetime"]}</i>
Статус: {newContent["status"]}"""
    
    removeJob(taskId)
    await call.answer("Статус изменен")
    await call.message.edit_text(sendText, reply_markup=newContent["sendKeyboard"])

    


    
    
    