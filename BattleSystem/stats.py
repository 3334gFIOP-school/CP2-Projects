# Stats for battle system, Jackson Hauley

import random
import time
import os
import matplotlib.pyplot as plt 
import pandas as pd
from essentials import *

def stats(): # All the stats
    cs()
    choice = int_input("Stats Visualizer\n\n1. Character Stats\n2. Level Increase Stats\n3. Battle Stats\n4. Exit\n\nWhat do you want to do?: ")
    if choice == 1:
        data = pd.read_csv(FILE_PATH)
        data['age'] = pd.to_numeric(data['age'], errors='coerce')  # Coerce invalid entries to NaN
        data['health'] = pd.to_numeric(data['health'], errors='coerce')
        data['level'] = pd.to_numeric(data['level'], errors='coerce')
        data['xp'] = pd.to_numeric(data['xp'], errors='coerce')
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        axes[0, 0].scatter(data['age'], data['health'], color='blue')
        axes[0, 0].set_title('Age vs Health') # Age vs Health
        axes[0, 0].set_xlabel('Age')
        axes[0, 0].set_ylabel('Health')
        axes[0, 1].scatter(data['age'], data['level'], color='green')
        axes[0, 1].set_title('Age vs Level')
        axes[0, 1].set_xlabel('Age') # Age vs Level
        axes[0, 1].set_ylabel('Level')
        axes[1, 0].scatter(data['health'], data['xp'], color='red')
        axes[1, 0].set_title('Health vs XP')
        axes[1, 0].set_xlabel('Health') # Health vs XP
        axes[1, 0].set_ylabel('XP')
        axes[1, 1].scatter(data['level'], data['xp'], color='purple')
        axes[1, 1].set_title('Level vs XP')
        axes[1, 1].set_xlabel('Level') # Level vs XP
        axes[1, 1].set_ylabel('XP')
        plt.tight_layout()
        plt.show()
        input("Press enter to continue")
    elif choice == 2:
        print("Levels increase every round you win giving more XP, what stats do you even need with this haha")
        input("Press enter to continue")
    elif choice == 3:
        data = pd.read_csv(FILE_PATH)
        cs()
        print(data.describe())
        input("Press enter to continue")
    elif choice == 4:
        pass
