import os

from art import logo
print(logo,"\n")

print("Welcome to the secret auction program.\n")

others_bidders = "yes"
auction_dict = {}
while others_bidders == "yes":
  name = str(input("What is your name? "))
  bid = float(input("What's your bid? "))

  auction_dict[name] = bid

  others_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'.")).lower()
  os.system("cls")

def find_highest_bidder(auction_dict):
  max_value = 0
  winner = ""
  for bidder in auction_dict:
    bid_value = auction_dict[bidder]
    if bid_value > max_value:
      max_value = bid_value
      winner = bidder
  print(f"The winner is {winner} with a bid of R${max_value:.2f}")

find_highest_bidder(auction_dict)