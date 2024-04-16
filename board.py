from dice import dice
from utility import get_input

def display_game_menu():
        print("1. Roll Dice")
        print("2. Check Position")
        print("3. Check Snakes & Ladders")
        print("4. Help")
        print("5. Exit game")

def help():
    print("Instructions:")
    print("- Enter '1' to roll the dice.")
    print("- Enter '2' to check your current position.")
    print("- Enter '3' to check if you've landed on a snake or ladder.")
    print("- Enter '4' to display this help menu.")
    print("- Enter '5' to exit the game.")
    
def game_menu(position):
    
    while True:
        display_game_menu()  
        print()
        option = get_input(1, 5, "Enter a number: ", "Invalid option. Please enter a number between 1 and 5.")
        break

    if option == 1:
        position += dice()  
        print(f"You are current position: {position}\n")
        return position

    elif option == 2:
        print(f"You are at position {position}")

    elif option == 3:
        print("There are ladders at 1, 4, 8, 21, 28, 50, 80, 71")
        print("There are snakes at 32, 36, 48, 62, 88, 95, 97")

    elif option == 4:
        help()
    
    else:
        return position
    
    print()
        
    game_menu(position)
