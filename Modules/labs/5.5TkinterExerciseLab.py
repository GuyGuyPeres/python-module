import tkinter as tk
from tkinter import *
from tkinter import ttk
import time


def change_text():
    print("i am here")
    Message_text.set("I AM THE CAPTAIN NOW")
    

def print_to_terminal():
    text_var=entry1_text.get()
    print(f"the text is: {text_var}")

root = tk.Tk()
root.geometry('900x400+400+350')
root.title("Guy's Testing This Now")
# root.resizable(False, False) --> locks app dimenstions, the user cant control


label1 = tk.Label(root, text="Guy Peres Was Here")
label2 = tk.Label(root, text="Moshe Cohen Was Here")
label3 = tk.Label(root, text="SuperMan Was Here")
label4 = tk.Label(root, text="I placed this with place()")
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=0, column=1, padx=10, pady=10)
label3.grid(row=0, column=2, padx=10, pady=10)
label4.place(x=50, y=100)

button1 = tk.Button(root, text="close this window!", activebackground="red", width=25, command=root.destroy)
button2 = tk.Button(root, text="change text", activebackground="blue", width=25, command=change_text)
button3 = tk.Button(root, text="print entry to terminal", activebackground="green", width=25, command=print_to_terminal)
button1.place(x=70, y=200)
button2.place(x=70, y=230)
button3.place(x=70, y=260)

Message_text = tk.StringVar()
Message_text.set("first simple text")
messageBox = tk.Message(root, text="simple text",textvariable=Message_text)
messageBox.config(bg='lightgreen')
messageBox.place(relx=1.0, rely=0.0, anchor="ne", width="200")


tk.Label(root, text="enter a name").place(relx=3.5, rely=3.0, anchor="s")


entry1_text=StringVar()
entry1 = tk.Entry(root, textvariable=entry1_text)
entry1.place(relx=1.0, rely=0.0, anchor="ne", width="200")


root.mainloop()