
# choose 0 for rock , 1 for paper , 2 for sessor

import random

rock_image = """
    -----------
  (           )
 (             )
(               )
 (             )
  (___________)
"""

paper_image = """
    -----------
  |           |
  |           |
  |           |
  |           |
  |___________|
"""

scissors_image = """
   --------
  (        )
   \      /
    \    /
     |  |
     \__/
"""




choice =int(input("choose 0 for rock , 1 for paper , 2 for sessor"))
if choice == 0:
    print("You chose Rock:")
    print(rock_image)
elif choice == 1:
     print(paper_image)
elif choice == 2:
     print(scissors_image)

print("computer choice")
computer_choice = random.randint(0,2)
print(computer_choice)

if computer_choice==0:
     print(rock_image)
elif computer_choice==1:
     print(paper_image)
elif computer_choice==2:
     print(scissors_image)

#win or lose
if choice==computer_choice:
     print("match is tie")

elif (choice==0 and  computer_choice==2) or(choice==1 and  computer_choice==0) or (choice==2 and  computer_choice==1) :
  print("you win ")
else:
     print("you lose")