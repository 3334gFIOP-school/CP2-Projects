# Jackson Hauley, Multiple Page Python Notes

from calc import addition as add,subtraction as sub,multiply as mul, divide as div, exponent as exp,num # Star lets you import everything

"""
> How do you make multiple files in python?
Make a new file and end it in .py
Snake case file names with descriptive names

> How do you get a function from another file
from file import * or function, * does everything

> How do you get variables from another file?
from file import * or variable name, * does everything
It is better to return from a function that using a variable so you can change it

> How do you have a function with multiple returns?
"""
def get_user_info():
    name = input("Name: ")
    age = input("Age: ")
    color = input("Color: ")
    return name,age,color

name2,age2,color2 = get_user_info()
print(name2,age2,color2)

"""
> Why would you use multiple pages for a python project? 
You can have each page its own functions so that you can manage different sections of the project in different sections of the code so you can manage and organize
Easier to merge branches
Modularity - Breaking program up
Functionality

"""

print(add())
print(sub(num,10))


