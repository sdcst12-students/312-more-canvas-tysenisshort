#!python3

# Adding an image instead of using canvas basic shapes

import tkinter as tk
import random
w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


r = c.create_rectangle(190,190,210,210,fill="#0000ff")

# Creates an image and places it with its center at 200,200
wimg = tk.PhotoImage(file="assets/charmander.png")
img = c.create_image(200,200,image=wimg)

# Note that the rectangle r is behind the image.  You can bring it in front
# untag the line 23 command
#c.tag_raise(r)

# We can also add walls using images and add them to a list of walls
walls  =[]
wallImg = tk.PhotoImage(file="assets/win.png")
for i in range(30):
    x = random.randint(0,25)*20
    y = random.randint(0,20)*20
    walls.append( c.create_image(x,y,image=wallImg))

c.tag_raise(img)






w.mainloop()