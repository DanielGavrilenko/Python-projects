import pandas

user_word = input("Please write word\n")
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = dict()
for (index, row) in data.iterrows():
    dictionary.update({row["letter"]: row["code"]})

# or
# dictionary = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

letters = [n for n in user_word]
result = [dictionary.get(letter.upper()) for letter in letters]
print(result)
