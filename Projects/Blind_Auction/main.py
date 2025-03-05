from logo import logo

print(logo)

def highest_bid(bid):
    amt=0
    for bidder in bid:
        bid_amt=bid[bidder] #Fetches the biding amount by accesing the dictionary and "bid[]"" then bidder being the key => bid[bidder] 
        if bid_amt>amt: 
            amt=bid_amt
            winner=bidder
    print(f"Winner of the Auction : {bidder} with Bidding of {amt}$")

bid_list={}

Should_continue=True

while Should_continue:
    name=input("Enter your Name : ")
    price=int(input("Enter your Bid$ : "))
    bid_list[name]=price #stores the bidders name as key and bidding as value in bid dictionary
    new_bid=input("Is there any new bidder ?  Type \"Y/N\" ").lower()
    if new_bid=="n":
        Should_continue=False
        highest_bid(bid_list)#calls bidding function using bid_list
    elif new_bid=="y":
        print("\n"*100)
        


            
        
        
