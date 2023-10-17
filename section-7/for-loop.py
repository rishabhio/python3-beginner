

'''

for <iterator> in <iterable>:
    <block_of_code> 

'''

# Example 1 

simple_iterable = [ 1, 2, 3, 4, 5, 6, 7, 8 ] 

for iter in range(1, 10, 2): 
    print(iter) 

# Example 2 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
]

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print() 


# Example 3 

for num in range(10):
    if num == 4:
        break 
    elif num == 2:
        continue 
    print(num) 


# Example 4 
nums_list = [1, 2, 3, 4, 5 ]
for i in range(len(nums_list) - 1 , -1, -1 ):
    print(nums_list[i]) 

