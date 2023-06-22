#!python3


# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!


import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
window.title("Big Shrek")
originalimage = Image.open("Shraq.png")
flippedimage = originalimage.transpose(Image.FLIP_LEFT_RIGHT)


originalphoto = ImageTk.PhotoImage(originalimage)
flippedphoto = ImageTk.PhotoImage(flippedimage)


canvas = tk.Canvas(window, width=originalimage.width, height=originalimage.height)
canvas.pack()

imageobject = canvas.create_image(0, 0, anchor=tk.NW, image=originalphoto)

def animate():
    currentimage = canvas.itemcget(imageobject, "image")
   
    if currentimage == str(originalphoto):
        canvas.itemconfigure(imageobject, image=flippedphoto)
    else:
        canvas.itemconfigure(imageobject, image=originalphoto)
   
    window.after(500, animate)


animate()


window.mainloop()