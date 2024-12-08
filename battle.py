import os
from characters import Character

def clear_screen():
    os.system('clear')
            
def battle(player, boss):
    while boss.health > 0 and player.health > 0:
        clear_screen()
        print("\n--- Your Turn ---\n")
        print("1. Attack")
        print("2. Special Abilities")
        print("3. Heal")
        print("4. View Stats\n")
        choice = input("Choose an action (1-4): ")
        if choice == '1':
            clear_screen()  # clear the screen
            player.attack(boss)
            if boss.health == 0:
                continue
            else:            
                boss.regenerate()
                input()  # pause for user to hit enter
                boss.attack(player)
        elif choice == '2':
            clear_screen()
            print("\nChoose special ability:\n")
            print(f"1. {player.special1.__name__.replace('_', ' ').title()}")
            print(f"2. {player.special2.__name__.replace('_', ' ').title()}")
            special = input("Choose a special ability (1-2): ")
            if special == '1':
                clear_screen()
                player.special1(boss)
                if boss.health == 0 or player.health == 0:
                    continue
                else:            
                    boss.regenerate()
                    input()  
                    boss.attack(player)
            elif special == '2':
                clear_screen()
                player.special2(boss)
                if boss.health == 0:
                    continue
                else:   
                    boss.regenerate()
                    input(" ")  
                    boss.attack(player)
            else:
                input("Invalid choice. Please try again.\n")
        elif choice == '3':
            clear_screen()  
            player.heal()
            boss.regenerate()
            input(" ")
            boss.attack(player)
        elif choice == '4':
            clear_screen()
            player.display_stats(boss)
            continue
        else:
            clear_screen()
            input("Invalid choice, try again.\n")
    else:
        if boss.health == 0:
            clear_screen()
            input(f"Victory! {boss.name} has been defeated! 💀\n")
            input("You are the Hyrule Hero! 🏆")
            clear_screen()
        else:
            clear_screen()
            input(f"{player.name} has been defeated! 💀\n")
            input("Game Over! 😵")
            clear_screen()
    
