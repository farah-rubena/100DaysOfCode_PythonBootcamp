import random

logo = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """

print(logo)
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = [
    "abruptly",
    "absurd",
    "abyss",
    "affix",
    "askew",
    "avenue",
    "awkward",
    "axiom",
    "azure",
    "bagpipes",
    "bandwagon",
    "banjo",
    "bayou",
    "beekeeper",
    "bikini",
    "blitz",
    "blizzard",
    "boggle",
    "bookworm",
    "boxcar",
    "boxful",
    "buckaroo",
    "buffalo",
    "buffoon",
    "buxom",
    "buzzard",
    "buzzing",
    "buzzwords",
    "caliph",
    "cobweb",
    "cockiness",
    "croquet",
    "crypt",
    "curacao",
    "cycle",
    "daiquiri",
    "dirndl",
    "disavow",
    "dizzying",
    "duplex",
    "dwarves",
    "embezzle",
    "equip",
]

lives = 6
# Generate a random word
random_word = random.choice(word_list)
print(f"Psst the random word is {random_word}")
# Generate as many spaces as the random word
display_board = []

for char in random_word:
    display_board.append("_")
print(display_board)

blanks_on_board = True

while blanks_on_board:
    # Ask user guess
    user_guess = input("Enter your guess: ").lower()

    if user_guess in display_board:
        print(f"You've already guessed {user_guess}")

    # Check if guessed letter is in the word
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_guess:
            display_board[position] = user_guess
    print(display_board)

    if user_guess not in random_word:
        print(f"You've guessed {user_guess}, that is not in the word. You loose a life")
        lives -= 1
        if lives == 0:
            blanks_on_board = False
            print("You loose!!!")

    if "_" not in display_board:
        blanks_on_board = False
        print("You win!!!")

    print(stages[lives])
