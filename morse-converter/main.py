import tkinter
from tkinter import END, messagebox, Canvas, PhotoImage
from convert import text_to_morse, morse_to_text

FONT = ("Courier", 12)
root = tkinter.Tk()
root.wm_minsize(600, 400)
root.maxsize(2000, 1800)
root.title("Morse Code Converter")
root.configure(bg="#ca91ff", padx=30, pady=30)

canvas = Canvas(width=300, height=290, bg="#ca91ff", highlightthickness=0)
logo_img = PhotoImage(file="logo1.png")
canvas.create_image(150, 145, image=logo_img)
canvas.grid(row=3, column=4, rowspan=6, columnspan=1, pady=40)

def exit_the_programm():
    exit(0)

def get_value():
    return v.get()

def convert():
    radio_option = get_value()
    if radio_option == 1:
        text_to_convert = text_textbox.get("1.0", "end")
        converted_text = text_to_morse(text_to_convert)
        morse_textbox.insert(END, converted_text)
        return text_to_convert, radio_option
    elif radio_option == 2:
        text_to_convert = morse_textbox.get("1.0", "end")
        converted_text = morse_to_text(text_to_convert)
        text_textbox.insert(END, converted_text)
        return text_to_convert, radio_option
    else:  # Just in case, regular the first is preselected
        messagebox.showerror(title="No selected option.", message="Check one of the options!\n\n")

header_label = tkinter.Label(text="Morse code converter", font=("Courier", 26, "bold"), bg="#ca91ff", pady=15)
header_label.grid(row=0, column=1, columnspan=3)


v = tkinter.IntVar(root, 1)
A = tkinter.Radiobutton(root, text=" Text -> Morse", variable=v, value=1, bg="#ca91ff", command=get_value)
A.grid(row=1, column=2, columnspan=2)
B = tkinter.Radiobutton(root, text="Morse -> Text", variable=v, value=2, bg="#ca91ff", command=get_value)
B.grid(row=2, column=2, columnspan=2)

text_label = tkinter.Label(text="Text:", font=FONT, bg="#ca91ff", pady=20)
text_label.grid(row=3, column=2, columnspan=2)
text_textbox = tkinter.Text(root, height=6, width=65, bg="lightgrey")
text_textbox.grid(row=4, column=2, columnspan=2)
morse_label = tkinter.Label(text="Morse:", font=FONT, bg="#ca91ff", pady=20)
morse_label.grid(row=5, column=2, columnspan=2)
morse_textbox = tkinter.Text(root, height=6, width=65, bg="lightgrey")
morse_textbox.grid(row=6, column=2, columnspan=2)

convert_button = tkinter.Button(root, font=("Courier", 12, "bold"), bg="black", text="Convert", fg="darkorange",
                                width=15, activeforeground = "darkorange", activebackground="blue",
                                command=convert)
convert_button.grid(row=7, column=2, columnspan=2)

exit_button = tkinter.Button(text="EXIT", width=14, font=("Arial", 12), fg="orange",
                             bg="black", command=exit_the_programm)
exit_button.grid(row=8, column=4, columnspan=2)

root.mainloop()
