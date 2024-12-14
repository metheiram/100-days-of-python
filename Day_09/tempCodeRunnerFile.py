# blind auction



hammer = """
   
  ___________
 |           |
 |   bid     |
 |           |
 |___________|
    |     |
    |     |
    |     |
    |     |
    |_____|
"""


name=print(input("what is your name"))
bid=print(input("what is your bid"))

dictionary={   
          "name":name,
          "bid":bid,
         }
for other in dictionary:
    other=input(print("others for bid ?")).lower
if other=="yes":
    print("clear the screen")
else:
    print("find the heighest bid and declare them as a winner")

    
  