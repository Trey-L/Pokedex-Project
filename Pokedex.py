# Made by Trey Ignatius Leong, 24S54

import random
import pandas as pd

# Load Pokedex File
pokedex = pd.read_csv('/Users/treyleong/Downloads/Pokedex/Pokedex.csv ') # change filepath to where csv file is located if not working

print("1. Display selected number of Pokemons with their types and statistics.") # working [main] [invalidate]
print("2. Display the first Pokemon of a Type of the trainer's choice.") # working [main]
print("3. Display all Pokemons with Total Base stat of the trainer's choice.") # working [main]
print("4. Display all Pokemons with a minimum set of stats.") # working [main]
print("5. Display all legendary Pokemons of Types of the trainer's choice.") # [main not working: only showing either or; not both]
print("6. Display a random surprise pokemon. ") # working [main]
print("7. Quit") # working
option = int(input("Enter option number: "))

# need to add code to invalidate answers for each option
# can add option to filter by Generation

if option == 1:
# Function to display selected number of Pokemons
    def display_selected_pokemons(number):
        print(pokedex.head(number))
    num = int(input("Enter number of Pokemon to display: "))
    if num <= 800 and num > 0:
        display_selected_pokemons(num)
    else:
        print("Enter an integer between 1 and 800 inclusive.")
    
elif option == 2:
# Function to display the first Pokemon of a selected type
    def display_first_pokemon_of_type(pokemon_type):
    # Checks both Type 1 and Type 2 for the specified type
        filtered = pokedex[(pokedex['Type 1'] == pokemon_type) | (pokedex['Type 2'] == pokemon_type)]
        if not filtered.empty:
            print(filtered.iloc[0])
        else:
            print(f"No Pokemon found of type {pokemon_type}")
    tpe = input("Enter Pokemon Type: ")
    display_first_pokemon_of_type(tpe)

elif option == 3:
# Function to display all Pokemons with a specific Total Base Stat
    def display_pokemons_by_total_base_stat(total_base_stat):
        filtered = pokedex[pokedex['Total'] == total_base_stat]
        print(filtered)
    tstat = int(input("Enter Total Base Stat: "))
    display_pokemons_by_total_base_stat(tstat)

elif option == 4:
# Function to display all Pokemons with minimum set stats
    def display_pokemons_by_minimum_stats(min_stats):
        filtered = pokedex
        for stat, value in min_stats.items():
            filtered = filtered[filtered[stat] >= value]
        print(filtered)
    hth = int(input("Enter Min HP: "))
    att = int(input("Enter Min Attack: "))
    dee = int(input("Enter Min Defense: "))
    satk = int(input("Enter Min Sp. Atk: "))
    sdef = int(input("Enter Min Sp. Def: "))
    spd = int(input("Enter Min Speed: "))
    min_stats = {'HP': hth, 'Attack':att, 'Defense': dee, 'Sp. Atk': satk, 'Sp. Def': sdef, 'Speed': spd}
    display_pokemons_by_minimum_stats(min_stats)

elif option == 5:
# Function to display all legendary Pokemons of selected types
    def display_legendary_pokemons_of_types(types):
# Checks both Type 1 and Type 2 for specified types
        filtered = pokedex[((pokedex['Type 1'].isin(types)) | (pokedex['Type 2'].isin(types))) & (pokedex['Legendary'] == True)]
        print(filtered)
    typ1 = input("Enter Type 1: ").title()
    typ2 = input("Enter Type 2: ").title()
    display_legendary_pokemons_of_types([typ1, typ2])
    
elif option == 6:
    # Function to display a Pokemon by its No. column value
    def display_pokemon_by_number(rand_no):
    # Find the Pokemon with the corresponding No.
        filtered = pokedex[(pokedex['No.'] == rand_no)]
        if not filtered.empty:
            print(f"Randomly selected Pokémon with No. {rand_no}:")
            print(filtered.iloc[0])
        else:
            print(f"No Pokémon found with No. {rand_no}")
    rand_no = random.randint(1, 800)
    display_pokemon_by_number(rand_no)

elif option == 7:
    print()
else:
    print("Invalid Option.")
    
# python3 -u "/Users/treyleong/Downloads/newpoke.py"