from tkinter import *



def btn_click_red():
     print("Red now")
     window.configure(bg='red')
    
def btn_click_blue():
     print("Blue now")
     window.configure(bg='blue')

def btn_click_white():
     print("White now")
     window.configure(bg='white')

window = Tk ()
window.geometry("500x500")

btn = Button(window, text="Red",
command=btn_click_red)
btn.pack()


btn2 = Button(window, text="Blue",
command=btn_click_blue)
btn2.pack()


btn3 = Button(window, text="White", 
command=btn_click_white)
btn3.pack()




window.mainloop()
