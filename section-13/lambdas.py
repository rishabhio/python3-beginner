
# Lambda Functions 

'''
What are Lambda Functions ?? 
1. Small 
2. Anonymous 
3. N Arguments 
4. One Expression 
5. Result = Output of Expression 

lambda arg1, arg2 : expression 
'''


add = lambda x, y : x + y 
print(add(2, 3 ))


# Sort a list of tuples 
pairs = [ (7, 'seven'), (20, 'twenty'), (2, 'two'), (3, 'three'), (1, 'one')]

sorted_pairs = sorted(pairs, key = lambda pair : pair[0])
print(sorted_pairs) 


