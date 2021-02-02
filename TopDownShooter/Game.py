from tkinter import *
import random
import time
from Player import Player
from Enemy import Enemy
from Spawner import Spawner
class Game:
    def __init__(self):
        #instantiate the game
        self.tk = Tk()
        self.tk.title("Place holder")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        #create the canvas for the game. all changes will be made to this canvas
        self.canvas = Canvas(self.tk, width=1000, height=720, \
                             highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 1000
        self.canvas_width = 1000
        self.bg = PhotoImage(file="Temp_back.gif")
        w = self.bg.width() 
        h = self.bg.height()
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.sprites = []
        self.attacks = []
    def mainloop(self):
        while 1:
            #run through sprites and attacks and call their move function
            for sprite in self.sprites:
                sprite.move()
            for attack in self.attacks:
                attack.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

g = Game()
p1 = Player(g, g.canvas)
g.sprites.append(p1)
spawner = Spawner(g, p1, 500, 100)
g.sprites.append(spawner)
#This updates the player and bullet each frame
g.mainloop()
