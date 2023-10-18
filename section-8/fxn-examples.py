

'''
    Params: Define the values expected by fxn
    Args: Represent the actual values which are passed 
'''


def rect_area_perimeter(length, width):
    '''
        Calculate the area and parimeter of rectangle
    '''
    area = length * width
    perimeter = 2 * ( length + width )
    return area, perimeter


# Calling the fxn 
area, perimeter = rect_area_perimeter(10, 20) 
print(f"Area: {area} and Perimeter: {perimeter}")


def average(list_of_numbers):
    '''
        average all the elems of the list 
    '''
    return sum(list_of_numbers) // len(list_of_numbers) 

print(average([1, 2, 3] ))



