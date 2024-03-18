from art import logo
list_participants = []


def highest_bidder(bidder_list):
    max_price = bidder_list[0]["price"]
    winner = bidder_list[0]["name"]
    for bidders in range(1, len(bidder_list)):
        if bidder_list[bidders]["price"] > max_price:
            max_price = bidder_list[bidders]["price"]
            winner = bidder_list[bidders]["name"]
    return [winner, max_price]


print(logo)
print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    list_participants.append({"name": name, "price": price})
    bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if bidders == "no":
        break
winner = highest_bidder(list_participants)
print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
