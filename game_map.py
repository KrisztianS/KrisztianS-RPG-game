from tkinter import *
root = Tk()

canvas = Canvas(root, width='720', height='720')

filename = PhotoImage(file = "floor_tile.png")

def draw_map():
    x = 0
    y = 0

    for row in range(10):
        x = 0
        for tile in range(10):
            canvas.create_image(x, y, anchor=NW, image=filename)
            x += 72
        y += 72
        
draw_map()
canvas.pack()
root.mainloop()