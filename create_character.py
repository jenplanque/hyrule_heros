from characters import Urbosa, Revali, Mipha, Daruk

# Function to create player based on user's character choice
def create_character():
    print("\nChoose your character class:")
    print()
    print("1. Urbosa - The Gerudo Champion") # The Gerudo Champion
    print("2. Revali - The Rito Champion") # The Rito Champion
    print("3. Mipha - The Zora Champion")  # The Zora Champion
    print("4. Daruk - The Goron Champion")  # The Goron Champion
    print()
    class_choice = input("Enter the number of your Character choice: ")
    name = input("Enter your character's name: ")
    name = name.title()
    # # os.system('clear')  # Clear the screen

    if class_choice == '1':
        return Urbosa(name)
    elif class_choice == '2':
        return Revali(name)
    elif class_choice == '3':
        return Mipha(name)
    elif class_choice == '4':
        return Daruk(name)   
    else:
        print("Invalid choice. Defaulting to Urbosa class.\n")
        return Urbosa(name)