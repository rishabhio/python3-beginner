

# Calculate the volume and surface of a sphere 


PI = 3.14 

# input radius is going to be a string 
input_radius = input("Enter the radius of the Sphere:\n ~$ ") 

# perform the type cast  
radius = float(input_radius) 

# calculate the surface area 

surface_area = 4 * PI * radius ** 2 

# calculate the volume 

volume = (4/3) * PI * radius ** 3 

# print the results 
print(f'The surface area of sphere is: {surface_area}')

# print the volume 
print(f'Volume of the sphere is: {volume} ')
 
 