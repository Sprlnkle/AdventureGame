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
'''

import random



def purchase_item(itemPrice, startingMoney, item_name, quantityToPurchase = 1):

    """
    This functions allows the player to buy items, If the player buys the item(s) and can afford them
    it just gives them the items. If the player cannot afford the items it gives them the max ammount
    they could afford.
    """

    if itemPrice * quantityToPurchase < startingMoney: 
        pass
    elif itemPrice * quantityToPurchase > startingMoney:
        while itemPrice * quantityToPurchase > startingMoney and quantityToPurchase > 0:
            quantityToPurchase -= 1
        pass


#Transaction logic

    quantityPurchased = quantityToPurchase
    remainingMoney = startingMoney - itemPrice * quantityToPurchase 
    print(f'Purchased {quantityToPurchase} {item_name}')
    print(f'${remainingMoney} Money remaining')
    return remainingMoney

# --TO DO-- code for giving player purchased items and updating global money goes here

    # I didn't know how to set up a function for returning without knowing what the 
    # rest of the code would look like so I just printed for now     

def new_random_monster():
    
    """This is the list of monsters and their traits. A monster is selected with random and then given random traits and returned"""
    
    monster_dict = [
        {
        'name': 'Slime',
        'desc': 'A small clump of rotting biomatter clung together by the collective, dying will of its parts',
        'health': (1, 3),
        'power': (0, 2),
        'money': (5, 10)
    },
    {
        'name': 'Zombie',
        'desc': 'Any dead creature with enough soul left to continue to move',
        'health': (20, 50),
        'power': (10, 20),
        'money': (20, 60)
    },
    {
        'name': 'Greg',
        'desc': 'Greg is a wealthy passerby. Will you sacrifice your morality for wealth?',
        'health': (8, 12),
        'power': (1, 3),
        'money': (2000, 5000)
    }
    ]

    #This is the logic for creating a new monster using random

    monster = random.choice(monster_dict)
    return {
        'name': monster['name'],
        'desc': monster['desc'],
        'health': random.randint(*monster["health"]),
        'power': random.randint(*monster['power']),
        'money': random.randint(*monster['money'])
    }


#--------------------------------------------------------------------------------------------------------------------------------
# New functions for assignment 6 below line

def print_welcome(name, width=20):
    

    '''pretty straight forward, just prints the welcome message'''

    print(f'{"Hello, " + name + "!":^{width}}')


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
    for item, price in SHOP_ITEMS.items():
        print(f'| {item} ${price} |')
    print("\\---------------------/")


'Manages fights between the player and monster returning the gold amount the monster dropped.'

def fight_manager(playerhealth = 50, playerdmg = 5):
    monster = new_random_monster()
    monstername = monster['name']
    monsterhealth = monster['health']
    monsterdmg = monster['power']
    monstergold = monster['money']
    desc = monster['desc']
    choice = int(input(f'A wild {monstername} appeared! {desc}. Monster Health:{monsterhealth}, Monster Damage:{monsterdmg}, Gold Reward:{monstergold} Fight(1), Run(2)'))
  

    while playerhealth > 0 and monsterhealth > 0 and choice == 1:
        monsterhealth -= playerdmg
        print(f'You dealt {playerdmg} damage. Monster health:{monsterhealth}')
        if monsterhealth > 0:
            playerhealth -= monsterdmg
            print(f'{monstername} attacks, dealing {monsterdmg} damage. Player health: {playerhealth}')          
        if monsterhealth > 0 and playerhealth > 0:
            choice = int(input('Continue to fight (1) or run away (2): '))
            if choice != 1:
                print('You ran away!')
        else:
            break

      
    if monsterhealth < 0 and playerhealth > 0:
        print(f'You won the fight! You got {monstergold} gold!')
        return monstergold
    elif playerhealth < 0:
        print('You died')
        return(0)
    elif choice != 1:
        print('You ran away!')
        return(0)


    



def function_test_if_main():


    """This tests the functions if they are running in main"""
    print('This test shows what happens when the player does not have enough money to purchase an item\n')
    purchase_item(100, 50, 1)
    print('\n\n')
    print('This is what happens when a player requests more items than they can afford but can still afford some\n')
    purchase_item(10, 30, 5)
    print('\n\n')
    print('This is what happens when a player purchases items correctly\n')
    purchase_item(10, 100, 4)
    print('\n\n')

    print('This is just showcasing the new_random_monster function\n')
    monster = new_random_monster()
    print(monster, '\n\n')
    monster = new_random_monster()
    print(monster, '\n\n')
    monster = new_random_monster()
    print(monster, '\n\n')

    # Functions for assignment 6 to showcase functionality

    print('\n\nWelcome message tests\n\n')
    print_welcome('Jeff')
    print_welcome('Tom')
    print_welcome('NoobSlayer3000')

    print('\n\nShop menu tests\n\n')
    print_shop_menu("Bow", 125.75, "Arrow", 2.50)
    print_shop_menu("Potion", 10.50, "Wand", 299.99)
    print_shop_menu("Sword", 135.80, "Shield", 99.99)

    if __name__ == '__main__':
        function_test_if_main()
