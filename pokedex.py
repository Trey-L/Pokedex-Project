import csv
import random

def welcome():
    print("\nWelcome to the Pokedex!\n")

def menu():
    print("\n1. Display a selected number of Pokemons with their types and statistics.") # working
    print("2. Display the first Pokemon of a Type of the Trainer's choice.") # working
    print("3. Display all Pokemons of a Type of the Trainer's choice.") # working
    print("4. Display all Pokemons with a Total Base Stat of the Trainer's choice.") # working
    print("5. Display all Pokemons with a minimum set of stats.") # working
    print("6. Display all legendary Pokemons of Types of the trainer's choice.") # working
    print("7. Display all Pokemons of a Generation of the Trainer's Choice.") # working
    print("8. Display a random surprise pokemon. ") # working
    print("9. Quit\n")

def print_headers(): # print headers for pokedex
    print()
    print("No.".ljust(5), "Name".ljust(30), "Type 1".ljust(8), "Type 2".ljust(8), 
          "Total".ljust(8), "HP".ljust(5), "Attack".ljust(8), "Defense".ljust(8), 
          "Sp. Atk".ljust(8), "Sp. Def".ljust(10), "Speed".ljust(8), "Generation".ljust(11), 
          "Legendary".ljust(11))

def read_pokedex(): # read pokedex file
    with open('pokemon.csv', 'r') as file:
        reader = csv.reader(file)
        global pokedex
        pokedex = list(reader)
    return pokedex

def display_selected_pokemons(number): 
    '''display x number of pokemon'''
    subopt = input("Do you want to display the top or bottom " + str(number) + " Pokemons? (top/bottom): ").lower()
    print_headers()
    if subopt == "top":
        for i in range(1, number+1): # iterates through pokedex for selected number of pokemon from top
            pokemon = pokedex[i]
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                pokemon[12].ljust(11))
    elif subopt == "bottom":
        for i in range(800-number, 801): # iterates through pokedex for selected number of pokemon from bottom
            pokemon = pokedex[i]
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                pokemon[12].ljust(11))
    else:
        print("Invalid Option Entered.")
        
def display_first_pokemon_of_type(pokemon_type): 
    '''display first pokemon of selected type'''
    print_headers()
    for i in range(1, len(pokedex)): # iterates through whole pokedex for first occurence of selected type
        pokemon = pokedex[i]
        if pokemon[2] == pokemon_type or pokemon[3] == pokemon_type:
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            break

def display_all_pokemon_of_type(allptype): 
    '''display all pokemon of selected type'''
    print_headers()
    count = 0
    for i in range(1, len(pokedex)): # iterates through whole pokedex for all occurences of selected type
        pokemon = pokedex[i]
        if pokemon[2] == allptype or pokemon[3] == allptype:
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            count += 1
    print("\nTotal Number of Pokemon Found: " + str(count)) # print total number of pokemon found

def display_all_pokemon_with_total_base_stat(stat):
    '''display all pokemon with total base stat'''
    print_headers()
    count = 0
    for i in range(1, len(pokedex)): # iterates through whole pokedex for total base stat entered
        pokemon = pokedex[i]
        if int(pokemon[4]) == stat:
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            count += 1
    print("\nTotal Number of Pokemon Found: " + str(count)) # print total number of pokemon found

def display_all_pokemon_with_min_stats(hp, attack, defense, spatk, spdef, speed):
    '''display all pokemon with minimum set of stats'''
    print_headers()
    count = 0
    for i in range(1, len(pokedex)): # iterates through whole pokedex for selected stats
        pokemon = pokedex[i]
        if int(pokemon[5]) >= hp and int(pokemon[6]) >= attack and int(pokemon[7]) >= defense and int(pokemon[8]) >= spatk and int(pokemon[9]) >= spdef and int(pokemon[10]) >= speed:
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            count += 1
    print("\nTotal Number of Pokemon Found: " + str(count)) # print total number of pokemon found
    
