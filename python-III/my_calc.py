

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

def rectangle_area(l, w):
    l = float(input("Enter the length of the house: "))
    w = float(input("Enter the width of the house: " ))
    area = l * w
    print("The square footage of the house is", float(area))
    
rectangle_area(l=input, w=input)

# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

def find_circumference(r):
    from math import pi
    r = float(input("Enter the radius of a circle: "))
    c = 2 * pi * r
    # return 2 * pi * r
    print("The circumference of a circle is", float(c) ,"cm.")
    
find_circumference(r=input)