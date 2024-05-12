from art import logo
import random

print(logo)
computer_hand = []
player_hand = []
border_number = 21
draw_card_number = 17
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card(hand):
    hand.append(random.choice(cards))


def generate_hand(hand):
    get_card(hand)
    get_card(hand)


def calculating_points(hand):
    suma = sum(hand)
    while suma > border_number and 11 in hand:
        hand.remove(11)
        hand.append(1)
        suma -= 10
    return suma


want_play = "yes"
while want_play == "yes":
    generate_hand(player_hand)
    generate_hand(computer_hand)
    print(f"Your hand is {player_hand}")
    print(f"Computer's hand is [{computer_hand[0]}, ?]")
    draw_card = input("Do you want to draw card?(yes/no)")
    while draw_card == "yes":
        get_card(player_hand)
        print(player_hand)
        draw_card = "no"
        if calculating_points(player_hand) <= border_number:
            draw_card = input("Do you want to draw card?(yes/no)")
    while calculating_points(computer_hand) < draw_card_number and calculating_points(player_hand) <= border_number:
        get_card(computer_hand)
    user_score = calculating_points(player_hand)
    computer_score = calculating_points(computer_hand)
    print(f"Your hand {player_hand}. You have {user_score} points")
    print(f"Computer's hand {computer_hand}. Computer has {computer_score} points")
    if user_score > border_number:
        print("You lose!!! Noob")
    elif computer_score > border_number:
        print("You win")
    elif user_score < computer_score:
        print("You lose!!!")
    elif user_score == computer_score:
        print("Draw")
    else:
        print("You win")
    want_play = input("Do you want to play again? (yes/no)")
    computer_hand = []
    player_hand = []
print("GG")
