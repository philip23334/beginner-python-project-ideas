# import the random module
import random

# define the main function
def main():
    
    # define the variables
    guess = 0
    count = 0
    number = random.randint(1, 100)
    # print(number)
    
    # get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))
    
    # loop until the player guesses the number or runs out of guesses
    while guess != number and count < 10:
        
        # if the guess is too high
        if guess > number:
            print("Too high!")
            
        # if the guess is too low
        else:
            print("Too low!")
            
        # get the next guess
        guess = int(input("Guess again: "))
        
        # increment the count
        count += 1
        
    # if the player guessed the number
    if guess == number:
        print("You guessed it!")
        
    # if the player ran out of guesses
    else:
        print("You ran out of guesses!")

# call the main function
main()