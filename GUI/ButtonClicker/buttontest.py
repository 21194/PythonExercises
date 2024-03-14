from tkinter import *

count=0

def btn_click():
    global count 
    count += 1
    print("Button Clicked ", count , " times")


window = Tk ()


btn = Button(window, text="Click me!",
command=btn_click)

btn.pack()


window.mainloop()