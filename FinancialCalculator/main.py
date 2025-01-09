# Jackson Hauley - Financial Calculator

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError: 
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
    
def invalid(): 
    print("Invalid Input!")
    input("Press enter to continue")

def interest():
    cs()
    deposit = int_input("How much would you like to deposit?: ")
    original_deposit = deposit
    time = int_input("How many months are you planning on investing this money?: ")
    while True:
        try: percent = float(input("What percent increase do you get per month? (0.01 = 1%): "))
        except ValueError: 
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        break
    percent = percent+1
    for x in range(time):
        print(f"Month {x}: ${deposit:.2f}")
        deposit = deposit*percent
    print(f"Month 10: ${deposit:.2f}")
    print(f"You now have ${deposit:.2f} which is {deposit/original_deposit:.2f} times more than you originally invested!")
    input("Press enter to continue")

def goal():
    cs()
    goal = int_input("How much money do you want to save?: ")
    while True:
        choice2 = input("Do you want to deposit monthly or weekly?: ")
        if choice2 == "monthly": 
            deposit = int_input("How much would you like to deposit monthly?: ")
            print(f"It will take you about {round(round(goal/deposit)/12)} years and {round(goal/deposit)%12} months depositing ${deposit} per month to reach your goal!")
        elif choice2 == "weekly": 
            deposit = int_input("How much would you like to deposit weekly?: ")
            print(f"It will take you {round(goal/deposit)} weeks of depositing ${deposit} per week to reach your goal!")
        else:
            invalid()
        input("Press enter to continue")
        break

def budget():
    cs()
    income = int_input("What is your monthly income?: ")
    print(f"You can spend ${income*0.15:,.2f} this month on food")
    print(f"You can spend ${income*0.50:,.2f} this month on house/car/cell service")
    print(f"You can spend ${income*0.20:,.2f} this month on savings")
    print(f"You can spend ${income*0.05:,.2f} this month on entertainment")
    print(f"You can spend ${income*0.10:,.2f} this month on miscellaneous")
    input("Press enter to continue")

def sale():
    price = int_input("What is the items original price?")
    while True:
        try: percent = float(input("How much percent off? (0.01 = 1%): "))
        except ValueError: 
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        break
    print(f"The item cost ${price-price*percent} during the sale!")
    input("Press enter to continue")
    
def tip():
    spent = int_input("How much money did you spend? ")
    while True:
        try: tip = float(input("what percent do you want to tip the waiter?? (0.01 = 1%): "))
        except ValueError: 
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        break
    print(f"You tipped the waiter {spent*tip}! Generous!")
    input('Press enter to continue')

def cs(): # Clear Screen
    print("\033c",end="")

def main():
    while True:
        cs()
        choice = int_input("Jacksons Financial Calculator\n\n1. Goal Setting\n2. Interest Calculator\n3. Budget Calculator\n4. Sale Price Calculator\n5. Tip Calculator\n\nWhat would you like to do? (1-5): ")
        if choice == 1:
            goal()
        elif choice == 2:
            interest()
        elif choice == 3:
            budget()
        elif choice == 4:
            sale()
        elif choice == 5:
            tip()
        else:
            invalid()

main()