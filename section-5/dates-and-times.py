# Python Datetime 

from datetime import datetime 
from datetime import timedelta 
from datetime import date 

# Current date and time 
now = datetime.now() 
print(f'Current date and time: {now}') 

# Display date and time in different formats 

print(f'Current date: {now.date()}') 

# Current time 
print(f'Current Time: {now.time()}') 

# Format the date and time 
print(f'Formatted Datetime: {now.strftime("%Y-%m-%d %H:%M:%S")}') 

# Get the day of the Week 
weekday = now.strftime('%A')
print(f'Weekday: {weekday}') 

# Adding and Subtracting Time durations 
delta = timedelta(days=1) 
one_day_in_future = now + delta 
print(f'One day in future: {one_day_in_future}') 

# One day in Past 
one_day_in_past = now - delta  
print(f'One day in past: {one_day_in_past}') 


# Create a specific date 
specific_date = date(2023, 11, 12) 
print(f'Specific date: {specific_date}') 


