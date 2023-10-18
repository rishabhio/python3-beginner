
"""
    Function vs Method 

    Function: Reusable block of code 

    Method: Function that belongs to an object 

"""

my_list = [1, 2, 3, 4, 5 ]
print("####### Traversing the List ########")
for i in my_list:
    print(i, end=' ') 
print() 

# Method 2 to traverse 
N = len(my_list) 

print("####### Traversing the List 2 ########")
for i in range(0, N):
    print(my_list[i], end = ' ' ) # using indexing
print() 

print("List After Deletion")
del my_list[0] 
print(my_list) 
 
del my_list[-2]
print(my_list) 
