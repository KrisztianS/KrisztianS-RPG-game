from tkinter import *
root = Tk()

canvas = Canvas(root, width='720', height='720')

floor_tile = PhotoImage(file = "floor_tile.png")
wall_tile = PhotoImage(file = "wall_tile.png")

map_blueprint = [
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
                                             ]
                
def draw_map():
    x = 0
    y = 0

    for row in range(len(map_blueprint)):
        x = 0
        for tile in range(len(map_blueprint[0])):
            if map_blueprint[row][tile] == 1:
                canvas.create_image(x, y, anchor=NW, image=wall_tile)
            else:
                canvas.create_image(x, y, anchor=NW, image=floor_tile)
            x += 72
        y += 72

draw_map()
canvas.pack()
root.mainloop()