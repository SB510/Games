from tkinter import *
from Enemy import Enemy
import time


class Spawner:
    def __init__(self, game, p1,x, y):
        self.game = game
        self.p1 = p1
        self.time = time.time()
        self.cooldown = 5
        self.image = PhotoImage(file = "Spawner.gif")
        self.id = self.game.canvas.create_image(x, y, image = self.image, anchor = 'nw')
    def coords(self):
        return self.game.canvas.coords(self.id)
    def move(self):
        if time.time() - self.time >= self.cooldown:
            enemy1 = Enemy(self.game, self.game.canvas, self.p1)
            self.game.sprites.append(enemy1)
            if self.cooldown != 1:
                self.cooldown -= 0.5
            self.time = time.time()
