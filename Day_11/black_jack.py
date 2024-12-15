import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards.'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def campare(u_score, c_score):
    if c_score == u_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack."
    elif u_score == 0:
        return "Win with a blackjack!"
    elif u_score > 21:
        return "You went over, you lose."
    elif c_score > 21:
        return "Opponent went over, you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose."

# Game setup
user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

# User's turn
while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()
        if user_should_deal == "y":
            user_card.append(deal_card())  # Fix: call deal_card() directly
        else:
            is_game_over = True

# Computer's turn
while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

# Final output
print(f"Your final hand: {user_card}, final score: {user_score}")
print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
print(campare(user_score, computer_score))
