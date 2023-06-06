#!python3

# Adding walls to the canvas using coordinates to create a grid
# in this example, all blocks are 20x20 pixels
# See example2b.py to see how we could use different size walls

import tkinter as tk
import random
import time

#settings
wallSize = 40 
w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


#Placing blocks by coordinates assuming all blacks are the same size and wallSize x wallSize pixels
map = [ (0,1),(0,2),(0,3), (3,4) , (5,10) , (9,0) , (10,3)]
walls = []
for i in map:
    x1 = i[0] * wallSize + 5
    y1 = i[1] * wallSize + 5
    x2 = x1 + wallSize
    y2 = y1 + wallSize
    walls.append( c.create_rectangle(x1,y1,x2,y2,fill="#aa00aa"))




w.mainloop()