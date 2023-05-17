import art
import os

print(art.logo)
bids ={}
end_of_bids = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bidding_record[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of R{highest_bid}")

while not end_of_bids:
    name = input("What is your name? ")
    bid_price = int(input("Enter your bid? "))
    bids[name] = bid_price
    # print(bids)
    other_bidders = input("Are the any other bidders? Yes or No ")
    if other_bidders.lower() == "no":
        end_of_bids = True
        find_highest_bid(bids)


