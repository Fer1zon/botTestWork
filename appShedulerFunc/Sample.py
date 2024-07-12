from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from sqlite3 import Connection, Cursor






scheduler = AsyncIOScheduler()




def changeStatus(taskId, newStatus, cur:Cursor, conn:Connection):
    cur.execute("UPDATE task SET status =? WHERE id =?", (newStatus, taskId))
    conn.commit()





async def notification(userId : str, taskId : int, sendNotification : bool, cur : Cursor, conn:Connection, bot:Bot):
    changeStatus(taskId, "Закрыто", cur, conn)
    
    if sendNotification:

        data = cur.execute("SELECT title, description FROM task WHERE id = ?", (taskId,)).fetchone()
        title = data[0]
        description = data[1]

        sendText = f"""Напоминание о задаче: <b>{title}</b>
<code>{description}</code>"""
        
        await bot.send_message(userId, sendText)

    

    
        

        
        
        


