

manifest = 'Flight: BA283 | Destination: Singapore | Passengers: 215' 

# Strings are immutable, following will raise an error 
# manifest[0] = 'D' 

# Indexing 
print(manifest[8]) 

# Slicing 
print(manifest[8:14]) 

# Concatenation 
gate = '| Gate: 12' 
manifest += gate 
print(manifest) 

# length function 
total_chars = len(manifest) 
print(f'Total characters in manifest: {total_chars} ') 

# Membership 
print('BA283' in manifest) 

# Replication 

print(manifest * 3) 

