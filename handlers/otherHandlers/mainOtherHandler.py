from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from utils.function.getMessageContent import getMainMenuContent





async def backInMenu(message:types.Message, state:FSMContext):
    await state.reset_data()

    content = getMainMenuContent()

    await message.answer(content["sendText"], reply_markup=content["sendKeyboard"])
    await States.USER_MAIN_MENU.set()
