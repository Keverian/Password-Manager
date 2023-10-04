import database as db
import sqlite3

#db.create_database()
#db.store_passwords("pepenike.com","password", "somethin@gmail.com", "kevin")
#db.store_passwords("nike695.com","password", "somethin@gmail.com", "pepega")
import secret

"""
con = sqlite3.connect("my_database.db")
cur = con.cursor()
name = "nike"
cur.execute("SELECT * FROM pwManager WHERE website_url LIKE ('%' ||?|| '%')", (name,))
rows = cur.fetchall()
for row in rows:
    print(row)
"""

con = sqlite3.connect("my_database.db")
cur = con.cursor()
userInput = "pepenike"
username = "new username"
user_email ="otherthing@gmail.com"
password = "new password"
#userinput must be the website name or url
cur.execute("UPDATE pwManager SET username = ?, user_email = ?, password = ? WHERE website_url LIKE ('%' ||?|| '%')", (username, user_email, password, userInput,))
con.commit()
con.close()

con = sqlite3.connect("my_database.db")
cur = con.cursor()

cur.execute("SELECT * FROM pwManager WHERE website_url LIKE ('%' ||?|| '%')", (userInput,))

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

            print("Password: ")
            continue
        print(col)

con.close()

con = sqlite3.connect("my_database.db")
cur = con.cursor()
cur.execute("SELECT (*) from pwManager WHERE username = ?", (username,))