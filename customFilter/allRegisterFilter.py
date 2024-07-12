import sys 
import os

from aiogram.dispatcher import Dispatcher

sys.path.append(os.path.dirname(__file__) + '/..')

from customFilter.isAdmin import IsAdmin







def registerAllFilter(dp:Dispatcher):
    dp.filters_factory.bind(IsAdmin)