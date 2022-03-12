from tkinter import *
from password_generator import generate_password
import clipboard
from tkinter import messagebox
import json
import PyInstaller


# ----------------------------SEARCH INFO-------------------------------------- #
def search():
    search_for = website_insert_entry.get()
    search_for = search_for.title()
    try:
        with open("data.json", "r") as fa:
            data = json.load(fa)
    except FileNotFoundError:
        messagebox.showerror(title="No Data", message="No data found.\n\nThere is no file with data.")
    else:
        for key, value in data.items():
            if key == search_for:
                messagebox.showinfo(title=key, message=f"These are the details:\n\nEmail: {data[key]['email']}"
                                                         f"\n\nPassword: {data[key]['password']}")
                break
        else:
            messagebox.showinfo(title="key", message=f"No information about this website")


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def random_password_generate():
    password_insert_entry.delete(0, END)
    new_pass = generate_password(16)
    password_insert_entry.insert(0, new_pass)


# ---------------------------- SAVE PASSWORD ---------------------------- #
def save_data():
    site = website_insert_entry.get().title()
    mail = email_username_insert_entry.get()
    pswr = password_insert_entry.get()
    clipboard.copy(pswr)
    new_data = {
        site: {
            "email": mail,
            "password": pswr
        }
    }
    if len(site) == 0 or len(pswr) == 0:
        messagebox.showinfo(title="Oooppssss", message="Please make sure you haven't left empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"These are the details entered"
                                               f":\n\nEmail:{mail}\n\nPassword:{pswr}\n\nSave info?")
        if is_ok:
            try:
                with open("data.json", "r") as fa:
                    data = json.load(fa)
            except FileNotFoundError:
                with open("data.json", "w") as fa:
                    json.dump(new_data, fa, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as fa:
                    json.dump(data, fa, indent=4)
            finally:
                website_insert_entry.delete(0, END)
                email_username_insert_entry.delete(0, END)
                email_username_insert_entry.insert(0, "panosfps1993@gmail.com")
                password_insert_entry.delete(0, END)


# ---------------------------- UI SETUP ----------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=80, bg="#5463ff")


canvas = Canvas(width=200, height=200, bg="#f4fcd9", highlightthickness=0)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2, padx=20, pady=20)

# LABELS

website_label = Label(text="Website:", bg="#5463ff")
website_label.grid(row=1, column=0, pady=5)

email_username_label = Label(text="Email/Username:", bg="#5463ff")
email_username_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:", bg="#5463ff")
password_label.grid(row=3, column=0, pady=5)

# ENTRIES

website_insert_entry = Entry(width=31, bg="white", bd=2, relief="groove")
website_insert_entry.grid(row=1, column=1, pady=5)
website_insert_entry.focus()

email_username_insert_entry = Entry(width=50, bd=2, relief="groove")
email_username_insert_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_username_insert_entry.insert(0, "panosfps1993@gmail.com")

password_insert_entry = Entry(width=31, bd=3, relief="groove", show="*")
password_insert_entry.grid(row=3, column=1, pady=5)

# BUTTONS

search_button = Button(text="Search", relief="groove",width=14, command=search, bg="yellow")
search_button.grid(row=1, column=2, pady=5)

generate_pass_button = Button(text="Generate Password", relief="groove", command=random_password_generate, bg="yellow")
generate_pass_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=43, relief="groove", command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
