from tkinter import *
from os import system

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKS = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    global REPS
    global CHECKS
    REPS = 0
    CHECKS = ""
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():  # called in label_start command
    global REPS
    global CHECKS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)
        CHECKS += "✔"
        checkmarks.config(text=CHECKS)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif REPS == 8:
        title_label.config(text="Long Break", fg=GREEN)
        count_down(long_break_sec)
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):  # call in start_timer
    global TIMER
    min = (str(count // 60)).zfill(2)
    sec = (str(count % 60)).zfill(2)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmarks.grid(row=3, column=1)

window.mainloop()
