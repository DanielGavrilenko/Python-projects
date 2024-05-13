from art import logo
import random

print(logo)
computer_hand = []
player_hand = []
BORDER_NUMBER = 21
DRAW_CARD_NUMBER = 17
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card(hand):
    hand.append(random.choice(cards))


def generate_hand(hand):
    get_card(hand)
    get_card(hand)


def calculating_points(hand):
    suma = sum(hand)
    while suma > BORDER_NUMBER and 11 in hand:
        hand.remove(11)
        hand.append(1)
        suma -= 10
    return suma


def game_result(user, computer):
    user_score = calculating_points(user)
    computer_score = calculating_points(computer)
    print(f"Your hand {user}. You have {user_score} points")
    print(f"Computer's hand {computer}. Computer has {computer_score} points")
    if user_score > BORDER_NUMBER:
        print("You lose!!! Noob")
    elif computer_score > BORDER_NUMBER:
        print("You win")
    elif user_score < computer_score:
        print("You lose!!!")
    elif user_score == computer_score:
        print("Draw")
    else:
        print("You win")


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
        if calculating_points(player_hand) <= BORDER_NUMBER:
            draw_card = input("Do you want to draw card?(yes/no)")
    while calculating_points(computer_hand) < DRAW_CARD_NUMBER and calculating_points(player_hand) <= BORDER_NUMBER:
        get_card(computer_hand)
    user_score = calculating_points(player_hand)
    computer_score = calculating_points(computer_hand)
    game_result(player_hand, computer_hand)
    want_play = input("Do you want to play again? (yes/no)")
    computer_hand = []
    player_hand = []
print("GG")
