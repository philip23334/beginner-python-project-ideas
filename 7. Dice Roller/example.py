# import the random module
import random
# create a function to get the number of sides
def get_sides():
    # get the number of sides
    sides = int(input("How many sides? "))
    # return the number of sides
    return sides
# create a function to get the number of dice
def get_dice():
    # get the number of dice
    dice = int(input("How many dice? "))
    # return the number of dice
    return dice
# create a function to roll the dice
def roll_dice(sides, dice):
    # define the variables
    count = 0
    total = 0
    # loop until all the dice have been rolled
    while count < dice:
        # get a random number
        num = random.randint(1, sides)
        # add the number to the total
        total += num
        # increment the count
        count += 1
    # return the total
    return total
# create a function to display the results
def display_results(total):
    # display the results
    print("You rolled a", total)
# create the main function
def main():
    # define the variables
    sides = 0
    dice = 0
    total = 0
    # get the number of sides
    sides = get_sides()
    # get the number of dice
    dice = get_dice()
    # roll the dice
    total = roll_dice(sides, dice)
    # display the results
    display_results(total)
# call the main function
main()