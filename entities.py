from tkinter import *
from random import randint

class Entity():
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.level = 1
        self.hp = 20
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
        self.hp = 20 + 3 * randint(1, 6)
        self.dp = 2* randint(1, 6)
        self.sp= 5 + randint(1, 6)

class Skeleton(Entity):

    def __init__(self, canvas):
        super().__init__(canvas)
        self.level = 1
        self.hp = self.level * 2 * randint(1, 6)
        self.dp = self.level / 2 * randint(1, 6)
        self.sp = self.level * randint(1, 6)
class Boss(Entity):
    
    def __init__(self, canvas):
        super().__init__(canvas)
        self.level = 1
        self.hp = self.level * 2 * randint(1, 6) + randint(1, 6)
        self.dp = self.level / 2 * randint(1, 6) + randint(1, 6) / 2
        self.sp = self.level * randint(1, 6) + self.level
