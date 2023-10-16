
# break 
# continue 
# Used with loops 

# break 
# continue 

# counter = 0 
# while counter < 10:
#     counter += 1 
#     if counter == 5: 
#         print(counter) 
#     continue 


# print("Out of the loop") 
attempts = 0 
MAX_ATTEMPTS = 4 
correct_pin = "1234"

while attempts < MAX_ATTEMPTS:
    user_pin = input("Enter your Pin: \n ~$ ") 

    if not user_pin:
        print("You did not enter a pin. Please enter the pin") 
        continue 

    if user_pin == correct_pin: 
        print("Please wait while we process your request") 
        break 

    else:
        attempts += 1 
        print(f"Incorrect pin. { MAX_ATTEMPTS- attempts } attempts remaining") 

if attempts == MAX_ATTEMPTS:
    print("Too many attempts. Card Blocked") 
f

print("Thanks for using demo ATM") 