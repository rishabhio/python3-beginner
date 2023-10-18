

'''
    1. Unit of reusable code 
    2. They enhance readability 
    3. More maintainable code 
'''


'''
    Syntax of Functions in Python: 

def <function_name>( <parameters> 1, 2, 3 . . .): 
    """
        Doc String: Describes why this fxn exists 
    """
    <block_of_code> 

    return <expression> 
'''


# # Example 1: 

# def greet():
#     '''
#         This functions greets the user. 
#     '''
#     print("Hello, Welcome to the world of Python!") 

# # Calling a Function 
# greet() 


## Example 2:

def greet_user( user ):
    '''
        Return a greeting for the user 
    '''
    greeting = f'Hello, {user}! How are you?'
    return greeting 


## Calling the function 

user_greeting = greet_user("Rishabh") 
print(user_greeting)
 
