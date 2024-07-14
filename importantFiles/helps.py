from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import sys
import os

if __package__:
    from . import config
else:
    sys.path.append(os.path.dirname(__file__) + '/..')
    import config


import sqlite3 




def sqliteLower(value_):
    return value_.lower()


conn = sqlite3.connect(config.dataBasePath)
cur = conn.cursor()

conn.create_function("LOWER", 1, sqliteLower)







bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot,storage=MemoryStorage())

class States(StatesGroup):  # Создаём состояния
    
    USER_NAME = State()
    USER_PHONE_NUMBER = State()


    USER_MAIN_MENU = State()
    

    USER_TITLE_TASK = State()
    USER_DESCRIPTION_TASK = State()
    USER_NOTIFICATION_TASK = State()
    USER_DATETIME_TASK = State()

    USER_LIST_TASK = State()
    USER_CHECK_TASK = State()