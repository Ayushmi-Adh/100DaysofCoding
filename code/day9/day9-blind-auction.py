#Blind-Auction
from art import logo2
import os
print(logo2)
print("Welcome to the secret auction program.")
auction={}
finished_bid = False
def highest_bidder(bidding_record):
    highest_bid=0
    for bids in bidding_record:
        bid_amount=bidding_record[bids]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bids
    os.system("cls")
    print(f"The winner is {winner} with a bid of ${highest_bid}")
   

while finished_bid==False:
    name = input("What is your name?: ")
    bid_price = int(input("Enter your Bid:$"))
    auction[name] = bid_price
    more_users =input("Are there more people who wants to bid?(type 'yes' or 'no'): ").lower()
    
    if more_users== "yes":
        os.system("cls")
        
    elif more_users=="no":
        finished_bid = True
        highest_bidder(auction)





