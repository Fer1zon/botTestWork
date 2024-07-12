from aiogram import types

from aiogram.dispatcher import FSMContext



import sys 
import os 
from handlers import generalKeyboard as kb
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, cur,conn

from utils.function.database.user import addUserInDB

from utils.function.getMessageContent import getMainMenuContent









async def getName(message:types.Message, state:FSMContext):
    await state.update_data(name = message.text)

    await message.answer("Отправьте ваш номер телефона. Или нажмите кнопку👇", reply_markup=kb.getNumberKb)
    await States.USER_PHONE_NUMBER.set()



async def getPhoneFromMessage(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        name = data["name"]
        phone = message.text

    addUserInDB(message.from_user.id, name, phone, cur, conn)

    content = getMainMenuContent()


    await message.answer(content["sendText"], reply_markup=content["sendKeyboard"])

    await States.USER_MAIN_MENU.set()
    await state.reset_data()


async def getPhoneFromButton(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        name = data["name"]
        phone = message.contact.phone_number

    addUserInDB(message.from_user.id, name, phone, cur, conn)

    content = getMainMenuContent()


    await message.answer(content["sendText"], reply_markup=content["sendKeyboard"])

    await States.USER_MAIN_MENU.set()
    await state.reset_data()





    