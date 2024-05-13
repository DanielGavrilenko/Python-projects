import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
attempts = 0
guessed_number = 0
game_end = 0
play_game = "yes"


def guess_number():
    global guessed_number
    guessed_number = random.randint(1, 100)


def level_selection():
    global EASY_ATTEMPTS
    global HARD_ATTEMPTS
    global attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    while attempts == 0:
        if difficulty == "easy":
            attempts = EASY_ATTEMPTS
        elif difficulty == "hard":
            attempts = HARD_ATTEMPTS
        else:
            print("Incorrect input. Try again.")
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    print(f"You have {attempts} attempts remaining to guess the number.")


def comparing_number():
    global attempts
    global guessed_number
    global game_end
    number = int(input("Make a guess:"))
    if number > guessed_number:
        print("Too high")
    elif number < guessed_number:
        print("Too low")
    else:
        game_end = 1


print("welcome to the Number Guessing Game!")
while play_game == "yes":
    print("I'm thinking of a number between 1 and 100.")
    guess_number()
    level_selection()
    while game_end == 0:
        comparing_number()
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
        if attempts == 0:
            game_end = 2
    if game_end == 1:
        print("You win!!")
    if game_end == 2:
        print("You loose.")
    play_game = input("Do you want to try again?(yes/no)")
