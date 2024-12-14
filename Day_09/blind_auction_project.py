# Blind auction - A simplified bidding process

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

# Function to determine the highest bid and the winner
def highest_bid(bidder_dictionary):
    winner = ""
    highest_bid = 0
    for bidding in bidder_dictionary:
        bid_amount = bidder_dictionary[bidding]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidding
    print(f"The winner is {winner} with the bid of ${highest_bid}")

# Initialize the bid dictionary
bids = {}

# Begin bidding process
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    bid = float(input("What is your bid $"))  # Ensure bid is a float for proper comparison
    
    # Store the bid in the dictionary
    bids[name] = bid
    
    # Ask if others want to bid
    result = input("Others for bid (yes/no)? ").lower()
    
    if result == "yes":
        print("\n" * 30)  # Clear the screen (this won't work in all environments)
    elif result == "no":
        continue_bidding = False
        highest_bid(bids)  # Call the function with the bids dictionary
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
