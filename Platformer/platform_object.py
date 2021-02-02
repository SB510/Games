from tkinter import *
import time
import random
##tk = Tk()
##tk.title = ("Game")
##tk.wm_attributes("-topmost", 1)
##canvas = Canvas(tk, width=500, height=400)#, bd=0, highlightthickness
##canvas.pack()
##tk.update()

class Platform:
    def __init__(self, x1, y1, x2, y2, canvas, color, x=0, y=0, limit=0, count=0):
        self.canvas = canvas
        self.color = color
        self.limit = limit
        self.count = count
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        self.canvas.move(self.id, 200, 300)
        self.x = x
        self.y = y
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.count+= 1
        if self.count == self.limit:
            if self.x != 0:
                self.count = 0
                self.x = -1*self.x
            if self.y != 0:
                self.count = 0
                self.y = -1*self.y
        
        
