


'''

for <iterator> in <iterable>:
    <block_of_code>
    # without any break statements 
else:
    <block_of_code> 

'''


fruits = ['apple', 'banana', 'cherry'] 

# search for 'guava' in fruits 

for fruit in fruits:
    if fruit == 'guava':
        print("Found Guava!") 
        break 
else:
    print("Guava not found") 


