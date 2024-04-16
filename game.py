from utility import get_input
from board import game_menu

players = []

def display_start_menu():
    print(f"\n{'GAME MENU':^{19}}\n{'_' * (19)}\n")
    print("1. Start game")
    print("2. Add players")
    print("3. Help")
    print("4. Exit game")
    
def help_menu():
    print("Instructions:")
    print("- Enter '1' to start the game.")
    print("- Enter '2' to add players.")
    print("- Enter '3' to display this help menu.")
    print("- Enter '4' to exit the game.")

def create_players():
    global players
    num_players = get_input(2, 4, "Enter the number of players: ", "Please enter a number between 2 and 4 of players")
    if  2 <= num_players <= 4:
        players = []

        for i in range(num_players):
            name = input(f"Enter player {i + 1}'s name: ")
            players.append([name, 0])
        
        return players

    create_players()

def start_menu():
    global players
    print("\nWelcome to Snakes and Ladders\n")
    
    while True:
        
        display_start_menu()
        
        print()
        
        option = get_input(1, 4, "Enter your option number: ", "Enter correct option")
        
        if option == 1:
            if len(players) >= 2:
                return players
            else:
                print('Not enough Players')
                print(f"You have {len(players)} current players")
        
        elif option == 2:
            players = create_players()
            
        elif option == 3:
            help_menu()
            
        else:
            break

        
        
def main():
    global players
    players = start_menu()
    
    while True:
        for player in players:
            name, position = player

            print(f"\nCurrently {name}'s turn\n")
            position = game_menu(position)
            player[1] = position
            
            if int(position) >= 100:
                print("You win", name)
                return
            
if __name__ == '__main__':
    main()
