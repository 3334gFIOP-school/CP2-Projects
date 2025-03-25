# Jackson Hauley - Coin Change Problem - File Handling

import pandas as pd # Needed for file reading

def get_money(): # Gets you a list of lists with the dictionary and the prefix
    money_file = pd.read_csv('CoinChange/money.csv', header=None) # Reads CSV File
    output = [] # Initializing the currency final output
    for _, row in money_file.iterrows():
        currency_data = row[0].split(',')
        country_type = currency_data[0]
        currency_dict = {} # Initializing the currency dictionary
        for coin in currency_data[1:]:
            name, value = coin.split('-')
            currency_dict[name] = int(value)
        output.append([country_type, currency_dict])
    return output