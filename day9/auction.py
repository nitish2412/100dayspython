from art import logo

print(logo)

bids = []
auction = True
while auction:
  name = input("Waht is your name? ")
  bid_val = int(input("what is your bid? $"))
  bid={}
  bid["name"]=name
  bid["bid"]=bid_val
  bids.append(bid)
  more_bidders=input("Are there any others bidders? Type 'yes' or 'no'")
  if more_bidders == "no":
    auction = False
  #else:
   # clear()
max_bid={"bid":0}

for bid in bids:
  print(bid)
  if bid["bid"] > max_bid["bid"]:
    max_bid=bid
winner_name=max_bid["name"]
winner_bid=max_bid["bid"]
print(f"The winner is {winner_name} with a bid of ${winner_bid}")
