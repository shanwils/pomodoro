from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


def add_check():
    global marks
    marks += "✓"
    check_label.config(text=marks, font=(FONT_NAME, 20, "normal"))

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    global marks
    marks = ""
    check_label.config(text="")
    time_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN  * 60

    if reps % 2 == 0:
        print(f"working: {reps}")
        time_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    elif reps % 7 == 0:
        print(f"long break: {reps}")
        add_check()
        time_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 1:
        add_check()
        time_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        print(f"short break: {reps}")

    reps += 1
    if reps == 8:
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time_label = Label(text="Timer", font=(FONT_NAME, 40, "bold",))
time_label.config(bg=YELLOW, fg=GREEN)
time_label.grid(column=1, row=0)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
