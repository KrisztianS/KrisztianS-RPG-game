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
        self.image_ID = None

    def move(self, dx, dy, direction):
        self.canvas.move(self.image_ID, dx*72, dy*72)
        self.x += dx
        self.y += dy
        
class Hero(Entity):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.image = "hero.png"
