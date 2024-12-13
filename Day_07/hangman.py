import random

# Hangman stages
stages = [
    """ 
 +---+
 |   |
 0   |
/|\\  |
/ \\  |
     |
========
 """,
    """ 
 +---+
 |   |
 0   |
/|\\  |
/    |
     |
========
 """,
    """ 
 +---+
 |   |
 0   |
/|\\  |
     |
     |
========
 """,
    """ 
 +---+
 |   |
 0   |
/|   |
     |
     |
========
 """,
    """ 
 +---+
 |   |
 0   |
 |   |
     |
     |
========
 """,
    """ 
 +---+
 |   |
 0   |
     |
     |
     |
========
 """,
    """ 
 +---+
 |   |
     |
     |
     |
     |
========
 """
]

# List of words
word_list = ["Apple", "pear", "alice"]

# Number of lives
lives = 6

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")  # For testing, remove in the final game

# Initialize placeholders for the word
placeholder = "-" * len(chosen_word)
print(placeholder)

# Game loop
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Ensure the user inputs only one letter and is not empty
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        print(f"Good job! {guess} is in the word.")
        correct_letters.append(guess)
    else:
        print(f"Oops! {guess} is not in the word.")
        lives -= 1

    # Update the displayed word with guessed letters
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "-"
    
    print(display)

    # Check if the player has guessed the word or lost
    if lives == 0:
        print("You lose!")
        print(f"The word was: {chosen_word}")
        break

    if "-" not in display:
        print("You win!")
        break

    # Display the current hangman stage
    print(stages[lives])

