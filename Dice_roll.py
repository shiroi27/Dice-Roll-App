from tkinter import *
import  random

# GUI SETup
root = Tk()
root.title(" DICE ROLL ")
root.geometry("700x450+200+200")
root.resizable(False,False)
root.config(bg="#41FFDF")

# Header Frame Box
frame = Frame(root, width=700, height=60, bg="#FDE757")
frame.place(x=0, y=0) 

# Header Title
title_bar = Label(root,text=" <~  DICE ROLL  ~> ",font=("Times New Roman", 30, "bold"),fg="#000000",bg="#FDE757")
title_bar.place(x=170, y=3) 

# Decorative Line
divider = Frame(root, bg="#FA8E00", height=7, width=1200)
divider.place(x= 0, y = 60)

# Dice 1
left_label = Label(root, text="", font=("Times New Roman", 200), bg="#41FFDF", fg="#000000")
left_label.place(x=150, y=67)

# Dice 2
right_label = Label(root, text="", font=("Times New Roman", 200), bg="#41FFDF", fg="#000000")
right_label.place(x=400, y=67)


def roll():
    dice = ['\u2680','\u2681' , '\u2683', '\u2684' , '\u2685']
    left_dice = random.choice(dice)
    right_dice = random.choice(dice)
    left_label.configure(text=left_dice)
    right_label.configure(text=right_dice)

# Button
button = Button(root,text=" LET'S ROLL . . . " , width = 15 , height=1 ,font=("Times new roman" , 20 , "bold"),
bg = "#FDE757" , fg="#000000", bd = 3 , command=roll)
button.place(x=227 , y =390)

root.mainloop()