# Timothy Fox
# 2/24/2025

# This is the Adventure Functions project. It lays out a 
# few basic functions (purchase_item and new_random_monster)
# to be used in an adventure game
#----------------------------------------------------------------------------

# Timothy Fox
# 3/1/2025
# Assignment 6
# Added welcome function
# Added shop menu function 

#-------------------------------------------------------------------------------
# Timothy Fox
#3/7/2025
# assignment 8
# Changed this file from the main file to gamefunctions 

'''
These are the game functions. This module contains the funcitons necessary for the adventure game such as:
print_welcome
print_shop_menu
purchase_item
new_random_monster
Load
Save
Start
pygame screen initialization 
'''
import json
import random
import pygame
import wanderingMonster














# Greg Trading
def Greg_Trading(inventory, Gold):
    Greg_items = {
        "Magic Sword": {"price": 500, "durability": 200, "multiplier": 7, "description": "A sword with magical properties."},
        "Elven Bow": {"price": 300, "durability": 150, "multiplier": 5, "description": "A bow crafted by the elves."},
        "Devastating Potion": {"price": 150, "durability": 1, "multiplier": 1000, "description": "Essentially hydrochloric acid."},
    }

    random_item_name = random.choice(list(Greg_items.keys()))
    random_item = Greg_items[random_item_name]

    print(f"Hey pal, I've got this {random_item_name} for ya!")
    print(f"It'll only set ya back {random_item['price']} Gold!")
    print(f"It does {random_item['multiplier']} damage!")
    print(f"Description: {random_item['description']}")

    choice = int(input(f'\n Would you like to buy?\n (1:Yes  2:No)\n'))
    if choice == 1:
        if Gold >= random_item['price']:
            Gold -= random_item['price']
            if random_item_name in inventory:
                inventory[random_item_name]['quantity'] += 1
            else:
                # Add all item stats to the inventory
                inventory[random_item_name] = {
                    **random_item,  # Copy all stats from Greg_items
                    'quantity': 1   # Add quantity
                }
            print(f"You bought {random_item_name}!")
        else:
            print("Not enough gold.")
    else:
        print("WHAT!!, WHADYA MEAN BAD DEAL? I sold my right foot to get my hands on that!")
    return Gold








def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((320, 320))  # 10x10 grid, each square is 32x32 I think
    pygame.display.set_caption('Outside Town')
    return screen

def draw_grid(screen, player_pos, monster_pos=None, monster_color=(255, 0, 0)):
    """
    Draws the game grid, player, monster, and town.
    """
    screen.fill((50, 150, 50))  # Green background
    grid_color = (200, 200, 200)  # Grid color

    # Draw the grid
    for x in range(0, 320, 32):
        for y in range(0, 320, 32):
            pygame.draw.rect(screen, grid_color, pygame.Rect(x, y, 32, 32), 1)

# monster is no longer a can of monster, I realized I can use the monster color var to determin the monster type and pick a different picture for each.
    if monster_color == (0, 200, 0):
        monster_image = pygame.image.load('images/zombie.png') 
    elif monster_color == (0, 200, 200):
        monster_image = pygame.image.load('images/slime.png')
    elif monster_color == (255, 255, 0):
        monster_image = pygame.image.load('images/greg.png')
    else:
        monster_image = pygame.image.load('images/monster.png')
    player_image = pygame.image.load('images/knight.png')
    player_color = (0, 0, 255)  # Blue

    # Draw the player
    try:
        player_rect = pygame.Rect(player_pos[0] * 32, player_pos[1] * 32, 32, 32)
        screen.blit(player_image, player_rect)

    except Exception as e:
        print(e)
        player_rect = pygame.Rect(player_pos[0] * 32, player_pos[1] * 32, 32, 32)
        pygame.draw.rect(screen, player_color, player_rect)

    # Draw the monster

    try:
        monster_rect = pygame.Rect(monster_pos[0] * 32, monster_pos[1] * 32, 32, 32)
        screen.blit(monster_image, monster_rect)

    except Exception as e:
        print(e)
        player_rect = pygame.Rect(player_pos[0] * 32, player_pos[1] * 32, 32, 32)
        pygame.draw.rect(screen, monster_color, monster_rect)

    # Draw the town
    town_color = (0, 255, 0)  # Green
    pygame.draw.circle(screen, town_color, (9 * 32 + 16, 9 * 32 + 16), 16)  

    return monster_pos

def player_move(player_pos, key):
    keys = pygame.key.get_pressed()

