#Secret auction
Auction = {}
end = True
def max_bid(Auction_bid):
    max = 0
    winner = ""
    for key in Auction_bid:
     if Auction_bid[key] > max:
        max = Auction_bid[key]
        winner=key
    print(f"The winner is {winner} with a bid of ${max}")

while end:
    name = input("What is your name? ")
    value = int(input("What is your bid? $"))
    Auction[name]=value
    message = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if message == "no":
        end = False
    

max_bid(Auction)



