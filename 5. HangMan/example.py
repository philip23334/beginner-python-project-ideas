# import the random module
import random
# create a function to display the board
def display_board(board):
    # print the board
    print(" ".join(board))
# create a function to get the player's guess
def get_guess():
    # get the player's guess
    guess = input("Guess a letter: ")
    # return the guess
    return guess
# create a function to check if the player's guess is in the word
def check_guess(guess, word, board):
    # if the guess is in the word
    if guess in word:
        # loop through the word
        for i in range(len(word)):
            # if the guess is in the word
            if guess == word[i]:
                # replace the dash with the guess
                board[i] = guess
    # if the guess is not in the word
    else:
        # print that the guess is not in the word
        print("That letter is not in the word.")
# create a function to check if the player has won
def check_win(board):
    # if there are no dashes in the board
    if "-" not in board:
        # return True
        return True
    # if there are dashes in the board
    else:
        # return False
        return False
# create a function to play the game
def play_game():
    # define the variables
    word = random.choice(["python", "java", "kotlin", "javascript"])
    board = ["-" for i in range(len(word))]
    guesses = []
    # loop until the player wins or loses
    while True:
        # display the board
        display_board(board)
        # get the player's guess
        guess = get_guess()
        # if the player's guess is not a letter
        if not guess.isalpha():
            # print that the guess is not a letter
            print("That is not a letter.")
        # if the player's guess is more than one letter
        elif len(guess) > 1:
            # print that the guess is more than one letter
            print("That is more than one letter.")
        # if the player's guess is a letter
        else:
            # if the player's guess is in the guesses list
            if guess in guesses:
                # print that the player has already guessed the letter
                print("You have already guessed that letter.")
            # if the player's guess is not in the guesses list
            else:
                # add the guess to the guesses list
                guesses.append(guess)
                # check if the guess is in the word
                check_guess(guess, word, board)
                # check if the player has won
                if check_win(board):
                    # display the board
                    display_board(board)
                    # print that the player has won
                    print("You won!")
                    # break out of the loop
                    break
# create a function to play again
def play_again():
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
    # loop until the player chooses not to play again
    while True:
        # play the game
        play_game()
        # check if the player wants to play again
        if not play_again():
            # break out of the loop
            break
# call the main function
main()