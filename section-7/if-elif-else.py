

'''
if condition: 
    <block of code> 
elif condition:
    <block of code> 
else:
    <block of code> 
'''


user_input = input("Enter a number: \n ~$ ") 
user_input = int(user_input) 

if user_input == 0:
    print("The number is Zero")
elif user_input > 0:
    print("The number is positive") 
else:
    print("The number is negative") 

