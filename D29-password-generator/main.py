from tkinter import *
from tkinter import messagebox  # messagebox is a module, not a class (not in the *)
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = web_entry.get()
    email = mail_entry.get()
    passw = pass_entry.get()

    if len(website) == 0 or len(passw) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email} \nPassword: {passw} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {passw}\n")
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg="white")

# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web = Label(text="Website:", bg="white")
web.grid(column=0, row=1)
mail = Label(text="Email/Username:", bg="white")
mail.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=52)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()  # get the cursor to the web entry
mail_entry = Entry(width=52)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(END, "evelynt@mail.com")  # END means the last position
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

# Buttons
pass_button = Button(text="Generate Password", command=pass_generate, bg="white", highlightthickness=0)
pass_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_pass, width=44, bg="white", highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
