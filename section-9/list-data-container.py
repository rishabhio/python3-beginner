

'''

list_identifier = [] # empty list 
list_identifier = [1, 2, 3, 4, 5 ] 

# Square Brackets 

'''

student_grades = [ 95, 82, 78, 89, 98 ]

print(student_grades) 
 
shopping_list = ['apples', 'egges', 'milk', 'bread', 65, True] 

print(shopping_list) 


# list() Function 

empty_list = list() 
range_list = list( range(1, 11)) 
print( empty_list) 
print(range_list) 

string_list = list("Hello World") 
print(string_list )

# Accessing the list items  
# Indexing -> [ index ]  

print(shopping_list[0]) 


# Negative Indexing 
print(shopping_list[-1]) 


# Slicing -> [ start : end : step ] 

shopping_slice = shopping_list[0:4] 
print(shopping_slice) 

# Mutable Data Structure 

shopping_list[0] = 'oranges'
print(shopping_list) 



