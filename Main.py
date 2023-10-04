import sqlite3

def create_database():
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            userName TEXT PRIMARY KEY,
            salt TEXT PRIMARY KEY,
            masterPassword TEXT PRIMARY KEY
         )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS pwManager(
            website TEXT NOT NULL,
            userName TEXT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )  
    ''')

    con.commit()
    con.close()




