from random import choice


# globals
word_pool = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle",
"bookworm", "boxcar", "staff", "strength", "strengths", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]


def pick_a_word(word_ls):
    hidden_word = choice(word_ls)
    return hidden_word.lower()


def show_rules():
    print('''The rules are simple:
Randomly a word is chosen and is hidden. You will know the number of letters and you will try to guess the hidden word 
letter by letter.
You have 8 tries or you lose.
if you find the word you WIN!
Let's PLAY!''')


def show_hidden_word(guessed_letters, hidden_word):
    for letter in hidden_word:
        if letter in guessed_letters:
            print(" " + letter + " ", end="")
        else:
            print(" _ ", end="")
    print("\n")


def play(hidden_word):
    guessed_letters = []
    tries = 0
    while tries < 8 and len(guessed_letters) != len(hidden_word):
        tries += 1
        print("*" * 20)
        print(f"TRY:{tries}")
        print(f"The numbers of the word are {len(hidden_word)}")
        show_hidden_word(guessed_letters, hidden_word)
        pick_a_letter = (input("What is your letter:")).strip()
        if (pick_a_letter in hidden_word) and pick_a_letter not  in guessed_letters:
            guessed_letters.append(pick_a_letter)
            print("You guessed correctly!")
            show_hidden_word(guessed_letters, hidden_word)
        else:
            print("Not a good guess!")
        print("*" * 20)

    if len(guessed_letters) == len(hidden_word):
        print("*" * 20)
        show_hidden_word(guessed_letters, hidden_word)
        print("NICE. YOU WON!")
        print("*" * 20)
    else:
        print("*" * 20)
        print("YOU LOST! You can try again!")
        print("*" * 20)


def menu():
    while True:
        print("2-RULES")
        print("1-PLAY")
        print("0-EXIT")
        menu_choice = (input("Choose 0 or 1 or 2:")).strip()
        if menu_choice.isdigit():
            menu_choice = int(menu_choice)
            if menu_choice == 0 or menu_choice == 1 or menu_choice == 2:
                return menu_choice
            else:
                print("Please 0 or 1 or 2")
        else:
            print("Wrong Input. TRY AGAIN!")


def main():
    while True:
        menu_choice = menu()
        if menu_choice == 0:
            exit()
        elif menu_choice == 1:
            hidden_word = pick_a_word(word_pool)
            play(hidden_word)
        else:
            show_rules()


# main
main()


