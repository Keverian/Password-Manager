import database
# TODO: function that checks if the database exist, if not exist, ask for username and master password
def register():
    print("Let's setup an account.")
    username = input("Please input an username:")
    password = input("Please input a master password:")
    database.store_users()
    salt = database.get_salt(username)
    return password, salt

# TODO: function that display main menu options, incluuding: adding account/password, updating, deleting, displaying
def display_main_menu():
    print("Select following options:")
    print("1. Display records")
    print("2. Search records")
    print("3. Add records")
    print("4. Update records")
    print("5. Delete records")
    print("press q to quit")
    return input()

#Function that takes userinput, revalidate them, and return user's website, email, password, username as strings
def add_record_menu(key):
    print("Please input the following informations:")

    website_url = input("Website url: ").lower()
    while not website_url:
        website_url = input("Cannot be empty, please re-enter: ").lower()

    username = input("Username: ")

    user_email = input("User email: ")
    while not user_email:
        user_email = input("Cannot be empty, please re-enter: ")

    password = input("Password: ")
    while not password:
        password = input("Cannot be empty, please re-enter: ")

    database.store_passwords(key, website_url, password, user_email, username)



def update_pw_menu(key):
    url = input("Input the website's url you wish to update your password for: ")
    pw = input("What is the new password: ")
    #check = input("The updated password is: " + pw + "\nIs this correct? (Y/N)").lower()
    database.update_pw(key, url, pw)

def delete_account_menu():
    url = input("What is the FULL url of the website?")
    database.delete_account(url)



