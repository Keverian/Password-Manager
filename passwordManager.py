import os, database, menu
#create database
import secret, sys

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

#MAIN
database.create_database()
#check database is empty, if it is, ask for master password and username
key = 0
salt = 0
password = 0
#Loggings
if database.user_empty_check():
    #register an new master account
    print("Let's setup an account.")
    username = input("Please input an username:")
    password = input("Please input a master password:")
    database.store_users()
    salt = database.get_salt(username)
    key = secret.derive_key(password, salt)
else:
    username = input("Username: ")
    password = input("Password: ")
    check = database.check_master_password(username, password)
    while not check:
        print("Logging Failed")
        user_input = input("Would you like to try again?(y/n)").lower()
        if input == 'n':
            exit_program()
        username = input("Username: ")
        pw = input("Password: ")
        check = database.check_master_password(username, pw)
    key = secret.derive_key(password, salt)
del password
#TODO: Display Menu
menu_going = True
while menu_going:
    print("Main Menu:")
    menu_user_input = menu.display_main_menu()
    #TODO: Add userinput check
    #1.display record
    if menu_user_input == '1':
        database.display_all(key)
    #2.search record
    elif menu_user_input == '2':
        url = input("What is the URL for the website you are looking for: ")
        database.search_display(key, url)
    #3.add records
    elif menu_user_input == '3':
        menu.add_record_menu(key)
    #4.update records
    elif menu_user_input == '4':
        menu.update_pw_menu(key)
    #5.Delete records
    elif menu_user_input == '5':
        menu.delete_account_menu(key)











