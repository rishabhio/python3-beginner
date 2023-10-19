
'''
    Operations on Dictionaries 
'''


# Check if a key exists 

my_dict = {"name": "Bob", "age": 25 } 

is_name_present = "name" in my_dict 
is_qualification_present = "qualification" in my_dict 
print(is_name_present) 
print(is_qualification_present)


# Delete an element from the dict 

del my_dict["age"] 
print(my_dict) 