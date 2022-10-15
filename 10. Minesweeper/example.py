# import the random module
import random
# create a function to get the number of rows
def get_rows():
    # get the number of rows
    rows = int(input("How many rows? "))
    # return the number of rows
    return rows
# create a function to get the number of columns
def get_columns():
    # get the number of columns
    columns = int(input("How many columns? "))
    # return the number of columns
    return columns
# create a function to get the number of mines
def get_mines():
    # get the number of mines
    mines = int(input("How many mines? "))
    # return the number of mines
    return mines
# create a function to create the board
def create_board(rows, columns):
    # define the variables
    board = []
    row = []
    count = 0
    # loop until all the rows have been created
    while count < rows:
        # loop until all the columns have been created
        while len(row) < columns:
            # add a space to the row
            row.append(" ")
        # add the row to the board
        board.append(row)
        # reset the row
        row = []
        # increment the count
        count += 1
    # return the board
    return board
# create a function to display the board
def display_board(board):
    # define the variables
    count = 0
    # loop through the board
    for row in board:
        # display the row
        print(row)
        # increment the count
        count += 1
# create a function to place the mines
def place_mines(board, mines):
    # define the variables
    count = 0
    # loop until all the mines have been placed
    while count < mines:
        # get a random row
        row = random.randint(0, len(board) - 1)
        # get a random column
        column = random.randint(0, len(board[0]) - 1)
        # if the space is not a mine
        if board[row][column] != "*":
            # place a mine
            board[row][column] = "*"
            # increment the count
            count += 1
    # return the board
    return board
# create a function to get the number of mines around a space
def get_mines_around(board, row, column):
    # define the variables
    count = 0
    # loop through the rows
    for r in range(row - 1, row + 2):
        # loop through the columns
        for c in range(column - 1, column + 2):
            # if the space is on the board
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                # if the space is a mine
                if board[r][c] == "*":
                    # increment the count
                    count += 1
    # return the count
    return count
# create a function to get the player's guess
def get_guess(board):
    # define the variables
    guess = []
    row = 0
    column = 0
    # get the row
    row = int(input("Guess a row: "))
    # get the column
    column = int(input("Guess a column: "))
    # add the row and column to the guess
    guess.append(row)
    guess.append(column)
    # return the guess
    return guess
# create a function to check the guess
def check_guess(board, guess):
    # define the variables
    row = guess[0]
    column = guess[1]
    # if the space is a mine
    if board[row][column] == "*":
        # return True
        return True
    # return False
    return False
# create a function to update the board
def update_board(board, guess):
    # define the variables
    row = guess[0]
    column = guess[1]
    # get the number of mines around the space
    mines = get_mines_around(board, row, column)
    # if there are no mines around the space
    if mines == 0:
        # set the space to a blank
        board[row][column] = " "
    # if there are mines around the space
    else:
        # set the space to the number of mines
        board[row][column] = str(mines)
    # return the board
    return board
# create a function to check if the game is over
def check_game_over(board):
    # define the variables
    count = 0
    # loop through the board
    for row in board:
        # loop through the row
        for space in row:
            # if the space is not a mine
            if space != "*":
                # increment the count
                count += 1
    # if the count is 0
    if count == 0:
        # return True
        return True
    # return False
    return False
# create a function to play the game
def play_game():
    # get the number of rows
    rows = get_rows()
    # get the number of columns
    columns = get_columns()
    # get the number of mines
    mines = get_mines()
    # create the board
    board = create_board(rows, columns)
    # place the mines
    board = place_mines(board, mines)
    # display the board
    display_board(board)
    # define the variables
    game_over = False
    # loop until the game is over
    while not game_over:
        # get the player's guess
        guess = get_guess(board)
        # check the guess
        game_over = check_guess(board, guess)
        # if the game is not over
        if not game_over:
            # update the board
            board = update_board(board, guess)
            # display the board
            display_board(board)
            # check if the game is over
            game_over = check_game_over(board)
    # display the board
    display_board(board)
    # if the game is over
    if game_over:
        # display a message
        print("Game over!")
# call the function to play the game
play_game()