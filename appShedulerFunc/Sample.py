from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot





async def send_message_time(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение отправлено через несколько секунд после старта бота')


async def send_message_cron(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение будет отправляться ежедневно в указанное время.')


async def send_message_interval(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение будет отправляться с интервалом в 1 минуту')






scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.add_job(send_message_cron, trigger='cron', hour=datetime.now().hour,
                minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.start()






async def get_age(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    await message.answer(f'Твой возраст:\r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Вот твои данные\r\n' \
                f'Имя {name}\r\n' \
                f'Фамилия {last_name}\r\n' \
                f'Возраст {message.text}'
    await message.answer(data_user)
    await state.clear()
    apscheduler.add_job("Функция", trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                        kwargs={'bot': bot, 'chat_id': message.from_user.id})#Аргументы
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot





async def send_message_time(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение отправлено через несколько секунд после старта бота')


async def send_message_cron(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение будет отправляться ежедневно в указанное время.')


async def send_message_interval(bot: Bot):
    await bot.send_message(5528605206, f'Это сообщение будет отправляться с интервалом в 1 минуту')






scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.add_job(send_message_cron, trigger='cron', hour=datetime.now().hour,
                minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': "Сюда нужно передать объект 'Bot'"})
scheduler.start()






async def get_age(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    await message.answer(f'Твой возраст:\r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Вот твои данные\r\n' \
                f'Имя {name}\r\n' \
                f'Фамилия {last_name}\r\n' \
                f'Возраст {message.text}'
    await message.answer(data_user)
    await state.clear()
    apscheduler.add_job("Функция", trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                        kwargs={'bot': bot, 'chat_id': message.from_user.id})#Аргументы