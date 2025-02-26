
print("Welcome to Blind auction!")

def bidding(bid):
    amt=0
    for bidder in bid: #bidder is key in bid(dictionary)
        bid_amt=bid[bidder]
        if bid_amt>amt:
            amt=bid_amt
            winner=bidder
    print(f"highest bid is : {amt} from {winner}")

bid_list={}

should_continue=True
while should_continue:    
    name=input("Enter the name of the bidder: ")
    price=int(input("Enter your bidding $; "))
    bid_list[name]=price
    user_input=input("Is there any other bidder? (Y/N) ").lower()
    if user_input=="n":
        should_continue=False
        bidding(bid_list)
    elif user_input=="y":
        print("\n"*20)

        
    
    
    
