import time
from tkinter import *
from time import sleep
from datetime import datetime
from word_generator import generate_words, some_web

COUNTDOWN = 10
TIME = 0
HIGH_CPM = 0
# Creating a new window and configurations
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=500)


# Def start timer
def start_typing():
    reset()
    # Todo: generate random word here
    text.insert(END, f"{some_web}")
    sleep(2)

    # Start taking input
    window.after(500, count_down(COUNTDOWN))

def reset():
    global TIME
    #reset time
    TIME = 0
    # clear the text
    text.delete("1.0", END)
    # clear and open entry
    user_entry.config(state="normal")
    user_entry.delete(0, END)
    user_entry.focus()
    # clear notification
    notice.config(text="")


# Make countdown
def count_down(count):
    global TIME
    count_text = count
    if count < 10:
        count_text = f"0{count}"
    time_text.config(text=f"Your time: {count_text} sec")
    if count > 0:
        TIME += 1
        timer = window.after(1000, count_down, count - 1)
    else:
        #disable entry
        user_entry.config(state="disabled")
        # Calculate cpm
        total_char = len(user_entry.get())
        total_word = len(user_entry.get().split())
        cpm = int(total_char / TIME * 60)
        wpm = int(total_word / TIME * 60)
        cpm_score.config(text=f"Your typing speed is {cpm} cpm or {wpm} wpm")
        highest_score(cpm)

def on_key_release(event):
    typed_text = user_entry.get()
    compare_text(typed_text)


#TODO: Compare the user input to the word
def compare_text(typed_text):
    text_to_type = text.get("1.0", END)
    correct_text = text_to_type[:len(typed_text)]
    incorrect_text = typed_text[len(correct_text):]
    if typed_text == correct_text:
        user_entry.config(bg="white")
        text.delete("1.0", END)
        text.insert(END, f"{typed_text}{text_to_type[len(typed_text):]}")
    else:
        user_entry.config(bg="pink")


#Put highest score on
def highest_score(cpm):
    global HIGH_CPM
    if cpm > HIGH_CPM:
        HIGH_CPM = cpm
        current_time = datetime.now().strftime("%D %H:%M")
        high_cpm.config(text=f"Your highest speed is {HIGH_CPM} cpm at {current_time}")
        notice.config(text="New High Score!")


# Make Title label
Title = Label(text="Typing Speed Test", font=("Helvetica", 16, "bold"), fg="blue")
Title.pack()

# Make subtitle label
Subtitle = Label(text="Please click button below to start!", font=("Helvetica", 12), pady=10)
Subtitle.pack()

# create button
start_button = Button(text="Start!", command=start_typing)
start_button.pack()

# Make text for countdown:
time_text = Label(text=f"The countdown is {COUNTDOWN} seconds.", pady=10)
time_text.pack()

# Show generated words
text = Text(height=12, width=40, font=("helvetica", 11), wrap=WORD)
text.pack()

# Make entry
user_entry = Entry(width=30)
# Add some text to begin with
user_entry.focus()
user_entry.pack()
user_entry.bind("<KeyRelease>", on_key_release)

# Create cpm score
cpm_score = Label(font=("Helvetica", 14, "italic"), pady=10)
cpm_score.pack()

# Notification
notice = Label(font=("Helvetica", 12, "bold"), fg="blue")
notice.pack()

# Create high cpm score
high_cpm = Label(font=("Helvetica", 12))
high_cpm.pack()

window.mainloop()
