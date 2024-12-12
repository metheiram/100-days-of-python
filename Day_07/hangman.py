#step o1 

import random

word_list=["charle","Alice","edicon"]
choose_words=random.choice(word_list)
#02

guess=input("Guess a words:").lower()

#03
for letter in choose_words:
    if letter == guess:
        print("right")
    else:
        print("wrong")

