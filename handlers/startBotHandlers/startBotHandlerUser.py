from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from utils.function.getGreetingMessageContent import getGreetingMessageContent






async def startBotHandlerUser(message : types.Message):
    pass
    