import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Computer chose:")
print(game_images[user])

comp = random.randint(0, 2)
print(game_images[comp])

if user - comp == 1 or user - comp == -2:
    print("You win")
elif user - comp == 0:
    print("It's a draw")
else:
    print("You lose")
