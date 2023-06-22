import tkinter as tk
import random
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""

map_data = [
    "0000000000",
    "0661111223",
    "0661111233",
    "1111122333",
    "1111223334",
    "5551223344",
    "5511122223",
    "5551111222",
    "1155111222",
    "1111122222",
    "1111122266",
]

COLORS = {
    "0": "blue",  
    "1": "green",  
    "2": "green",  
    "3": "brown",  
    "4": "gray",  
    "5": "purple",
    "6": "red",    
}

TILE_SIZE = 30
MAP_WIDTH = len(map_data[0])
MAP_HEIGHT = len(map_data)
WINDOW_WIDTH = MAP_WIDTH * TILE_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * TILE_SIZE

window = tk.Tk()
window.title("task2")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()


for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        tile = map_data[y][x]
        color = COLORS.get(tile, "white")
        canvas.create_rectangle(
            x * TILE_SIZE,
            y * TILE_SIZE,
            (x + 1) * TILE_SIZE,
            (y + 1) * TILE_SIZE,
            fill=color
        )


validtiles = []
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        if map_data[y][x] == "1":
            validtiles.append((x, y))


startpos = random.choice(validtiles)
rect_x, rect_y = startpos


rectangle = canvas.create_rectangle(
    rect_x * TILE_SIZE,
    rect_y * TILE_SIZE,
    (rect_x + 1) * TILE_SIZE,
    (rect_y + 1) * TILE_SIZE,
    fill="orange"
)


def move_rectangle(event):
    global rect_x, rect_y


    prev_rect_x = rect_x
    prev_rect_y = rect_y


    if event.keysym == "Down" and rect_y < MAP_HEIGHT - 1 and map_data[rect_y + 1][rect_x] == "1":
        rect_y += 1
    elif event.keysym == "Left" and rect_x > 0 and map_data[rect_y][rect_x - 1] == "1":
        rect_x -= 1
    elif event.keysym == "Right" and rect_x < MAP_WIDTH - 1 and map_data[rect_y][rect_x + 1] == "1":
        rect_x += 1
    elif event.keysym == "Up" and rect_y > 0 and map_data[rect_y - 1][rect_x] == "1":
        rect_y -= 1


    canvas.coords(
        rectangle,
        rect_x * TILE_SIZE,
        rect_y * TILE_SIZE,
        (rect_x + 1) * TILE_SIZE,
        (rect_y + 1) * TILE_SIZE
    )

window.bind("<Up>", move_rectangle)
window.bind("<Down>", move_rectangle)
window.bind("<Left>", move_rectangle)
window.bind("<Right>", move_rectangle)

window.mainloop()

