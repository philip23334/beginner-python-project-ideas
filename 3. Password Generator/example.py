# import the random module
import random

# define the main function
def main():
        
        # define the variables
        password = ""
        length = 0
        count = 0
        
        # get the length of the password
        length = int(input("Enter the length of the password: "))
        
        # loop until the password is the correct length
        while count < length:
            
            # get a random number
            num = random.randint(1, 3)
            
            # if the number is 1
            if num == 1:
                
                # add a random lowercase letter to the password
                password += chr(random.randint(97, 122))
                
            # if the number is 2
            elif num == 2:
                
                # add a random uppercase letter to the password
                password += chr(random.randint(65, 90))
                
            # if the number is 3
            else:
                
                # add a random number to the password
                password += str(random.randint(0, 9))
                
            # increment the count
            count += 1
            
        # display the password
        print("Your password is", password)

# call the main function
main()