import pandas

def generate_phonetic():
    user_word = input("Please write word:")
    letters = [n for n in user_word]
    try:
        result = [dictionary[letter.upper()] for letter in letters]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = dict()
for (index, row) in data.iterrows():
    dictionary.update({row["letter"]: row["code"]})
generate_phonetic()
# or
# dictionary = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

