from tkinter import *
root = Tk()

canvas = Canvas(root, width='600', height='600')

filename = PhotoImage(file = "floor_tile.png")
image = canvas.create_image(0, 0, anchor=NW, image=filename)

canvas.pack()





root.mainloop()