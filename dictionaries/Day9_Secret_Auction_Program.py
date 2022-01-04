from Day9_Secret_Auction_Program_Logo import logo
import os

print(logo)
print("Welcome to Secret Auction Program!!!")

bidding_finished = False
total_bids = {}

while not bidding_finished:

    def add_biders(name, amount):
        total_bids[name] = amount
        return total_bids

    name = input("What is your name?: ")
    amount = int(input("What is your bid amount?: $"))
    x = add_biders(name, amount)
    # print(x)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_bidders == "yes":
        os.system("cls")
    else:
        bidding_finished = True
        print(total_bids)


def highest_bidder(bids):

    highest_bid = 0

    for bidder in bids:
        name = bids
        amount = bids[bidder]
        if amount > highest_bid:
            highest_bid = amount

    return highest_bid


x = highest_bidder(total_bids)
print(f"The highest bidder is {name} with bid amount {x}")
