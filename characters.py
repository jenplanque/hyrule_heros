import os
import random

def clear_screen(): # function to clear the terminal screen
    os.system('clear')
        
            
# MARK: Character class (parent)
class Character:
    def __init__(self, name, health, attack_power, weapon):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.weapon = weapon
  
# Beginning Character Stats
    def character_intro(self, opponent):
        print(f"\nBeginning Stats\n"
              "-------------\n"
              f"{self.name}'s Stats:\n"
              f"Health: {self.health}/{self.max_health}\nAttack Power: "
              f"{self.attack_power}\nWeapon: {self.weapon}\n")
        print(f"Ganon's Stats:\nHealth: {opponent.health}/{opponent.max_health}\n"
              f"Attack Power: {opponent.attack_power}\nWeapon: {opponent.weapon}\n")
        input(("-" * 30) + "\n") # pause till user hits enter
        clear_screen()
  
# Attack function
    def attack(self, opponent):
        opponent.health -= self.attack_power
        if opponent.health <= 0:
            opponent.health = 0
        input(f"\n{self.name} attacks {opponent.name} with {self.weapon}, causing "
        f"{self.attack_power} HP damage and reducing their health to "
        f"{opponent.health} HP! 💥\n") 
               
# Display Stats
    def display_stats(self, opponent):
        print("\n" + ("-" * 30) + "\n")
        print(f"{self.name}'s Stats:\nHealth: {self.health}/{self.max_health}\n")
        print()
        print(f"{opponent.name}'s Stats:\nHealth: {opponent.health}/{opponent.max_health}\n")
        input("\n" + ("-" * 30) + "\n") 
        clear_screen()  
    
# Heal method
    def heal(self):
        clear_screen()  
        random_heal = random.randint(0, (30 - 20) // 5) * 5 + 10 
        self.health += random_heal
        if self.health > self.max_health:
            self.health = self.max_health # prevents health from exceeding max_health
        input(f"{self.name} gains {random_heal} HP! 💚\n"
              f"Current health: {self.health}/{self.max_health} HP\n")
    
        
# MARK: Ganon class
class Ganon(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, weapon="fire balls")  
    
    # Ganon's special ability
    def regenerate(self): 
        self.health += 10
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 10 HP, raising total health to "
              f"{self.health} HP! 💚")
     
# MARK: Urbosa class     
class Urbosa(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=20, weapon="trident")  
    
    # Urbosa's special abilities:
    def urbosas_fury(self, opponent):
        power = "Urbosa's Fury"
        enemy_damage = self.attack_power * 1.35
        opponent.health -= enemy_damage   
        if opponent.health <= 0:
            opponent.health = 0
        self_damage = 15
        self.health -= self_damage 
        if self.health <= 0:
            self.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name} causing "
              f"{enemy_damage} HP damage, which reduces their health to "
              f"{opponent.health} HP."
              f"During battle, {self.name} also sustains injuries, causing "
              f"{self_damage} HP damage to self, and reducing health to "
              f"{self.health} HP. ⚡️💥\n")
        if opponent.health == 0 or self.health == 0:
            return
    
    def perfect_guard(self, opponent):
        power = "Perfect Guard"
        enemy_damage = self.attack_power * 1.15
        opponent.health -= enemy_damage 
        if opponent.health <= 0:
            opponent.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name}, "
                f"causing {enemy_damage} HP damage which reduces their health to "
                f"{opponent.health} HP. \n") 
        if opponent.health == 0:
            return
    
    special1 = urbosas_fury
    special2 = perfect_guard
    
# MARK: Revali class
class Revali(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30, weapon="falcon's bow")  
    
    # Revali's special abilities:
    def perfect_shot(self, opponent):
        power = "Perfect Shot"
        enemy_damage = self.attack_power * 1.25
        opponent.health -= enemy_damage   
        if opponent.health <= 0:
            opponent.health = 0
        self_damage = 15
        self.health -= self_damage 
        if self.health <= 0:
            self.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name} causing "
              f"{enemy_damage} HP damage, which reduces their health to "
              f"{opponent.health} HP."
              f"During battle, {self.name} also sustains injuries, causing "
              f"{self_damage} HP damage to self, and reducing health to "
              f"{self.health} HP. ⚡️💥\n")
        if opponent.health == 0 or self.health == 0:
            return  
        else:
            clear_screen()  
            print(f"\n{self.name} uses {power} to strike {opponent.name} causing "
              f"{enemy_damage} HP damage, and reducing their health to {opponent.health} "
              f"HP. {self.name} also sustains {self_damage} HP damage to self, "
              f"reducing health to {self.health} HP. ⚡️💥\n")
    
    def high_jump(self, opponent):
        power = "High Jump"
        enemy_damage = self.attack_power * 1.15
        opponent.health -= enemy_damage 
        if opponent.health <= 0:
            opponent.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name}, "
                f"causing {enemy_damage} HP damage which reduces their health to "
                f"{opponent.health} HP. \n") 
        if opponent.health == 0:
            return
    
    special1 = perfect_shot
    special2 = high_jump
    
# MARK: Mipha class
class Mipha(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25, weapon="harpoon") 
    
    # Mipha's special abilities:
    def shark_scurry(self, opponent):
        power = "Shark Scurry"
        enemy_damage = self.attack_power * 1.5
        opponent.health -= enemy_damage   
        if opponent.health <= 0:
            opponent.health = 0
        self_damage = 15
        self.health -= self_damage 
        if self.health <= 0:
            self.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name} causing "
              f"{enemy_damage} HP damage, which reduces their health to "
              f"{opponent.health} HP."
              f"During battle, {self.name} also sustains injuries, causing "
              f"{self_damage} HP damage to self, and reducing health to "
              f"{self.health} HP. ⚡️💥\n")
        if opponent.health == 0 or self.health == 0:
            return
    
    def magnesis(self, opponent):
        power = "Magnesis"
        enemy_damage = self.attack_power * 1.15
        opponent.health -= enemy_damage 
        if opponent.health <= 0:
            opponent.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name}, "
                f"causing {enemy_damage} HP damage which reduces their health to "
                f"{opponent.health} HP. \n") 
        if opponent.health == 0:
            return
        
    special1 = shark_scurry
    special2 = magnesis

# MARK: Daruk class
class Daruk(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20, weapon="stone crusher")  
    
    # Daruk's special abilities:
    def remote_bomb(self, opponent):
        power = "Remote Bomb"
        enemy_damage = self.attack_power * 1.35
        opponent.health -= enemy_damage   
        if opponent.health <= 0:
            opponent.health = 0
        self_damage = 25
        self.health -= self_damage 
        if self.health <= 0:
            self.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name} causing "
              f"{enemy_damage} HP damage, which reduces their health to "
              f"{opponent.health} HP."
              f"During battle, {self.name} also sustains injuries, causing "
              f"{self_damage} HP damage to self, and reducing health to "
              f"{self.health} HP. ⚡️💥\n")
        if opponent.health == 0 or self.health == 0:
            return
    
    def rock_block(self, opponent):
        power = "Rock Block"
        enemy_damage = self.attack_power * 1.15
        opponent.health -= enemy_damage 
        if opponent.health <= 0:
            opponent.health = 0
        input(f"\n{self.name} uses {power} to attack {opponent.name}, "
                f"causing {enemy_damage} HP damage which reduces their health to "
                f"{opponent.health} HP. \n") 
        if opponent.health == 0:
            return
    
    special1 = remote_bomb
    special2 = rock_block