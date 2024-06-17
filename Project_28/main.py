import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def click_reset():
    global reps
    reps = 1
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def click_start():
    global reps
    work_timer = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps in {1, 3, 5, 7}:
        count_down(work_timer)
        timer_label.config(text="Work time", fg=GREEN)
    elif reps in {2, 4, 6}:
        count_down(short_break)
        timer_label.config(text="Rest time", fg=PINK)
    elif reps == 8:
        count_down(long_break)
        timer_label.config(text="Rest time", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        timer = window.after(1000, count_down, count-1)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count == 0:
        reps += 1
        mark = ""
        work_sessions = int(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)
        click_start()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = tkinter.Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=click_start)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=click_reset)
reset_button.grid(column=2, row=2)


window.mainloop()
