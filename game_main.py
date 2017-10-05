from random import randint
from tkinter import *
from entities import Hero, Entity, Skeleton, Boss
root = Tk()

class Game():

    def __init__(self):
        self.canvas = Canvas(root, width='720', height='745')
        self.floor_tile = PhotoImage(file= "floor_tile.png")
        self.wall_tile = PhotoImage(file= "wall_tile.png")
        self.hero_images = {"Up": PhotoImage(file= "hero-up.png"),
                            "Down": PhotoImage(file="hero-down.png"),
                            "Left": PhotoImage(file="hero-left.png"),
                            "Right": PhotoImage(file= "hero-right.png"),
                            "space": PhotoImage(file="hero-down.png")}
        self.skeleton_image = PhotoImage(file= "skeleton.png")
        self.boss_image = PhotoImage(file= "boss.png")
        self.monster_coords = []
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
        self.boss = Boss(self.canvas)
        self.draw_hero(0, 0)
        self.draw_skeleton(self.x, self.y)
        self.draw_skeleton(self.x, self.y)
        self.draw_skeleton(self.x, self.y)
        self.draw_boss(self.x, self.y)
        self.hud = self.draw_HUD()
        self.canvas.pack()

        root.bind("<KeyPress>", self.on_key_press) #self.strike)
        root.mainloop()

    def on_key_press(self, e):
        self.canvas.itemconfig(self.myhero.image_ID, image=self.hero_images[e.keysym])
        if ( e.keysym == 'Up' ):
             if self.myhero.y >= 1 and not self.no_go_checker(self.myhero.x, self.myhero.y-1):
                self.myhero.move(0,-1, "Up")
        elif( e.keysym == 'Down'):
             if self.myhero.y <= 8 and not self.no_go_checker(self.myhero.x, self.myhero.y+1):
                self.myhero.move(0,1, "Down")
        elif( e.keysym == 'Right' ):
            if self.myhero.x <= 8 and not self.no_go_checker(self.myhero.x+1, self.myhero.y):
                self.myhero.move(1,0, "Right")
        elif( e.keysym == 'Left' ):
             if self.myhero.x >= 1 and not self.no_go_checker(self.myhero.x-1, self.myhero.y):
                self.myhero.move(-1,0, "Left")
        elif ( e.keysym  == "space" ) and self.are_on_same_tile:
            self.myhero.hp -= 1
            self.canvas.delete(self.hud)
            self.hud = self.draw_HUD()

    def no_go_checker(self, x, y):
        return self.map_blueprint[y][x] == 1

    def draw_hero(self, x, y):
        self.x = x
        self.y = y
        self.myhero.image_ID = self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.hero_images["Down"])

    def draw_skeleton(self, rand_x, rand_y):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        if self.no_go_checker(self.x, self.y) == 0 and [self.x , self.y] not in self.monster_coords:
            self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.skeleton_image)
            self.monster_coords.append([self.x, self.y])        
        else: self.draw_skeleton(self.x, self.y)
    
    def draw_boss(self, rand_x, rand_y):
        self.x = randint(4, 9)
        self.y = randint(4, 9)
        if self.no_go_checker(self.x, self.y) == 0 and [self.x , self.y] not in self.monster_coords:
            self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.boss_image)
            self.monster_coords.append([self.x, self.y]) 
        else: self.draw_boss(self.x, self.y)

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

    def draw_HUD(self):
        return self.canvas.create_text(10, 742, anchor=SW, text="Hero (Level" + str(self.myhero.level) + ")  HP: " + str(self.myhero.hp) + "  |  DP: " + str(self.myhero.dp) + "  |  SP: " + str(self.myhero.sp))

    def are_on_same_tile(self):
        return [self.myhero.x, self.myhero.y] in self.monster_coords

    # def strike(self):
    #     if self.are_on_same_tile == True and e.keysym == 'Space':
    #         self.myhero.hp -= 1
    # at the moment if hitting space anywhere decreases hero life

mymap = Game()