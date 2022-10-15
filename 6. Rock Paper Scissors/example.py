# import the random module
import random
# create a function to get the player's choice
def get_player_choice():
    # get the player's choice
    choice = input("Rock, paper, or scissors? ")
    # return the choice
    return choice
# create a function to get the computer's choice
def get_computer_choice():
    # get the computer's choice
    choice = random.choice(["rock", "paper", "scissors"])
    # return the choice
    return choice
# create a function to check if the player won
def check_win(player, computer):
    # if the player and computer chose the same thing
    if player == computer:
        # print that it is a tie
        print("It's a tie!")
    # if the player chose rock
    elif player == "rock":
        # if the computer chose paper
        if computer == "paper":
            # print that the computer won
            print("The computer won!")
        # if the computer chose scissors
        else:
            # print that the player won
            print("You won!")
    # if the player chose paper
    elif player == "paper":
        # if the computer chose scissors
        if computer == "scissors":
            # print that the computer won
            print("The computer won!")
        # if the computer chose rock
        else:
            # print that the player won
            print("You won!")
    # if the player chose scissors
    else:
        # if the computer chose rock
        if computer == "rock":
            # print that the computer won
            print("The computer won!")
        # if the computer chose paper
        else:
            # print that the player won
            print("You won!")
# create a function to play the game
def play_game():
    # define the variables
    player = ""
    computer = ""
    # loop until the player enters a valid choice
    while player not in ["rock", "paper", "scissors"]:
        # get the player's choice
        player = get_player_choice()
        # if the player's choice is not valid
        if player not in ["rock", "paper", "scissors"]:
            # print that the choice is not valid
            print("That is not a valid choice.")
    # get the computer's choice
    computer = get_computer_choice()
    # print the player's choice
    print("You chose " + player + ".")
    # print the computer's choice
    print("The computer chose " + computer + ".")
    # check if the player won
    check_win(player, computer)
# play the game
play_game()