import tkinter as tk
import random
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
CELL_SIZE = 20
SQUARE_SIZE = 15
MAP_FILENAME = "map1.txt"
MOVE_INCREMENT = 20


def readmap(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]


def canvassize(map_data):
    height = len(map_data) * CELL_SIZE
    width = len(map_data[0]) * CELL_SIZE
    return width, height


def drawmap(canvas, mapdata):
    for y in range(len(mapdata)):
        for x in range(len(mapdata[y])):
            if mapdata[y][x] == "*":
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill="black")
            else:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill="white")


def movesquare(event):
    if event.keysym == "Up":
        move(0, -MOVE_INCREMENT)
    elif event.keysym == "Down":
        move(0, MOVE_INCREMENT)
    elif event.keysym == "Left":
        move(-MOVE_INCREMENT, 0)
    elif event.keysym == "Right":
        move(MOVE_INCREMENT, 0)


def move(dx, dy):
    x1, y1, x2, y2 = c.coords(square)


    new_x1 = x1 + dx
    new_y1 = y1 + dy
    new_x2 = x2 + dx
    new_y2 = y2 + dy


    if isvalidmove(new_x1, new_y1, new_x2, new_y2):
        c.move(square, dx, dy)


def isvalidmove(x1, y1, x2, y2):
    overlapping_items = c.find_overlapping(x1, y1, x2, y2)
    for item in overlapping_items:
        if item != square and c.itemcget(item, "fill") == "black":
            return False
    return True


def randomwhitetile(mapdata):
    white_tiles = []
    for y in range(len(mapdata)):
        for x in range(len(mapdata[y])):
            if mapdata[y][x] == " ":
                white_tiles.append((x, y))
    return random.choice(white_tiles)


mapdata = readmap(MAP_FILENAME)
canvas_width, canvas_height = canvassize(mapdata)


w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost', True)


c = tk.Canvas(w, height=canvas_height, width=canvas_width, bg="#ffdddd")
c.pack()


drawmap(c, mapdata)


start_x, start_y = randomwhitetile(mapdata)
start_x = start_x * CELL_SIZE + (CELL_SIZE - SQUARE_SIZE) // 2
start_y = start_y * CELL_SIZE + (CELL_SIZE - SQUARE_SIZE) // 2
square = c.create_rectangle(start_x, start_y, start_x + SQUARE_SIZE, start_y + SQUARE_SIZE, fill="blue")


w.bind("<KeyPress>", movesquare)
w.focus_set()


w.mainloop()

