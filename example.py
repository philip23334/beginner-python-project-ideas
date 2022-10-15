import sqlite3

def create_account():
    # get the username
    username = input("Username: ")
    # get the password
    password = input("Password: ")
    # create the database
    database = sqlite3.connect("passwords.db")
    # create the cursor
    cursor = database.cursor()
    # create the table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (username TEXT, password TEXT)")
    # add the username and password to the database
    cursor.execute("INSERT INTO passwords VALUES (?, ?)", (username, password))
    # save the changes
    database.commit()
    # close the database
    database.close()
# create a function to get the password of an account
def get_password():
    # get the username
    username = input("Username: ")
    # create the database
    database = sqlite3.connect("passwords.db")
    # create the cursor
    cursor = database.cursor()
    # get the password
    cursor.execute("SELECT password FROM passwords WHERE username = ?", (username,))
    # store the password
    password = cursor.fetchone()
    # close the database
    database.close()
    # if the password exists
    if password:
        # return the password
        return password[0]
    # if the password doesn't exist
    else:
        # return None
        return None
# create a function to update the password of an account
def update_password():
    # get the username
    username = input("Username: ")
    # get the new password
    new_password = input("New Password: ")
    # create the database
    database = sqlite3.connect("passwords.db")
    # create the cursor
    cursor = database.cursor()
    # update the password
    cursor.execute("UPDATE passwords SET password = ? WHERE username = ?", (new_password, username))
    # save the changes
    database.commit()
    # close the database
    database.close()
# create a function to delete an account
def delete_account():
    # get the username
    username = input("Username: ")

    # create the database
    database = sqlite3.connect("passwords.db")
    # create the cursor
    cursor = database.cursor()
    # delete the account
    cursor.execute("DELETE FROM passwords WHERE username = ?", (username,))
    # save the changes
    database.commit()
    # close the database
    database.close()
# create a function to display the menu
def display_menu():
    # display the menu
    print("1. Create Account")
    print("2. Get Password")
    print("3. Update Password")
    print("4. Delete Account")
    print("5. Exit")
# create a function to get the user's choice
def get_choice():
    # get the user's choice
    choice = input("Choice: ")
    # return the user's choice
    return choice
# create a function to run the program
def run():
    # create a variable to store the user's choice
    choice = ""
    # while the user's choice is not 5
    while choice != "5":
        # display the menu
        display_menu()
        # get the user's choice
        choice = get_choice()
        # if the user's choice is 1
        if choice == "1":
            # create an account
            create_account()
        # if the user's choice is 2
        elif choice == "2":
            # get the password
            password = get_password()
            # if the password exists
            if password:
                # display the password
                print("Password: " + password)
            # if the password doesn't exist
            else:
                # display the error message
                print("Account doesn't exist")
        # if the user's choice is 3
        elif choice == "3":
            # update the password
            update_password()
        # if the user's choice is 4
        elif choice == "4":
            # delete the account
            delete_account()
# call the run function
run()