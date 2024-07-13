from sqlite3 import Cursor, Connection
from datetime import datetime

from appShedulerFunc.Sample import scheduler, notification

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def addTask(title : str, description : str, notificationStatus : bool, deadline : datetime, userId : str, cur : Cursor, conn: Connection, bot):

    record = cur.execute("INSERT INTO task (userId, title, description, datetime) VALUES(?, ?, ?, ?)", (userId, title, description, deadline))
    conn.commit()

    recordId = str(record.lastrowid)
    
    

    scheduler.add_job(notification, trigger="date", id = recordId, run_date = deadline, args=[userId, recordId, notificationStatus, cur, conn, bot])


def countMyTask(userId : str, cur : Cursor):
    return cur.execute("SELECT COUNT(*) FROM task WHERE userId = ?", (userId,)).fetchone()[0]




def getMyTask(userId : str, cur : Cursor, limit : int = 100, offset: int = 0):
    
    return cur.execute("SELECT id, title, datetime, status FROM task WHERE userId = ? ORDER BY datetime DESC LIMIT ? OFFSET ?", (userId, limit, offset,))



def getTaskKeyboard(userId : str, cur : Cursor):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for data in getMyTask(userId, cur):
        taskId = data[0]
        taskTitle = data[1]
        taskDatetime = data[2]
        taskStatus = data[3]
        
        buttonText = f"{taskTitle} - {taskDatetime}"
        if taskStatus == "Ожидает":
            buttonText += "⚪"

        elif taskStatus == "Закрыто":
            buttonText += "🔴"

        button = InlineKeyboardButton(buttonText, callback_data=f"task|{taskId}")
        keyboard.add(button)

    return keyboard




def checkTaskInDB(taskId : str, cur : Cursor):
    if cur.execute("SELECT * FROM task WHERE id = ?", (taskId,)).fetchone() is not None:
        return True
    
    return False




def getTaskData(taskId : str, cur : Cursor):
    data = cur.execute("SELECT title, description, datetime, status FROM task WHERE id = ?", (taskId,)).fetchone()

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Удалить из списка", callback_data=f"deleteTask|{taskId}"))
    if data[3] != "Выполнено":
        keyboard.add(InlineKeyboardButton("Задача выполнена✅", callback_data=f"taskComplete|{taskId}"))

    return {
        "title" : data[0],
        "description" : data[1],
        "datetime" : data[2],
        "status" : data[3],
        "sendKeyboard" : keyboard
            }


def deleteTaskFromDB(taskId, cur:Cursor, conn:Connection):
    cur.execute("DELETE FROM task WHERE id =?", (taskId,))
    conn.commit()
    scheduler.remove_job(taskId)





    





    










    