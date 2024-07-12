
from ...helps import cur, conn




def createUserTable():#Создание юзерских таблиц

    cur.execute("""CREATE TABLE IF NOT EXISTS user (
    id       TEXT PRIMARY KEY NOT NULL,
    name TEXT,
    phone TEXT
);


""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS task (
    id          TEXT PRIMARY KEY,
    userId      TEXT REFERENCES user (id),
    title       TEXT,
    description TEXT,
    datetime    DATETIME,
    status      TEXT
);


""")
    

    conn.commit()






def createAdminTable():#Создание админских таблиц
    pass