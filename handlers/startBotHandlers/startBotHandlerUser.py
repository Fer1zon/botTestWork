from aiogram import types

from aiogram.dispatcher import FSMContext





import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from utils.function.database.user import checkUserInDB
from utils.function.getMessageContent import getMainMenuContent






async def startBotHandlerUser(message : types.Message, state:FSMContext):
    if not checkUserInDB(message.from_user.id, cur):
        await message.answer("Для использования бота, нужно зарегистрироваться")
        await message.answer("Ваше имя?")
        await States.USER_NAME.set()
        return 
    
    await state.reset_data()

    content = getMainMenuContent()

    await message.answer(content["sendText"], reply_markup=content["sendKeyboard"])
    await States.USER_MAIN_MENU.set()






    