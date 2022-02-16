import random


# globals
letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f","G", "g", "H", "h", "I", "i", "J", "j",
         "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
         "U", "u", "V", "v", "W", "w", "x", "Y", "y", "Z", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

chars = ["!", "@", "#", "$", "%", "&", "*"]

def total_length():
    while True:
        t = (input("What is the total length of the password(8 and bigger)?:")).strip()
        if t.isdigit():
            t = int(t)
            if t >= 8:
                return t
            else:
                print("Your number is too short.")
        else:
            print("Please type a number:")


def number_of_letters():
    while True:
        t = (input("How many letters you want in your password?:")).strip()
        if t.isdigit():
            t = int(t)
            return t
        else:
            print("Please type a number:")


def number_of_numbers():
    while True:
        t = (input("How many numbers you want in your password?:")).strip()
        if t.isdigit():
            t = int(t)
            return t
        else:
            print("Please type a number:")


def number_of_chars():
    while True:
        t = (input("How many special characters you want in your password?:")).strip()
        if t.isdigit():
            t = int(t)
            return t
        else:
            print("Please type a number:")


def menu():
    while True:
        print("****MENU****")
        print("1-Generate password")
        print("0-Exit")
        while True:
            menu_choice = (input("Select:")).strip()
            if menu_choice.isdigit():
                menu_choice = int(menu_choice)
                if menu_choice == 1 or menu_choice == 0:
                    return menu_choice
                else:
                    print("Wrong Input.Please select 1 or 2.")
            else:
                print("Wrong Input.Please type a number(1 or 2).")


def generate_password(let, nums, cha,l_pas, l=0, n=0, c=0):
    if c == 0 and n == 0:
        password_ls = []
        for _ in range(l_pas):
            password_ls.append(random.choice(let))
        print("*" * 18)
        print("".join(password_ls))
        print("*" * 18)
    elif c ==0:
        password_ls = []
        for _ in range(l):
            password_ls.append(random.choice(let))
        for _ in range(n):
            password_ls.append(random.choice(nums))
        random.shuffle(password_ls)
        print("*" * 18)
        print("".join(password_ls))
        print("*" * 18)
    else:
        password_ls = []
        for _ in range(l):
            password_ls.append(random.choice(let))
        for _ in range(n):
            password_ls.append(random.choice(nums))
        for _ in range(c):
            password_ls.append(random.choice(cha))
        random.shuffle(password_ls)
        print("*" * 18)
        print("".join(password_ls))
        print("*" * 18)


def procces(let, nums, cha, length_of_password):
    while True:
        lenght_of_letters = number_of_letters()
        if lenght_of_letters > length_of_password:
            print("This is bigger of your password length.TRY AGAIN!")
            continue
        else:
            break

    if lenght_of_letters == length_of_password:
        return generate_password(let, nums, cha,length_of_password, lenght_of_letters)

    while True:
        lenght_of_numbers = number_of_numbers()
        if lenght_of_numbers + lenght_of_letters > length_of_password:
            print("This is bigger of your password length.TRY AGAIN!")
            continue
        else:
            break

    if lenght_of_letters + lenght_of_numbers == length_of_password:
        return generate_password(let, nums, cha,length_of_password, lenght_of_letters, lenght_of_numbers)

    length_of_chars = length_of_password - lenght_of_letters - lenght_of_numbers
    print(f"The number of special characters is {length_of_chars}.")
    return generate_password(let, nums, cha,length_of_password, lenght_of_letters, lenght_of_numbers, length_of_chars)


def main(letters, numbers, chars):
    while True:
        menu_choice = menu()
        if menu_choice == 0:
            exit()
        else:
            length_of_password = total_length()
        procces(letters, numbers, chars, length_of_password)



# MAIN
main(letters, numbers, chars)