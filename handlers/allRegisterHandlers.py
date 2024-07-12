from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser
from importantFiles.helps import States, dp,bot, cur,conn

from aiogram import types



from startBotHandlers.auth import getName, getPhoneFromMessage, getPhoneFromButton


def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    dp.register_message_handler(startBotHandlerUser, commands="start", state = "*")
    dp.register_message_handler(startBotHandlerAdmin, commands="start", state = "*")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    dp.register_message_handler(getName, content_types="text", state = States.USER_NAME)
    dp.register_message_handler(getPhoneFromMessage, content_types="text", state = States.USER_PHONE_NUMBER)
    dp.register_message_handler(getPhoneFromButton, content_types=types.ContentTypes.CONTACT, state = States.USER_PHONE_NUMBER)


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    pass




def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    pass





def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)