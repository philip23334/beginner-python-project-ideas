
# this has an problem, try and fix it

import os
import random
import sys

# create a function to display the board
def display_board(board):
    # clear the screen
    os.system("cls")
    # display the board
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])
# create a function to get the player's move
def player_input():
    # define the variables
    marker = ""
    # get the player's marker
    marker = input("Player 1, choose X or O: ").upper()
    # loop until the player chooses X or O
    while marker != "X" and marker != "O":
        # get the player's marker
        marker = input("Player 1, choose X or O: ").upper()
    # if the player chose X
    if marker == "X":
        # return the player's marker and the computer's marker
        return ("X", "O")
    # if the player chose O
    else:
        # return the player's marker and the computer's marker
        return ("O", "X")
# create a function to place a marker on the board
def place_marker(board, marker, position):
    # place the marker on the board
    board[position] = marker
# create a function to check if someone won
def win_check(board, mark):
    # check if the player won
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))
# create a function to randomly choose who goes first
def choose_first():
    # get a random number
    num = random.randint(1, 2)
    # if the number is 1
    if num == 1:
        # return player 1
        return "Player 1"
    # if the number is 2
    else:
        # return player 2
        return "Player 2"
# create a function to check if a space on the board is free
def space_check(board, position):
    # check if the space is free
    return board[position] == " "
# create a function to check if the board is full
def full_board_check(board):
    # check if the board is full
    return " " not in board
# create a function to get the player's next move
def player_choice(board):
    # define the variables
    position = 0
    # get the player's next move
    position = int(input("Choose your next position: "))
    # loop until the player chooses a free space
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # get the player's next move
        position = int(input("Choose your next position: "))
    # return the player's next move
    return position
# create a function to ask the player if they want to play again
def replay():
    # get the player's answer
    answer = input("Do you want to play again? (y/n): ").lower()
    # loop until the player chooses y or n
    while answer != "y" and answer != "n":
        # get the player's answer
        answer = input("Do you want to play again? (y/n): ").lower()
    # if the player chooses y
    if answer == "y":
        # return True
        return True
    # if the player chooses n
    else:
        # return False
        return False
# define the main function
def main():
    # define the variables
    board = [" "] * 10
    player1_marker = ""
    player2_marker = ""
    turn = ""
    play_game = ""
    # display the board
    display_board(board)
    # get the player's marker
    player1_marker, player2_marker = player_input()
    # choose who goes first
    turn = choose_first()
    # print who goes first
    print(turn + " goes first.")
    # ask the player if they want to play
    play_game = input("Are you ready to play? (y/n): ").lower()
    # loop until the player chooses y or n
    while play_game != "y" and play_game != "n":
        # ask the player if they want to play
        play_game = input("Are you ready to play? (y/n): ").lower()
    # if the player chooses y
    if play_game == "y":
        # set the game to True
        game_on = True
    # if the player chooses n
    else:
        # set the game to False
        game_on = False
    # loop until the game is over
    while game_on:
        # if it's player 1's turn
        if turn == "Player 1":
            # display the board
            display_board(board)
            # get the player's next move
            position = player_choice(board)
            # place the player's marker on the board
            place_marker(board, player1_marker, position)
            # check if the player won
            if win_check(board, player1_marker):
                # display the board
                display_board(board)
                # print that the player won
                print("Player 1 won!")
                # set the game to False
                game_on = False
            # check if the board is full
            elif full_board_check(board):
                # display the board
                display_board(board)
                # print that the game is a tie
                print("The game is a tie!")
                # set the game to False
                game_on = False
            # if the player didn't win and the board isn't full
            else:
                # switch to player 2's turn
                turn = "Player 2"
        # if it's player 2's turn
        else:
            # display the board
            display_board(board)
            # get the player's next move
            position = player_choice(board)
            # place the player's marker on the board
            place_marker(board, player2_marker, position)
            # check if the player won
            if win_check(board, player2_marker):
                # display the board
                display_board(board)
                # print that the player won
                print("Player 2 won!")
                # set the game to False
                game_on = False
            # check if the board is full
            elif full_board_check(board):
                # display the board
                display_board(board)
                # print that the game is a tie
                print("The game is a tie!")
                # set the game to False
                game_on = False
            # if the player didn't win and the board isn't full
            else:
                # switch to player 1's turn
                turn = "Player 1"
    # ask the player if they want to play again
    if not replay():
        # exit the program
        sys.exit()
# call the main function
main()