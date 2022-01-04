import string
from Day8_Final_project_Ceasers_Cypher_Logo import logo

print(logo)

alphabets = list(string.ascii_lowercase) * 2
# print(alphabets)
decipher_again = True

while decipher_again:
    direction = input("Type 'encode' to ENCRYPT or 'decode' to DECRYPT: ").lower()

    plain_text = input("Enter the text you wish to change: ").lower()

    cypher_shift = int(input("ENter the shift size: "))

    if cypher_shift > len(alphabets):
        cypher_shift %= 26

    def ceasers_cypher(text, shift, direction):
        cypher_text = ""

        if direction == "decode":
            shift *= -1

        for letter in plain_text:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position + shift
                new_letter = alphabets[new_position]
                cypher_text += new_letter
            else:
                cypher_text += letter
        print(f"The {direction}d text is {cypher_text}")

    ceasers_cypher(text=plain_text, shift=cypher_shift, direction=direction)

    try_again = input(
        "Would you like to decipher something else: type 'y' for yes or 'n' for no "
    ).lower()
    if try_again == "n":
        decipher_again = False
        print("Thankyou for playing Ceaser's Cypher!!!")
