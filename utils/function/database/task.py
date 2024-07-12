from sqlite3 import Cursor, Connection
from datetime import datetime

from appShedulerFunc.Sample import scheduler, notification



def addTask(title : str, description : str, notificationStatus : bool, deadline : datetime, userId : str, cur : Cursor, conn: Connection, bot):

    record = cur.execute("INSERT INTO task (userId, title, description, datetime) VALUES(?, ?, ?, ?)", (userId, title, description, deadline))
    conn.commit()

    recordId = str(record.lastrowid)
    
    

    scheduler.add_job(notification, trigger="date", id = recordId, run_date = deadline, args=[userId, recordId, notificationStatus, cur, conn, bot])






    





    










    