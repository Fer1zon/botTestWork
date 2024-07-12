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

conn = sqlite3.connect(config.dataBasePath)
cur = conn.cursor()







bot = Bot(token=config.TEST_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

class States(StatesGroup):  # Создаём состояния
    
    pass
