#step o1 : create a word list choose a random word and store it in the variable and then print it 
import random
word_list=["Apple","pear","alice"]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholder=""
word_length =len(choosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)


#step 02 : take input from to guess the number in a lower case and store them into a variable 
game_over= False

correct_letter=[]
while not game_over:
    guess= input("Guess a number:").lower()

#step 03 : cheak the letter the user guess is match the choosen word if it is right print right otherwise
# print wrong

    display=""
    for letter in choosen_word:
        if letter == guess:
        
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
             display += "-"
    print(display)


if "-" not in display:
    game_over=True
    print("you win")

    
