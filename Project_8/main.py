from art import logo
from art import alphabet


def encrypt(en_text, shift_cd):
    result = ""
    for i in en_text:
        if i in alphabet:
            pos = alphabet.index(i)
            new_pos = pos + shift_cd
            while new_pos >= len(alphabet):
                new_pos -= len(alphabet)
            result += alphabet[new_pos]
        else:
            result += i
    print(f"The encoded text is: {result}")


def decrypt(de_text, shift_cd):
    result = ""
    for i in de_text:
        if i in alphabet:
            pos = alphabet.index(i)
            new_pos = pos - shift_cd
            while new_pos < 0:
                new_pos += len(alphabet)
            result += alphabet[new_pos]
        else:
            result += i
    print(f"The decoded text is {result}")


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(en_text=text, shift_cd=shift)
elif direction == "decode":
    decrypt(de_text=text, shift_cd=shift)
else:
    print("incorrect input")
