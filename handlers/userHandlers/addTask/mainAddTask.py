from datetime import datetime
import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from userHandlers import keyboard as kb

from aiogram import types

from aiogram.dispatcher import FSMContext


from utils.function.database.task import addTask


from utils.function.getMessageContent import getMainMenuContent




async def responseAddTask(message:types.Message):
    sendText = "Отправьте в чат название задачи"

    await message.answer(sendText, reply_markup=kb.inMenuKb)
    await States.USER_TITLE_TASK.set()


async def titleTask(message:types.Message, state:FSMContext):
    await state.update_data(title = message.text)

    sendText = "Отправьте описание задачи"
    await message.answer(sendText)
    await States.USER_DESCRIPTION_TASK.set()


async def descriptionTask(message:types.Message, state:FSMContext):
    await state.update_data(description = message.text)

    sendText = "Уведомлять ли вас о том что нужно выполнить задачу?"

    await message.answer(sendText, reply_markup=kb.yesNoKb)
    await States.USER_NOTIFICATION_TASK.set()


async def notificationTask(call:types.CallbackQuery, state:FSMContext):
    if call.data == "True":
        await state.update_data(notification = True)

    else:
        await state.update_data(notification = False)


    sendText = "Отправьте дедлайн задачи в формате: 'DD.MM.YYYY HH:MM'"

    await call.message.edit_text(sendText)
    await States.USER_DATETIME_TASK.set()


async def datetimeTask(message:types.Message, state:FSMContext):
    try:
        deadline = message.text
        deadline = datetime.strptime(deadline, '%d.%m.%Y %H:%M')

    except:
        return await message.answer("Нарушен формат ввода даты и времени. Попробуйте снова: 'DD.MM.YYYY HH:MM'")
    
    if datetime.now() > deadline:
        return await message.answer("Вы выбрали дату которая уже прошла")
    

    async with state.proxy() as data:
        
        title = data["title"]
        description = data["description"]
        notification = data["notification"]

    print(notification)
    addTask(title, description, notification, deadline, message.from_user.id, cur, conn, bot)



    content = getMainMenuContent()

    await message.answer("Задача создана!")
    await message.answer(content["sendText"], reply_markup=content["sendKeyboard"])

    await States.USER_MAIN_MENU.set()



