from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
dict_word = {}
rand_card = {}

# --------------------------- Flash card Functions ----------------------------- #
try:
    df_word = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df_original = pd.read_csv("./data/french_words.csv")
    dict_word = df_original.to_dict(orient="records")
else:
    dict_word = df_word.to_dict(orient="records")



def new_card():
    # show a random card
    global rand_card, flip_timer
    window.after_cancel(flip_timer)
    rand_card = random.choice(dict_word)
    canvas.itemconfig(word, text=rand_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(word, text=rand_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")


def right_answer():
    new_card()
    dict_word.remove(rand_card)
    df_to_learn = pd.DataFrame(dict_word)
    df_to_learn.to_csv("./data/words_to_learn.csv", index=False)


# --------------------------------- UI Interface --------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(403, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=right_answer, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=new_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)


new_card()

window.mainloop()
