letters = ["A", "a", "B", "b", "@", "C", "c", "D", "d", "E", "e", "F", "f","G", "g", "H", "h", "I", "i", "J", "$", "j",
         "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "#", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
         "U", "u", "V", "v", "W", "w", "x", "Y", "y", "Z", "z", "!"]


def encode(word, n):
    ls = []
    for i in range(len(word)):
        ind_of_letter = letters.index(word[i])
        if ind_of_letter - n >= -len(letters):
            ls.append(letters[ind_of_letter - n])
        else:
            new_ind = (ind_of_letter - n) + len(letters)
    encrypted_word = "".join(ls)
    return encrypted_word


def decode(word, n):
    ls = []
    for i in range(len(word)):
        ind_of_letter = letters.index(word[i])
        if ind_of_letter + n <= len(letters)-1:
            ls.append(letters[ind_of_letter + n])
        else:
            new_ind = (ind_of_letter + n) - len(letters)
            ls.append(letters[new_ind])
    decrypted_word = "".join(ls)
    return decrypted_word


def get_number_of_cypher():
    while True:
        number = input("What is your key number to encode-decode?:").strip()
        if number.isdigit():
            number = int(number)
            return number
        else:
            print("Wrong Input!TRY AGAIN!")


def get_user_word():
    while True:
        word = input("What is the word:")
        if word.isascii():
            return word
        else:
            print("Try only characters!")


def main():
    while True:
        print("*" * 20)
        print("0-Exit")
        print("1-Encode")
        print("2-Decode")
        print("*" * 20)
        inputed_choice = input("What you want to do(0-1-2)?:").strip()
        if inputed_choice.isdigit():
            inputed_choice = int(inputed_choice)
            if inputed_choice == 0:
                exit()
            elif inputed_choice == 1:
                word = get_user_word()
                number = get_number_of_cypher()
                encoded_word = encode(word, number)
                print(f"The decrypted word is:'{encoded_word}'")
            elif inputed_choice == 2:
                word = get_user_word()
                number = get_number_of_cypher()
                decoded_word = decode(word, number)
                print(f"The decrypted word is:'{decoded_word}'")
            else:
                print("Wrong Input! Please try 0 or 1 or 2.")
        else:
            print("*" * 20)
            print("Wrong Input! TRY AGAIN!")

main()