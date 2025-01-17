from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser
from importantFiles.helps import States, dp,bot, cur,conn

from aiogram import types



from startBotHandlers.auth import getName, getPhoneFromMessage, getPhoneFromButton


from userHandlers.addTask.mainAddTask import responseAddTask, titleTask, descriptionTask, notificationTask, datetimeTask
from userHandlers.myTask.viewCatalog import responseListTasks, choiceTask, backInTask
from userHandlers.myTask.movementWithTask import deleteTask, completeTask
from userHandlers.myTask.searchTask import searchTask





from otherHandlers.mainOtherHandler import backInMenu


def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    dp.register_message_handler(startBotHandlerUser, commands="start", state = "*")
    dp.register_message_handler(startBotHandlerAdmin, commands="start", state = "*")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    dp.register_message_handler(getName, content_types="text", state = States.USER_NAME)
    dp.register_message_handler(getPhoneFromMessage, content_types="text", state = States.USER_PHONE_NUMBER)
    dp.register_message_handler(getPhoneFromButton, content_types=types.ContentTypes.CONTACT, state = States.USER_PHONE_NUMBER)

    dp.register_message_handler(backInMenu, lambda msg: msg.text == "В меню 🏠", state = "*")


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    dp.register_message_handler(responseAddTask, lambda msg: msg.text == "Добавить задачу 📝", state = States.USER_MAIN_MENU)
    dp.register_message_handler(titleTask, lambda msg: msg.text != "В меню 🏠", content_types="text", state = States.USER_TITLE_TASK)
    dp.register_message_handler(descriptionTask, lambda msg: msg.text != "В меню 🏠", content_types="text", state = States.USER_DESCRIPTION_TASK)
    dp.register_callback_query_handler(notificationTask, lambda call: call.data in ["True", "False"], state = States.USER_NOTIFICATION_TASK)
    dp.register_message_handler(datetimeTask, lambda msg: msg.text != "В меню 🏠", content_types="text", state = States.USER_DATETIME_TASK)


    dp.register_message_handler(responseListTasks, lambda msg: msg.text == "Список задач 📋", state = States.USER_MAIN_MENU)
    dp.register_callback_query_handler(backInTask, lambda call: call.data == "backInTasks", state = States.USER_CHECK_TASK)

    dp.register_message_handler(searchTask, lambda msg: msg.text != "В меню 🏠", state = States.USER_LIST_TASK)

    dp.register_callback_query_handler(choiceTask, lambda call: call.data.split("|")[0] == "task", state = States.USER_LIST_TASK)
    

    dp.register_callback_query_handler(deleteTask, lambda call: call.data.split("|")[0] == "deleteTask", state = States.USER_CHECK_TASK)
    dp.register_callback_query_handler(completeTask, lambda call: call.data.split("|")[0] == "taskComplete", state = States.USER_CHECK_TASK)


def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    pass





def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)