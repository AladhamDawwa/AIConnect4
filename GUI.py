from tkinter import *
from tkinter import messagebox
from game import AI


def play(difficulty, algorithm):
    if difficulty == "Beginner":
        difficultyNumber = 1
    elif difficulty == "Amateur":
        difficultyNumber = 2
    elif difficulty == "Professional":
        difficultyNumber = 3
    elif difficulty == "World Class":
        difficultyNumber = 4
    else:
        difficultyNumber = 5

    AI(difficultyNumber, algorithm)
    print("Difficulty:", difficulty)
    print("Algorithm:", algorithm)


def btn_clicked():
    difficulty = difficulty_var.get()
    algorithm = algorithm_var.get()

    if difficulty and algorithm:
        play(difficulty, algorithm)
    else:
        messagebox.showwarning("Error", "Please select values from both ComboBoxes.")


window = Tk()
window.geometry("650x400")
window.configure(bg="#ffffff")
window.title("AI Connect 4")

canvas = Canvas(window, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
bg = PhotoImage(file="background.png")
canvas.create_image(500.0, 300.0, image=bg)

Label(window, text="Difficulty:").place(x=130, y=150)

difficulty_var = StringVar(window)
OptionMenu(window, difficulty_var, "Beginner", "Amateur", "Professional", "World Class", " Legendary") \
    .place(x=205, y=150)

Label(window, text="Algorithm:").place(x=350, y=150)

algorithm_var = StringVar(window)
OptionMenu(window, algorithm_var, "Minimax", "Alpha-Beta pruning").place(x=460, y=150)

img = PhotoImage(file="img0.png")
Button(image=img, borderwidth=-1, highlightthickness=-1, command=btn_clicked, relief="flat")\
    .place(x=250, y=250, width=173, height=53)

window.resizable(False, False)
window.mainloop()
