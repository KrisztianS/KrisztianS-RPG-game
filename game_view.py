from tkinter import *
from entities import Hero
root = Tk()

class Map():

    def __init__(self):
        self.canvas = Canvas(root, width='720', height='720')

        self.floor_tile = PhotoImage(file = "floor_tile.png")
        self.wall_tile = PhotoImage(file = "wall_tile.png")

        self.map_blueprint = [
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
                
    def draw_map(self):
        self.x = 0
        self.y = 0

        for row in range(len(self.map_blueprint)):
            self.x = 0
            for tile in range(len(self.map_blueprint[0])):
                if self.map_blueprint[row][tile] == 1:
                    self.canvas.create_image(self.x, self.y, anchor=NW, image=self.wall_tile)
                else:
                    self.canvas.create_image(self.x, self.y, anchor=NW, image=self.floor_tile)
                self.x += 72
            self.y += 72


mymap = Map()
myhero = Hero(canvas)
mymap.draw_map()
myhero.draw(0, 0)
canvas.pack()
root.mainloop()