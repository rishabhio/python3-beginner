


## Syntax 

# the condition has to evaluate to a boolean 
# block of code can contain any python code 
'''
    if <condition>: 
        <block of code> 
'''


## Example 1 

# Check whether the number given by user 
# as input is even or odd 

user_input = input("Enter a number: \n ~$ ") 
user_input = int(user_input) 

if user_input % 2 == 0:
    print("The number is Even") 

if user_input %2 != 0:
    print("The number is Odd") 


