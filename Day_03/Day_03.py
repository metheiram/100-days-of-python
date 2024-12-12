print("Welcome to Treasure Island! Your mission is to find the treasure.")

first = input("Choose the path: left or right? ").lower()

if first == "left":
    # Continue the game
    print("You chose the left path, so let's dive into adventure!")

    choice = input('You have come to the lake. There is an island in the lake. '
                   'Type "wait" or "swim" to proceed next: ').lower()

    if choice == "wait":
        # Game continues
        door = input("You arrived at the island. There is a house with three doors. "
                     "You have to select the right door to proceed next. Type: right, blue, or yellow: ").lower()
        
        if door == "yellow":
            print("Congratulations, you found the treasure! You win!")
        else:
            print("Game over.")
    else:
        print("You were attacked by a shark. Game over.")
else:
    print("You fell down a hole. Game over.")

