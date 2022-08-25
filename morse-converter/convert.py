from alphabet import morse_dict


def text_to_morse(x):
    x = x.split()
    morse_text= []

    for word in x:
        for letter in word:
            try:
                morse_text.append(morse_dict[letter.upper()])
            except KeyError:
                morse_text.append(morse_dict["un"])
            morse_text.append(" ")
        morse_text.append("/")

    return "".join(morse_text)


def morse_to_text(x):
    words = x.split("/")
    words.pop()
    words_splitted = []
    for word in words:
        words_splitted.append(word.split())

    print(words_splitted)

    clear_text = []
    for word in words_splitted:
        for letter in word:
            try:
                for key, value in morse_dict.items():
                    if value == letter and value != "#":
                        clear_text.append(key)
                    elif value == letter and value == "#":
                        clear_text.append(value)
            except:
                clear_text.append("#")
        clear_text.append(" ")

    return "".join(clear_text)
