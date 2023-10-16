
## Calculating grades of a student 
## Based on the marks obtained in a subject 


marks = int(input("Enter the marks obtained: ")) 


if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C' 
elif marks >= 50:
    grade = 'D' 
else:
    grade = 'E'

print('The grade obtained is: ', grade) 