def display_legendary_pokemons_of_types(types1, types2):
    '''display all legendary pokemon of selected types'''
    print_headers()
    count = 0
    for i in range(1, len(pokedex)): # iterates through whole pokedex for selected types and legendary status
        pokemon = pokedex[i]
        if ((pokemon[2] in types1 and pokemon[3] in types2) or (pokemon[2] in types2 and pokemon[3] in types1)) and pokemon[12] == "TRUE":
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            count += 1
    print("\nTotal Number of Pokemon Found: " + str(count)) # print total number of pokemon found
            
def display_all_pokemon_of_generation(gen): 
    '''display all pokemon of selected generation'''
    print_headers()
    count = 0
    for i in range(1, len(pokedex)): # iterates through whole pokedex for selected generation
        pokemon = pokedex[i]
        if pokemon[11] == gen:
            print(str(i).ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8), 
                  pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8), 
                  pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11), 
                  pokemon[12].ljust(11))
            count += 1
    print("\nTotal Number of Pokemon Found: " + str(count)) # print total number of pokemon found

def display_random_pokemon(): 
    '''display random pokemon'''
    print_headers()
    pokemon = pokedex[random.randint(1, len(pokedex))] # generate random number between 1 and 800 inclusive, and display pokemon
    print(pokemon[0].ljust(5), pokemon[1].ljust(30), pokemon[2].ljust(8), pokemon[3].ljust(8),
            pokemon[4].ljust(8), pokemon[5].ljust(5), pokemon[6].ljust(8), pokemon[7].ljust(8),
            pokemon[8].ljust(8), pokemon[9].ljust(10), pokemon[10].ljust(8), pokemon[11].ljust(11),
            pokemon[12].ljust(11))



read_pokedex() # read pokedex file
welcome() # welcome message
while True:
    menu()
    try:
        option = int(input("Enter option number: "))
    except ValueError: # if non integer is entered, return error message
        print("\nInvalid Option Entered.")
        
    if option == 1:
        try:
            number = int(input("Enter number of Pokemon to display: "))
            if number <= 800 and number > 0: # only accepts numbers between 1 and 800 inclusive
                display_selected_pokemons(number)
            else:
                print("Enter an integer between 1 and 800 inclusive.")
        except ValueError: # if non integer is entered, return error message
            print("Invalid Option Entered.")
            
    elif option == 2:
            tpe = input("Enter Pokemon Type: ").title()
            display_first_pokemon_of_type(tpe)
            
    elif option == 3:
        ptype = input("Enter Pokemon Type: ").title()
        display_all_pokemon_of_type(ptype)

    elif option == 4:
        try:
            tstat = int(input("Enter Total Base Stat: "))
            display_all_pokemon_with_total_base_stat(tstat)
        except ValueError: # if non integer is entered, return error message
            print("Invalid Option Entered.")
            
    elif option == 5:
        try:
            hp = int(input("Enter minimum HP: "))
            attack = int(input("Enter minimum Attack: "))
            defense = int(input("Enter minimum Defense: "))
            spatk = int(input("Enter minimum Special Attack: "))
            spdef = int(input("Enter minimum Special Defense: "))
            speed = int(input("Enter minimum Speed: "))
            display_all_pokemon_with_min_stats(hp, attack, defense, spatk, spdef, speed)
        except ValueError: # if non integer is entered, return error message
            print("Invalid Option Entered.")
            
    elif option == 6:
        typ1 = input("Enter Type 1: ").title()
        typ2 = input("Enter Type 2: ").title()
        display_legendary_pokemons_of_types(typ1, typ2)
        
    elif option == 7:
        try:
            gen = input("Enter Generation: ")
            display_all_pokemon_of_generation(gen)
        except ValueError: # if non integer is entered, return error message
            print("Invalid Option Entered.")

    elif option == 8:
        display_random_pokemon()

    elif option == 9:
        print("\nGoodbye!\n")
        exit() # exit program
        
    else:
        print("Invalid Option Entered.")