# Importing Logo from the art.py
from art import logo
print(logo)

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','@','#','$','%','^','&','*','(',')']


# Creating Caesar function which contain both encrypt and decrypt function as well as characters which are not present in the list
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in characters:
            output_text += letter

        else:

            shifted_position = characters.index(letter) + shift_amount
            shifted_position %= len(characters)
            output_text += characters[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# While loop introduced to enable looping and asking the user for input 

should_continue = True

while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good- Bye")




