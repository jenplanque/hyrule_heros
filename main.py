from battle import battle, clear_screen
from characters import Ganon
from create_character import create_character
 

# "Hyrule Heroes" - a Turn-based CLI Game, based off of "Zelda - Breath of the Wild"

# MARK: Welcome Screen
def welcome_screen():
    clear_screen()  # Clear the screen
    input("\n\nWelcome to Hyrule Heroes! 🗡️ 🛡️ 💪\n") # hit enter to continue
    clear_screen()  # Clear the screen

# Main function to handle the flow of the game
def main():
    welcome_screen() # Display welcome screen
    player = create_character() # create the player
    boss = Ganon("Calamity Ganon") # initialize the boss
    clear_screen()  # Clear the screen
    player.character_intro(boss) # Display beginning stats
    battle(player, boss) # start the battle
    
# Run the game
if __name__ == "__main__":
    main()
