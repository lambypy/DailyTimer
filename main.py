from tkinter import *
from tkinter.ttk import *
import time
from datetime import datetime, timezone


root = Tk()
root.geometry("800x600")
root.resizable(True, True)
root.title("DailyTaskTimer")




def reset():
    pass


def start():

    for _ in range(5):
        cpp_progress_bar["value"] += 20
        root.update_idletasks()
        time.sleep(1)



# in mins




main_menu_label = Label(root, text="DailyTasks")
main_menu_label.place(relx=0.4, rely=0.1)



programming_label = Label(root, text="Programming Label:")
programming_label.place(relx=0.04, rely=0.2)



python_button = Button(root, text="Python")
python_button.place()

CPP_TIME = 30
cpp_label = Label(root, text="C++")
cpp_button_start = Button(root, text="Start", command=start, width=5)
cpp_button_pause = Button(root, text="Pause", width=5)
cpp_label.place(relx=0.04, rely=0.3)
cpp_button_start.place(relx=0.04, rely=0.35)
cpp_button_pause.place(relx=0.15, rely=0.35)
cpp_progress_bar = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
cpp_progress_bar.place(relx=0.04, rely=0.4)


functional_button_start = Button(root, text="OCaml/Haskell")
functional_button_pause = Button(root, text="Pause")

other_button = Button(root, text="Other language")



reading_programming = Button(root, text="Programming book/articles")



reset_button = Button()




root.mainloop()