#gets the arrow key pressed

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 1
    elif keys[pygame.K_RIGHT] and player_pos[0] < 9:
        player_pos[0] += 1
    elif keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 1
    elif keys[pygame.K_DOWN] and player_pos[1] < 9:
        player_pos[1] += 1


    return player_pos



def save(inventory, HP, Gold, Name):
#saves the game
    data = {
        'inventory': inventory,
        'hp': HP,
        'gold': Gold,
        'Name': Name
    }
    with open(f"{Name}.json", 'w') as file:
        json.dump(data, file)


def start_game():
#Starts the game
    NewOrSave = input('New game or load save? ("new" or "load")')
    if NewOrSave == 'new':
        inventory = {}
        HP = 100
        Gold = 300
        Name = print_welcome()
    elif NewOrSave == 'load':
        Name = input('What is the name of the save?')
        Name, inventory, HP, Gold = load_game(Name)
    return Name, inventory, HP, Gold


def load_game(Name):
    # Loads a game if start game calls for load game, If loading fails it just starts a new cause it kept crashing without the "try"
    file_name = f"{Name}.json"
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if not content:  # Check if file is empty
                raise ValueError("Save file is empty.")
            data = json.loads(content)
            inventory = data.get('inventory', [])
            hp = data.get('hp', 100)
            gold = data.get('gold', 300)
            return Name, inventory, hp, gold
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"Error loading save file: {e}")
        print("Starting a new game...")
        Name = print_welcome()
        return Name, [], 100, 300


def purchase_item(item_stats, Gold, item_choice, inventory, quantity=1):
    if item_choice not in item_stats:
        print("Item not found.")
        return Gold

    item_price = item_stats[item_choice]['price']
    total_cost = item_price * quantity

    if Gold >= total_cost:
        Gold -= total_cost
        if item_choice in inventory:
            inventory[item_choice]['quantity'] += quantity
        else:
            # Add all item stats to the inventory
            inventory[item_choice] = {
                **item_stats[item_choice],  # Copy all stats from item_stats
                'quantity': quantity       # Add quantity
            }
        print(f"You bought {quantity} {item_choice}(s).")
    else:
        print("Not enough gold.")
    return Gold



def new_random_monster():
    
    """This is the list of monsters and their traits. A monster is selected with random and then given random traits and returned"""
    
    monster_dict = [
        {
        'name': 'Slime',
        'desc': 'A small clump of rotting biomatter clung together by the collective, dying will of its parts',
        'health': (1, 3),
        'power': (0, 2),
        'Gold': (5, 50),
        'color': (0, 200, 200)
    },
    {
        'name': 'Zombie',
        'desc': 'Any dead creature with enough soul left to continue to move',
        'health': (20, 150), #buffed to have higher potential health and power while also giving more gold.
        'power': (10, 35),
        'Gold': (20, 230),
        'color': (0, 200, 0)
    },
    {
        'name': 'Greg',
        'desc': 'Greg is a wealthy passerby. Will you sacrifice your morality for wealth?',
        'health': (8, 12),
        'power': (1, 3),
        'Gold': (500, 1000),
        'color': (255, 255, 0)
    }
    ]

    #This is the logic for creating a new monster using random

    monster = random.choice(monster_dict)
    return {
        'name': monster['name'],
        'desc': monster['desc'],
        'health': random.randint(*monster["health"]),
        'power': random.randint(*monster['power']),
        'Gold': random.randint(*monster['Gold']),
        'color' : monster['color']
    }



def print_welcome():
    Name = input('What is your name?\n')

    print(f'Hello {Name}!')
    return(Name)

#This is outdated but I'm keeping it for now just in case I need it
SHOP_ITEMS = {
    'Bow': 125.75,
    'Arrow': 2.50,
    'Potion': 10.50,
    'Wand': 299.99,
    'Sword': 135.80,
    'Shield': 99.99
}


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):

    """Prints the formatted shop
    
    
        item1Name: name of item 1
        item1Price: price of item 1
        item2Name: name of item2
        item2Price: price of item 2
    
       --To Do-- Add returns instead of just printing when the game has more structure and the values can be returned somewhere.
     """

def print_shop_menu():
    print("/---------------------\\")
    for item, stats in item_stats.items():
        print(f"| {item} ${stats['price']} |")
    print("\\---------------------/")

'''
Used to store the items the player buys
'''


inventory = {
    'Bow': 0,
    'Arrow': 0,
    'Potion': 0,
    'Wand': 0,
    'Sword': 0,
    'Shield': 0
}


