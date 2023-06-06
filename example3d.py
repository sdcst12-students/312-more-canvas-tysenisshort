#!python3

# Pulling images from a tilesheet
# It helps to know the coordinates of your tile.

import tkinter as tk
from PIL import ImageTk,Image
import random
import time

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


#Placing blocks by coordinates assuming all blacks are the same size and 20x20 pixels
def getImage(x,y):
    img = Image.open("assets/tiles.png").convert("RGBA")
    xi = x*64
    yi = y*64
    img2 = img.crop([xi,yi,xi+64,yi+64])
    return ImageTk.PhotoImage(img2)


#img = tk.PhotoImage(file="assets/tiles.png")
map = [ (0,1) , (3,4) , (5,10) , (9,0) , (10,3)]
walls = []
img = [[]]
for i in range(4):
    for j in range(4):
        print(i,j)
        img.append(getImage(i,j+8))
        walls.append(c.create_image(i*64+32,j*64+32,image=img[-1]))





w.mainloop()