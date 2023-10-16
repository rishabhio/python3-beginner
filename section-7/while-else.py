

'''

    while <condition>:
        <statements> 
    else:
        <statements> 

Else executes only: 
1. When the while condition becomes false 
2. and the loop didn't encounter any break 

'''

counter = 1 

while( counter < 5 ):
    print(counter) 
    counter += 1 
    if counter == 3:
        break 
else:
    print("All the items have been processed") 




