# Jackson Hauley - Coin Change Problem - File Handling

import pandas as pd # Needed for file reading

def get_money(): # Gets you a list of lists with the dictionary and the prefix
    result = []
    with open("CoinChange/money.csv", 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(',', 1)
            country = parts[0]
            currency_info = parts[1]
            currency_dict = {}
            for currency in currency_info.split(','):
                name, value = currency.split('-')
                currency_dict[name] = int(value)
            result.append([country, currency_dict])
    return result