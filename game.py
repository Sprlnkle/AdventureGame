'''
This is the main game file that the game will actually run within. The functions will be imported from gamefunctions.py
and used here
'''
import pygame
import sys
import gamefunctions








#had to move item stats to game.py for simplicity may not be used but leaving here for now

item_stats = {
    "Sword": {"price": 100, "durability": 50, "multiplier": 3},
    "Bow": {"price": 100, "durability": 50, "multiplier": 4},
 #   "Arrow": {"price": 2.5, "durability": 1, "multiplier": 0.5},
    "Potion": {"price": 50, "durability": 1, "multiplier": 500},  
    "Wand": {"price": 200, "durability": 100, "multiplier": 3},
    "Shield": {"price": 99.99, "durability": 15, "multiplier": 0}, 
}
    


def main():
    '''This is the main game function, everything should run within this'''
    Name, inventory, HP, Gold = gamefunctions.start_game() 


    while True:
        print("\nWhat would you like to do?\n")
        print("1. Shop")
        print("2. Fight (leave town)") # still needs work and I want to add more functionality but I need to get the base requirements for the assignment in on time this time.
        print('3. Save')
        print("4. Quit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':  # Shop
            gamefunctions.print_shop_menu()  # Print the shop menu with items and prices
            item_choice = input("What would you like to buy?\n")

            if item_choice in gamefunctions.SHOP_ITEMS:  # Check if the item is real
                price = gamefunctions.SHOP_ITEMS[item_choice]
                quantity = int(input(f"How many {item_choice}s would you like to buy? "))
                Gold = gamefunctions.purchase_item(item_stats, Gold, item_choice, inventory, quantity)
                gamefunctions.display_inventory(inventory)  # Display updated inventory after purchase
            else:
                print("That item is not available in the shop.")

        elif choice == '2':  # loads pygame and lets player move around. Also sees if player touches monster or town
            player_pos = [0, 0]

            screen = gamefunctions.init_pygame()
            monster_pos = None  # Let draw_grid handle monster position cause its easier 
            monster_pos = gamefunctions.draw_grid(screen, player_pos, monster_pos)
            pygame.display.flip()

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:  # moves player on keypress
                        player_pos = gamefunctions.player_move(player_pos, event.key)
                        monster_pos = gamefunctions.draw_grid(screen, player_pos, monster_pos)
                        pygame.display.flip()

                        # Check for touching monster
                        if player_pos == monster_pos:
                            print("You ran into a monster.")
                            pygame.quit()  # close the PyGame window cause leaving it open freezes computer
                            gold_reward = gamefunctions.fight_manager(playerhealth=50, playerdmg=5, inventory=inventory)
                            Gold += gold_reward
                            running = False
                            break

                        # Check for touching town
                        if player_pos == [9, 9]:  # bottom right corner
                            print("You returned to the town.")
                            pygame.quit()  # close the pygame window
                            running = False
                            break


     

        elif choice == '3':
            gamefunctions.save(inventory, HP, Gold, Name)
            print("Game saved!")

        elif choice == '4':
            print(f'Goodbye')
            break

        else:
            print("That is not a valid number, please pick a listed number.")

if __name__ == "__main__":
    main()