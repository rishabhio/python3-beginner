

'''
1. Assign functions to variables. 
2. Pass functions as args to other fxns. 
3. Return functions as value from other fxns. 

'''

#1. Assign functions to variables.

def greet():
    return "Hello First Class Citizens" 

greet_fxn = greet 
print( greet_fxn()) 


#2. Pass functions as args to other fxns.
def say_hello():
    return "Hello Again!"

def greet_again(fxn):
    greeting = fxn() 
    print(greeting) 

greet_again(say_hello)

#3. Return functions as value from other fxns.

def parent():
    def child():
        return "Hello from Child!"
    return child 

my_fxn = parent() 
print( my_fxn() ) 
        

