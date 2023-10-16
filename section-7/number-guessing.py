

# There is a random number 1 = 25 
# User is given 3 attempts to guess the number
# If the user is able to guess, they win 
# Else they loose 

import random 

random_number = random.randint(1, 26) 
MAX_ATTEMPTS  = 3 
current_attempts = 0 

while current_attempts < MAX_ATTEMPTS:
    user_guess = int(input("Guess the number: "))
    if user_guess == random_number:
        print("You Won!") 
        break 
    else:
        current_attempts += 1 
else:
    print("You have exhausted all the attempts. \n Please try again!") 






