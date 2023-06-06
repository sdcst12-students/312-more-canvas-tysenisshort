#!python3

# Adding an image that is constantly changing using the tk.after() command

import tkinter as tk
tile = 0

def update():
    # alternates the tile between state 0 and 1 using modulus
    # depending on the state, the image contents are changed and 
    # a new timer is set to change again in 200 milliseconds
    global tile
    ig = None
    tile +=1
    tile = tile%2
    if tile: 
        ig = img
    else: 
        ig = img2

    c.itemconfig(wim,image=ig)
    w.after(200,update)

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("500x300")

c = tk.Canvas(w,width=475,height=280)
c.pack()
img = tk.PhotoImage(file="assets/win.png")
img2 = tk.PhotoImage(file="assets/winb.png")
wim = c.create_image(200,100,image=img)

w.after(200,update)


w.mainloop()