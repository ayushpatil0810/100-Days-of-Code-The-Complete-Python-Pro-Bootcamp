#Day 9
print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

def highest_bidder(bidding_data) :
    winner = ""
    highest_bid = 0
    for bidder in bidding_data :
        bid_amount = bidding_data[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner  = bidder
    print(f"The winner is {winner} with a bid of ₹ {highest_bid}")

data = {}

continue_bidding = True
while continue_bidding :
    name = input("What is your name ? : ")
    bid = int(input("What is your bid ? : ₹ "))
    data[name] = bid
    any_other_bidders = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if any_other_bidders == "no" :
        continue_bidding = False
        highest_bidder(data)
    elif any_other_bidders == "yes":
        print("\n" * 100)
