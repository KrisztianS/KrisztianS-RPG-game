from tkinter import *

class Entity():
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.hp = 100
        self.sp = 20
        self.dp = 20
        self.image = ""
        
    def draw(self, x, y):
        self.x = x
        self.y = y
        self.asset = PhotoImage(file = self.image)
        self.image_ID = self.canvas.create_image(self.x * 72, self.y * 72, anchor=NW, image=self.asset)

class Hero(Entity):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.image = "hero.png"
