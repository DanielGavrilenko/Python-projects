import random
import hangman_art as art
import hangman_words as words

#word_list = ["apple", "balloon", "human", "history"]
print(art.logo)
chosen_word = random.choice(words.word_list)
current_word = []
for j in range(len(chosen_word)):
    current_word.append("_")
lives = 7
if_win = 0

while lives > 0 and if_win == 0:
    letter = input("Guess letter: ").lower()
    if_guess = 0
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            current_word[i] = letter
            if_guess = 1
    if "_" not in current_word:
        if_win = 1
    if if_guess == 0:
        lives -= 1
    if_guess = 0
    print(current_word, art.stages[lives-1])
if if_win == 1:
    print("You win")
else:
    print("You lose")
