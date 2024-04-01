from art import logo


def highest_bidder(bidder_list):
    max_bid = max(bidder_list, key=lambda x: x["price"])
    return max_bid["name"], max_bid["price"]

print(logo)
print("Welcome to the secret auction program.")

list_participants = []

while True:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    list_participants.append({"name": name, "price": price})
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if more_bidders != "yes":
        break

winner_name, winning_bid = highest_bidder(list_participants)
print(f"The winner is {winner_name} with a bid of ${winning_bid}")
