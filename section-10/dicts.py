

'''
Syntax for Dicts 

my_dict = {} # initializes an empty dict 

my_dict = {
    'key1': 'value1' 
}

keys: Immutable datatypes 
    int, string, float, tuple 

values: Any valid python object 

'''

# Method 1 
phonebook = {
    "Alice": "9000912121", 
    "Bob": "8888812123",
    "Charlie": "7878782332"
}

print(phonebook.get("Alice"))  

# Method 2
addressbook = dict() 
addressbook["Rishabh"] = '127.0.0.1' 
addressbook["Python"] = "10.1.1.23" 

print(addressbook) 

