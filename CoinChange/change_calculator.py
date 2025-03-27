# Change Calculator - Jackson Hauley

from essentials import *
from filehandling import *

def calculate_change(): 
    cs()
    currency = get_money()  # Gets the money dictionary
    while True:
        cs()
        country_choice = int_input("Select Country\n\n1. United States\n2. Europe\n3. United Kingdom\n4. Japan\n\nPick one (1-2): ")
        if country_choice == 1: 
            country = "usd"
            break
        elif country_choice == 2: 
            country = "eur"
            break
        elif country_choice == 3: 
            country = "uk"
            break
        elif country_choice == 4: 
            country = "jp"
            break
        else: 
            print("Invalid Input! Pick a number from 1 to 4!")
            input('Press enter to continue')
    cs()
    print(f"Country: {country}")
    while True:
        amount = input("\nEnter the amount of money you want change of: ")
        end = 0
        
        try:
            amount = float(f"{float(amount):.2f}")  # the input is a float
            formatted = f"{amount:.2f}"
            if amount < 0:
                print("What the heck are you trying to do here, bug test? Too bad I added this so there are no errors so take that.")
                input('Press enter to continue')
                end = 1
                break
            elif amount == 0:
                print("No change its 0 you dont need a calculator for that dummy")
                input('Press enter to continue')
                end = 1
                break
            else:
                break
        except ValueError:
            print("Invalid Input! Enter any amount of money (e.g. 19.20, 35000)")
    if end != 1:
        print(f"\nYou are converting {formatted} into {country} change\n")
        for x in currency:  # Getting the used currency dictionary
            if x[0] == country:
                used_currency = x[1]
        # This is where I made the actual currency calculation
        amount = int(amount*100) # Setting amount to cent base without the float
        currency_list = []  # This is the starting list to calculate how many coins needed
        currency_list = [float('inf')] * (amount + 1) # Setting everything to infinite and adding one, infinite being no solution
        currency_list[0] = 0  # No coins are needed to make 0 amount
        coins_used = [None] * (amount + 1) # Does the same thing but for coins used
        for coin_name, coin_value in used_currency.items():  # This uses the value and the coin name and separates it from used_currency
            for i in range(coin_value, amount + 1): # Iterates through the coin values
                if currency_list[i - coin_value] + 1 < currency_list[i]:  # Replaces it from the list if the coin doesnt fit
                    currency_list[i] = currency_list[i - coin_value] + 1 # Subtracs it if the coin value can fit in the list
                    coins_used[i] = coin_name  # Track the coin used
        coins_used_list = [] # This is the thing that gets the names of all the coins used
        while amount > 0:
            coin_name = coins_used[amount]
            coins_used_list.append(coin_name)
            amount -= used_currency[coin_name]  # Subtract the coin value from the remaining amount
        coin_count = {}
        for coin in coins_used_list:
            if coin in coin_count:
                coin_count[coin] += 1 # Adds it if you do want to use it
            else:
                coin_count[coin] = 1 # Removes if you dont want to tuse it
        formatted_coins = []
        for coin, count in coin_count.items(): # Counting how many coins in it
            coin_name = get_name(coin)
            formatted_string = f"{coin_name} x {count}"
            formatted_coins.append(formatted_string)
        change_string = "\n".join(formatted_coins) # This is just making it look nice when it prints
        print(f"Your change: \n\n{change_string}\n")
        input("Press enter to continue")



def get_name(name): # Gets a cleaned up name for each bill
    if name == "penny": return "Penny"
    elif name == "nickel": return "Nickel"
    elif name == "dime": return "Dime"
    elif name == "quarter": return "Quarter"
    elif name == "one": return "Dollar"
    elif name == "five": return "Five Dollar Bill"
    elif name == "ten": return "Ten Dollar Bill"
    elif name == "twenty": return "Twenty Dollar Bill"
    elif name == "fifty": return "Fifty Dollar Bill"
    elif name == "onehundred": return "One Hundred Dollar Bill"
    elif name == "onecent": return "One Cent Piece"
    elif name == "twocent": return "Two Cent Piece"
    elif name == "fivecent": return "Five Cent Piece"
    elif name == "tencent": return "Ten Cent Piece"
    elif name == "twentycent": return "Twenty Cent Piece"
    elif name == "fiftycent": return "Fifty Cent Piece"
    elif name == "euro": return "Euro"
    elif name == "twoeuro": return "Two Euro Bill"
    elif name == "fiveeuro": return "Five Euro Bill"
    elif name == "teneuro": return "Ten Euro Bill"
    elif name == "twentyeuro": return "Twenty Euro Bill"
    elif name == "fiftyeuro": return "Fifty Euro Bill"
    elif name == "onehundredeuro": return "One Hundred Euro Bill"
    elif name == "twopence": return "Two Pence"
    elif name == "fivepence": return "Five Pence"
    elif name == "tenpence": return "Ten Pence"
    elif name == "twentypence": return "Twenty Pence"
    elif name == "fiftypence": return "Fifty Pence"
    elif name == "onepound": return "One Pound"
    elif name == "twopound": return "Two Pound"
    elif name == "fivepound": return "Five Pound"
    elif name == "tenpound": return "Ten Pound"
    elif name == "oneyen": return "One Yen"
    elif name == "fiveyen": return "Five Yen"
    elif name == "tenyen": return "Ten Yen"
    elif name == "fiftyyen": return "Fifty Yen"
    elif name == "hundredyen": return "One Hundred Yen"
    elif name == "fivehundredyen": return "Five Hundred Yen"
    elif name == "thousandyen": return "One Thousand Yen"
    elif name == "fivethousandyen": return "Five Thousand Yen"
    else: return "NAME_ERROR [get_name()]"
