
'''
Dictionary Comprehensions

identifier = {key: value for key, value in iterable if condition }

'''


# Example 


squares = {
    num: num ** 2 for num in range(1, 5) 
}

print(squares) 


even_squares = {
    num: num ** 2 for num in range(1, 10) if num % 2 == 0
}

print(even_squares) 