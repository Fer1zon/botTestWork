from aiogram.utils import executor
import sys
import os

from pathlib import Path

sys.path.append(os.path.dirname(__file__) + '/..')
os.chdir(Path(__file__).parent.parent)
from importantFiles.helps import bot, dp
from handlers.allRegisterHandlers import finalHandlerRegistrator
from importantFiles.ExecuteAtStartup.mainExecuteStartup import mainExecuteAtStartupFunction

from appShedulerFunc.Sample import scheduler
    










finalHandlerRegistrator(dp)












if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp,skip_updates=True, on_startup = mainExecuteAtStartupFunction())