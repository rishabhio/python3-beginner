

'''
    list, dict 

    tuple: Immutable list 

    [ ] -> list 
    { } -> dict 
    ( ) -> tuple 

    tuple_identifer = (1, 2, 3, ) 

'''


tuple_example = (1, 2, 3, 'a') 
print(tuple_example)
print(type(tuple_example)) 


########################################### 

# Parenthesis overloading problem 

a = (1, 2) 
print(type(a)) 

b = (True, False) 
print(type(b)) 

c = ('one', 'two') 
print(type(c)) 

d = (1, ) 
print(type(d)) 