from random import randint
from tkinter import *
from entities import Hero, Entity, Skeleton
root = Tk()

class Game():

    def __init__(self):
        self.canvas = Canvas(root, width='720', height='720')
        self.floor_tile = PhotoImage(file= "floor_tile.png")
        self.wall_tile = PhotoImage(file= "wall_tile.png")
        self.hero_images = {"Up": PhotoImage(file= "hero-up.png"),
                            "Down": PhotoImage(file="hero-down.png"),
                            "Left": PhotoImage(file="hero-left.png"),
                            "Right": PhotoImage(file= "hero-right.png")}
        self.skeleton_image = PhotoImage(file= "skeleton.png")
        self.map_blueprint = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                              [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                              [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                              [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                              [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]]
                                                 
        self.draw_map()
        self.myhero = Hero(self.canvas)
        self.skeleton1 = Skeleton(self.canvas)
        self.draw_hero(0, 0)
        self.draw_skeleton(self.x, self.y)
        self.draw_skeleton(self.x, self.y)
        self.draw_skeleton(self.x, self.y)
        self.canvas.pack()

        root.bind("<KeyPress>", self.on_key_press)
        root.mainloop()

    def on_key_press(self, e):
        self.canvas.itemconfig(self.myhero.image_ID, image=self.hero_images[e.keysym])
        if ( e.keysym == 'Up' ):
             if self.myhero.y >= 1 and self.no_go_checker(self.myhero.x, self.myhero.y-1) == False:
                self.myhero.move(0,-1, "Up")
        elif( e.keysym == 'Down'):
             if self.myhero.y <= 8 and self.no_go_checker(self.myhero.x, self.myhero.y+1) == False:
                self.myhero.move(0,1, "Down")
        elif( e.keysym == 'Right' ):
            if self.myhero.x <= 8 and self.no_go_checker(self.myhero.x+1, self.myhero.y) == False:
                self.myhero.move(1,0, "Right")
        elif( e.keysym == 'Left' ):
             if self.myhero.x >= 1 and self.no_go_checker(self.myhero.x-1, self.myhero.y) == False:
                self.myhero.move(-1,0, "Left")
  
    #     else:
    #         return True
    def no_go_checker(self, x, y):
        return self.map_blueprint[y][x] == 1

    def draw_hero(self, x, y):
        self.x = x
        self.y = y
        self.myhero.image_ID = self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.hero_images["Down"])

    def draw_skeleton(self, rand_x, rand_y):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        if self.no_go_checker(self.x, self.y) == 0:
            self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.skeleton_image)
        else: self.draw_skeleton(self.x, self.y)
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