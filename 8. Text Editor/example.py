# import the os module
import os
# create a function to get the file name
def get_file_name():
    # get the file name
    file_name = input("File name: ")
    # return the file name
    return file_name
# create a function to get the file contents
def get_file_contents():
    # define the variables
    contents = ""
    line = ""
    # loop until the user enters an empty line
    while line != "":
        # get a line of text
        line = input()
        # add the line to the contents
        contents += line + " "
    # return the contents
    return contents
# create a function to save the file
def save_file(file_name, contents):
    # open the file
    file = open(file_name, "w")
    # write the contents to the file
    file.write(contents)
    # close the file
    file.close()
# create a function to open the file
def open_file(file_name):
    # open the file
    file = open(file_name, "r")
    # read the contents
    contents = file.read()
    # close the file
    file.close()
    # return the contents
    return contents
# create a function to display the menu
def display_menu():
    # display the menu
    print("1. Open file")
    print("2. Save file")
    print("3. Exit")
    # get the user's choice
    choice = int(input("Choice: "))
    # return the choice
    return choice
# create the main function
def main():
    # define the variables
    file_name = ""
    contents = ""
    choice = 0
    # loop until the user chooses to exit
    while choice != 3:
        # display the menu
        choice = display_menu()
        # if the user chose to open a file
        if choice == 1:
            # get the file name
            file_name = get_file_name()
            # open the file
            contents = open_file(file_name)
            # display the contents
            print(contents)
        # if the user chose to save a file
        elif choice == 2:
            # get the file name
            file_name = get_file_name()
            # get the file contents
            contents = get_file_contents()
            # save the file
            save_file(file_name, contents)
        # if the user chose to exit
        elif choice == 3:
            # exit the program
            exit()
        # if the user chose an invalid option
        else:
            # display an error message
            print("Invalid choice.")
# call the main function
main()
