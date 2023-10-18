

''' 
    List Comprehensions 
    Syntax: 
    identifier = [ expression for item in iterable if condition ]
'''


numbers = [ x for x in range(1, 11) if x % 2 == 0 ]

print(numbers) 


squares = [ x * x for x in range(1, 11)] 
print(squares) 


multiples = [ x * 5 for x in [1, 3, 8, 12] ] 
print(multiples) 

'''

    List Operations 

'''

marks = [12, 32, 21 ] 
replicated = marks * 4 
print(replicated) 


