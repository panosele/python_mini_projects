import random


# globals
letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f","G", "g", "H", "h", "I", "i", "J", "j",
         "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
         "U", "u", "V", "v", "W", "w", "x", "Y", "y", "Z", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

chars = ["!", "@", "#", "$", "%", "&", "*"]

luck = [0, 1, 2]


def generate_password(length_of_password):
    new_password_list = []
    for _ in range(length_of_password):
        r_ch = random.choice(luck)
        if r_ch == 0:
            new_password_list.append(random.choice(letters))
        elif r_ch == 1:
            new_password_list.append(random.choice(numbers))
        else:
            new_password_list.append(random.choice(chars))

    return "".join(new_password_list)
