# Change Calculator - Jackson Hauley

from essentials import *
from filehandling import *

def calculate_change(): 
    cs()
    currency = get_money()  # Gets the money dictionary
    while True:
        country_choice = int_input("Select Country\n\n1. United States\n2. Europe\n\nPick one (1-2): ")
        if country_choice == 1: 
            country = "us"
            break
        elif country_choice == 2: 
            country = "eu"
            break
        else: print("Invalid Input! Pick a number from 1 to 2!")
    cs()
    print(f"Country: {country}")
    while True:
        amount = input("\nEnter the amount of money you want change of: ")
        try:
            amount = float(f"{float(amount):.2f}")  # the input is a float
            formatted = f"{amount:.2f}"
            break  
        except ValueError:
            print("Invalid Input! Enter any amount of money (e.g. 19.20, 35000)")
    print(f"\nYou are converting {formatted} into {country} change")
    for x in currency:  # Getting the used currency dictionary
        if x[0] == country:
            used_currency = x[1]
    
    # This is where I made the actual currency calculation

    amount = int(amount*100)
    currency_list = []  # This is the starting list to calculate how many coins needed
    currency_list = [float('inf')] * (amount + 1)
    currency_list[0] = 0  # No coins are needed to make 0 amount
    coins_used = [None] * (amount + 1)
    for coin_name, coin_value in used_currency.items():  # This uses the value and the coin name and separates it from used_currency
        for i in range(coin_value, amount + 1):
            if currency_list[i - coin_value] + 1 < currency_list[i]:  # Replaces it from the list if it doesnt work correctly
                currency_list[i] = currency_list[i - coin_value] + 1
                coins_used[i] = coin_name  # Track the coin used
    if currency_list[amount] == float('inf'):
        return -1, []
    coins_used_list = []
    while amount > 0:  # This finds the name of the coins used
        coin_name = coins_used[amount]
        coins_used_list.append(coin_name)
        amount -= used_currency[coin_name]
    change_string = ", ".join([f"{get_name(coin)} x {count}" for coin, count in coins_used])
    print(f"Your change: {change_string}")
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