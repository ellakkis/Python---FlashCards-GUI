from tkinter import *
import pandas
import random

# -------------CONSTANTS------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 30, "italic")
FONT_WORD = ("Ariel", 40, "bold")
FONT_FLIP = ("Ariel", 15, "underline")

# -------------GLOBAL VARIABLES------------------------#
current_word = ""

# ---------------READ DATA----------------------------#
try:
  words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  words = pandas.read_csv("data/french_words.csv")
finally:
  words_dict = words.to_dict(orient="records")


# ---------------FUNCTIONS----------------------------#  
def update_data():
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

  
def right_answer():
  words_dict.remove(current_word)
  next_card()
  lbl_flip.place(x=580, y=450)
  update_data()
  
def wrong_answer():
  next_card()
  lbl_flip.place(x=580, y=450)


def next_card():
  global current_word
  current_word = random.choice(words_dict)
  canvas.itemconfigure(card, image=card_front)
  canvas.itemconfigure(lbl_title, text="French", fill="black")
  canvas.itemconfigure(lbl_word, text=current_word['French'], fill="black")
  
def flip_card():
  canvas.itemconfigure(card, image=card_back)
  canvas.itemconfigure(lbl_title, text="English", fill="white")
  canvas.itemconfigure(lbl_word, text=current_word['English'], fill="white")
  lbl_flip.place(x=980, y=950)  
# ----------------GUI-----------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# images
canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 270, image=card_front)
lbl_title = canvas.create_text(400, 120, text="title", font=FONT_TITLE)
lbl_word = canvas.create_text(400, 250, text="Word", font=FONT_WORD)
lbl_flip = Label(canvas, text="Flip", font=FONT_FLIP, fg="blue", bg="white")
lbl_flip.bind("<Button-1>", lambda e: flip_card())
lbl_flip.place(x=580, y=450)
canvas.grid(columnspan=2, column=0, row=0)

# buttons
# btn_flipcard = Button(text="Flip", command=flip_card)
# btn_right.grid(column=1, row=1)

right = PhotoImage(file="images/right.png")
btn_right = Button(image=right, highlightthickness=0, command=right_answer)
btn_right.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong, highlightthickness=0, command=wrong_answer)
btn_wrong.grid(column=0, row=1)


next_card()


window.mainloop()
