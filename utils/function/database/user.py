from sqlite3 import Cursor, Connection



def checkUserInDB(userId, cur:Cursor) -> bool:
    """Если пользователь есть в базе, то вернет True, если нет - False"""
    if cur.execute("SELECT * FROM user WHERE id = ?", (userId,)).fetchone() is None:
        return False 
    
    return True


def addUserInDB(userId, name, phone, cur:Cursor, conn:Connection) -> None:
    """Добавляет нового пользователя в базу"""
    cur.execute("INSERT INTO user VALUES(?,?,?)", (userId, name, phone))
    conn.commit()


    