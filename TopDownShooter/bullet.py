from tkinter import *
import math
class Attack():
    def __init__(self, game, x1, y1, canvas):
        self.game = game
        self.tk = Tk()
##        self.x = 0
##        self.y = 0
        self.speed = 10
        self.change = False
        self.canvas = canvas
        self.image = PhotoImage(file="Bullet.gif")
        self.id = self.game.canvas.create_image(x1, y1, image=self.image, anchor='nw')
    def coords(self):
        return self.canvas.coords(self.id)
    def mouse_coords(self):
        rawMouseX, rawMouseY =   self.tk.winfo_pointerx(), self.tk.winfo_pointery()
        self.mousecoords = rawMouseX  - self.tk.winfo_rootx(), rawMouseY - self.tk.winfo_rooty()
        return self.mousecoords   
    def move(self):
        if self.change == False:
            self.change = True
            selfx, selfy = (self.coords()[0]+15/2, (self.coords()[1]+15/2))
            mousex, mousey = self.mouse_coords()
            movex = (mousex-selfx)
            movey = (mousey-selfy)
            theta = math.atan2(movey, movex) ## angle between player and mouse position, relative to positive x
            self.x = self.speed*math.cos(theta)
            self.y = self.speed*math.sin(theta)
        self.canvas.move(self.id, self.x, self.y)
##            print(self.x, self.y)
##            if self.coords[0] <= 0 or self.coords[0]+30 >= 1000:
##                self.canvas.delete(self.id)
##                self.game.sprites.remove(self)
##            elif self.coords[1] <= 0 or self.coords[1]+30 >= 720:
##                self.canvas.delete(self.id)
##                self.game.sprites.remove(self)
                

