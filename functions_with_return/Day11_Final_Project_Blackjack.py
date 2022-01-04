import random
from Day11_Final_Project_Blackjack_Logo import logo
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def deal_card():
    # Step 1: pick out 2 random cards from the deck
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """takes a list o cards and returns the score"""

    # Check for black Jack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # replace 11 eith 1 if sum of cards > 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_function(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "You Lose, opponent has a Black Jack"
    elif user_score == 0:
        return "You Win with a BlackJack"
    elif user_score > 21:
        return "You went over 21. You loose"
    elif computer_score > 21:
        return "Opponent went over 21. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You loose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    computer_first_card = computer_cards[0]

    game_over = False

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards {computer_first_card}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
                print("Thankyou for playing BlackJack!!!")

    while computer_score != 0 and computer_score < 17:

        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand was {user_cards} and score was {user_score}")
    print(f"Computer's final hand was {computer_cards} and score was {computer_score}")
    print(compare_function(user_score, computer_score))


while (
    input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y"
):
    system("cls")
    play_game()
