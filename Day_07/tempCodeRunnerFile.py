#step o1 

import random

word_list=["charle","Alice","edicon"]
choose_words=random.choice(word_list)


#02

display=[]
for i in choose_words:
    display+= "_"
print(display)


#03
guess=input("Guess a words:").lower()

#04
for letter in choose_words:
    if display[letter] == guess:
        print("right")
    else:
        print("wrong")




