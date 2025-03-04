# Jackson Hauley Advanced Classes Notes

# 1. What is a helper function?
    # A function written to be called in another functional

def is_int(user_input):
    try:
        int(user_input)
    except:
        # 8. What is recursion?
            # When you call a function inside of itself, you
        # 9 How does recursion work?
            #
        print("Please give a number")
        user_input = is_int(input("How old are you?: "))
    else:
        return int(user_input)
    
def age():
    old = is_int(input("How old are you?: "))
    print(f"Cool. You are {old}")

# age()

# 2. What is the purpose of a helper functional function?
    # A function inside another function to help it like recursion
# 3. What is an inner function?
    # An inner function is a function that exists inside of another function

def add(a):
    b = int(input("Give me a number: "))

    def addition():
        print(a+b)

    addition()

#add(3)

import logging

logging.basicConfig(level=logging.INFO)

def logger(func):
    def wrapper(*args,**kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@logger
def add2(a,b):
    return a+b

# print(add2(3,4))

# 4. What is the scope of a variable in a function WITH an inner function?
    # The scope is limited to only the outer funtion so if you call it in a function than the function is only in the function
# 5. Why do we use inner functions?
    # So that we can use functions inside of other ones more efficiently
# 6. What is a closure function
    # it is a function inside an insane function and it saves information across multiple calls

def add(a):

    def addition(b):
        return(a+b)

    return addition

base = add(10)

# print(base(5))
# EXAMPLE
def math(income):

    def perc(amount,type):
        percent = amount/income
        print(f"Your {type} is ${amount}, and that is {percent} of your income")

def user_inputs(type):
    return int(input(f"What is your monthly {type}: "))

income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportation")

start = math()

# 7. Why do we write closure functions
    # it is a function inside an insane function and it saves information across multiple calls