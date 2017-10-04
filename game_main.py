from tkinter import *
from entities import Hero, Entity
root = Tk()

class Game():

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
        self.draw_map()
        self.myhero = Hero(self.canvas)
        self.myhero.draw(0, 0)
        self.canvas.pack()

        root.bind("<KeyPress>", self.on_key_press)
        root.mainloop()

    def on_key_press(self, e):
        if ( e.keysym == 'Up' ):
            self.myhero.move(0,-1)
        elif( e.keysym == 'Down' ):
            self.myhero.move(0,1)
        elif( e.keysym == 'Right' ):
            self.myhero.move(1,0)
        elif( e.keysym == 'Left' ):
            self.myhero.move(-1,0)

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

mymap = Game()