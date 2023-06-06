#!python3

# A basic canvas drawing using some geometric shapes

import tkinter as tk
import random
import time

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


def randomColor():
    #converts rgb values to hex color code
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# create 10 random objects on the canvas
# create an empty list
# iterate 10 times to populate list
#   create random coordinates
#   add a rectangle to the list of objects by appending it to the list
objects = []
colors = ['blue','green','red','yellow','white','black','#888888',"#ffff77"]
for i in range(10):
    x1 = random.randint(0,500)
    y1 = random.randint(0,400)
    x2 = x1 + random.randint(20,40)
    y2 = y1 + random.randint(20,40)
    objects.append( c.create_rectangle(x1,y1,x2,y2,fill=randomColor() ) )



w.mainloop()