item_stats = {
    "Sword": {"price": 100, "durability": 50, "multiplier": 3},
    "Bow": {"price": 100, "durability": 50, "multiplier": 4},
#    "Arrow": {"price": 2.5, "durability": 1, "multiplier": 0.5},  unused for now cause idk how to impliment 
    "Potion": {"price": 50, "durability": 1, "multiplier": 500},  
    "Wand": {"price": 200, "durability": 100, "multiplier": 3},
    "Shield": {"price": 99.99, "durability": 15, "multiplier": 0}, 

}

'''
Used to add items to the player inventory after they have been purchased
'''

def add_to_inventory(inventory, item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        print(f"Item {item} not recognized.")

'''
Used to remove items from the players inventory after they have been used.
'''


def remove_from_inventory(inventory, item, quantity=1):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
    else:
        print(f"Not enough {item} in inventory to remove.")



'''
Used when the players inventory needs to be displayed
'''

def display_inventory(inventory):
    print("\nInventory:")
    for item, data in inventory.items():
        quantity = data['quantity']
        durability = data['durability']
        print(f"- {item} (x{quantity}, Durability: {durability})")




'Manages fights between the player and monster returning the gold amount the monster dropped.'

def fight_manager(playerhealth=50, playerdmg=5, inventory={}, monster=None, Gold=0):
    monster = monster.get_info()
    monstername = monster['name']
    monsterhealth = monster['health']
    monsterdmg = monster['power']
    monstergold = monster['Gold']
    desc = monster['desc']
    
    if monstername == 'Greg':
        choice = int(input(f'You ran into Greg! {desc}. Monster Health: {monsterhealth}, Monster Damage: {monsterdmg}, Gold Reward: {monstergold}. Fight(1), Run(2), Trade(3): \n'))
        if choice == 3:
            Gold = Greg_Trading(inventory, Gold)
            return Gold  
    
    choice = int(input(f'A wild {monstername} appeared! {desc}. Monster Health: {monsterhealth}, Monster Damage: {monsterdmg}, Gold Reward: {monstergold}. Fight(1), Run(2): '))
    
    # Weapon selection
    if inventory:
        print("\nChoose your weapon from the inventory:")
        for idx, item in enumerate(inventory):
            stats = inventory[item]
            print(f"{idx + 1}. {item} (Durability: {stats['durability']}, Quantity: {stats['quantity']})")
        
        weapon_choice = int(input("Select your weapon: ")) - 1
        weapon = list(inventory.keys())[weapon_choice]
        
        # Get weapon stats from inventory
        weapon_info = inventory.get(weapon, None)
        if weapon_info is None:
            print(f"Error: {weapon} does not have valid stats in inventory.")
            return 0
        
        weapon_dmg = weapon_info['multiplier']
        weapon_durability = weapon_info['durability']
        print(f'You equipped {weapon} with damage multiplier of {weapon_dmg} and durability of {weapon_durability}.\n')
    else:
        print("You have no weapons! Fighting with your fists.")
        weapon_dmg = 1  # Default damage multiplier for fists
        weapon_durability = 0

    # Combat loop
    while playerhealth > 0 and monsterhealth > 0 and choice == 1:
        # Calculate damage using weapon multiplier
        total_player_dmg = playerdmg * weapon_dmg
        monsterhealth -= total_player_dmg
        print(f'You dealt {total_player_dmg} damage. Monster health: {monsterhealth}')
        
        # Is the monster still alive?
        if monsterhealth > 0:
            playerhealth -= monsterdmg
            print(f'{monstername} attacks, dealing {monsterdmg} damage. Player health: {playerhealth}')
        
        # Reduce weapon durability
        if weapon_durability > 0:
            weapon_durability -= 1
            inventory[weapon]['durability'] -= 1
            print(f'{weapon} durability: {weapon_durability}')
            if weapon_durability <= 0:
                print(f'{weapon} broke!')
                if inventory[weapon]['quantity'] > 1:
                    inventory[weapon]['quantity'] -= 1
                else:
                    del inventory[weapon]
                break

        # Continue or run away
        if monsterhealth > 0 and playerhealth > 0:
            choice = int(input('Fight (1) or Run Away (2): '))
            if choice != 1:
                break
        else:
            break

    # End of fight conditions
    if monsterhealth <= 0 and playerhealth > 0:
        print(f'You won the fight! You got {monstergold} gold!')
        return monstergold
    elif playerhealth <= 0:
        print('You died.')
        return 0
    elif choice != 1:
        print('You ran away!')
        return 0






