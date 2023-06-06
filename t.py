import tkinter as tk
from PIL import Image,ImageTk

#settings:
x = 3 # Sprite Sheet Row
y = 4 # Sprite Sheet Column

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("400x300")

c = tk.Canvas(width=380,height=280)
c.pack()
i=0
def getSprite(x,y):
    img = Image.open("assets/skt.png").convert("RGBA")
    xi = x*32
    yi = y*48
    img2 = img.crop([xi,yi,xi+32,yi+48])
    return ImageTk.PhotoImage(img2)    

def skelUpdate():
    global i

    i+=1
    i%=len(skel)
    c.itemconfig(img,image=skel[i])
    w.after(200,skelUpdate)
image = tk.PhotoImage(file="assets/skt.png")
# sk.png sprite sheet is 384 x 384 pixels, with 12 across and 8 down.
# each image is 32 x 48 pixels

skel=[]
for i in range(3):
    skel.append( getSprite(i+x*3,y))
skel.append( getSprite(1+x*3,y))
img = c.create_image(32,48,image=skel[0])
w.after(200,skelUpdate)


w.mainloop()