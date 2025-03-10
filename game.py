'''
This is the main game file that the game will actually run within. The functions will be imported from gamefunctions.py
and used here
'''
import gamefunctions
def main():
    '''This is the main game function, everything should run within this'''
    money = 100
    name = str(input('What is your name?\n'))
    gamefunctions.print_welcome(name)



    while True:
        print("\nWhat would you like to do?\n")
        print("1. Shop")
        print("2. Fight")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            gamefunctions.print_shop_menu()
            item_choice = input("What would you like to buy? \n")
            price = gamefunctions.SHOP_ITEMS[item_choice]
            money = gamefunctions.purchase_item(price, money, item_choice)


        elif choice == '2':
            money += gamefunctions.fight_manager()

        elif choice == '3':
            print(f'Goodbye')
            break

        else:
            print("That is not a valid number, please pick a listed number.")

if __name__ == "__main__":
    main()
