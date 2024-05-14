import random
from replit import clear

from game_data import data
from art import logo, vs

score = 0
end_of_game = 0


def get_random_account():
    return random.choice(data)


def check_answer(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return 'A'
    else:
        return 'B'


print(logo)
while end_of_game == 0:
    if score > 0:
        print(f"You're right. Your current score is {score}")
    account_a = get_random_account()
    print(f"Compare A: {account_a["name"]}, a {account_a["description"]} from {account_a["country"]}.")
    print(vs)
    account_b = get_random_account()
    print(f"Against B: {account_b["name"]}, a {account_b["description"]} from {account_b["country"]}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    print(logo)
    if guess == check_answer(account_a, account_b):
        score += 1
    else:
        score = 0
        print("You lost")
