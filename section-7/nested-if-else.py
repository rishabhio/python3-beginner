

## Domain: Ecomm. 

## Calculate discount 

## electronics / clothing / other 

## "INDIA", "USA" 


prompt_category = '''
Please choose the product: \n 
1. Electronics | Press-1 \n 
2. Clothing | Press-2 \n 
3. Other | Press-3 \n 
>>> 
'''
product = int(input(prompt_category)) 

prompt_location = '''
Please choose the location: \n   
1. India | Press-1 \n 
2. USA | Press-2 \n 
>>>    
'''

location = int(input(prompt_location)) 

if product == 1:
    if location == 1: 
        # India Location 
        discount = 20
    else: 
        # USA Location 
        discount = 5 

elif product == 2:
    if location == 1:
        discount = 10
    else:
        discount = 5 
else:
    discount = 2 


print("Applicable Discount is: ", discount) 

