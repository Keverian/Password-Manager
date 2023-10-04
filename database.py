import sqlite3
import secret
#Create database
def create_database():
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY NOT NULL,
            salt TEXT KEY NOT NULL,
            master_password TEXT KEY NOT NULL
         )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS pwManager(
            website_url TEXT PRIMARY NOT NULL,
            username TEXT,
            user_email TEXT NOT NULL,
            password TEXT NOT NULL
        )  
    ''')

    con.commit()
    con.close()

#Store passwords into pwManager
def store_passwords(key, website, password, user_email,username=""):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    pw = secret.encrypt_pw(key, password)

    cur.execute('INSERT INTO pwManager (website_url, username, user_email, password) VALUES (?,?,?,?)', (website, username, user_email, password))

    con.commit()
    con.close()

def store_users(username, mp):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    #TODO: add single user stored in database check

    salt = secret.gen_salt()
    hashed_password = secret.hash_master_password(mp, salt)

    cur.execute('INSERT INTO users (username, salt, master_password) VALUES (?,?,?)',
                (username, salt, hashed_password))

    con.commit()
    con.close()


def get_salt(name):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    cur.execute('SELECT salt FROM users WHERE username =?', (name, ))
    salt = cur.fetchone()

    con.close()

    return salt


def display_all(key):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    cur.execute('SELECT * FROM pwManager')

    rows = cur.fetchall()

    for row in rows:
        for count, col in enumerate(row):
            if count == 0:
                print("Website Url: ", end="")
            elif count == 1:
                print("Username: ", end="") #make sure all empty username is in empty string and not null
            elif count == 2:
                print("Email: ", end="")
            elif count == 3:
                pw = secret.decrypt_pw(key, col)
                print("Password: " + pw)
                continue
            print(col)

    con.close()

#Function that takes a fetch from sqlite3 search return and display them
def display_fetched(key, fetch):
    for row in fetch:
        for count, col in enumerate(row):
            if count == 0:
                print("Website Url: ", end="")
            elif count == 1:
                print("Username: ", end="") #make sure all empty username is in empty string and not null
            elif count == 2:
                print("Email: ", end="")
            elif count == 3:
                pw = secret.decrypt_pw(key, col)
                print("Password: " + pw)
                continue
            print(col)

def search_display(key, url):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM pwManager WHERE website_url LIKE ('%' ||?|| '%')", (url,))
    rows = cur.fetchall()
    display_fetched(key, rows)
    con.close()



def update_pw(key, url, pw):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    pw = secret.encrypt_pw(key, pw)
    #userinput must be the website name or url
    cur.execute(
        "UPDATE pwManager SET password = ? WHERE website_url LIKE ('%' ||?|| '%')",
        (pw, url,))
    con.commit()

def delete_account(url):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM pwManager WHERE website_url = ?", (url,))
    con.commit()
    con.close()

def user_empty_check():
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    cur.execute("SELECT count(*) from users")
    count = cur.fetchone()[0]
    con.close()
    if not count:
        return True
    return False

def check_master_password(username, password):
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    cur.execute("SELECT * from users WHERE username = ?", (username,))
    row = cur.fetchone()
    if len(row) == 0:
        print("Username do not exist.")
        return False
    input_pw = secret.hash_master_password(password, row[1])
    con.close()
    if input_pw == row[2]:
        return True
    return False

