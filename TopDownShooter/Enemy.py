from tkinter import *
from Sprite import Sprite
import math

class Enemy(Sprite):
    def __init__(self, game, canvas, target):
        self.game = game
        self.canvas = game.canvas
        self.target = target
        self.speed = 5
        self.x = 550
        self.y = 150
        self.image = PhotoImage(file="Enemy.gif")
##        self.tk = Tk()
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor = 'nw')
    def coords(self):
        return self.canvas.coords(self.id)
    def move(self):
        selfx, selfy = (self.coords()[0]+30/2, (self.coords()[1]+30/2))
        targetx, targety = self.target.coords()
        movex = (targetx-selfx)
        movey = (targety-selfy)
        theta = math.atan2(movey, movex) ## angle between player and mouse position, relative to positive x
        self.x = self.speed*math.cos(theta)
        self.y = self.speed*math.sin(theta)
        self.canvas.move(self.id, self.x, self.y)
        for attack in self.game.attacks:
            attack_coords = attack.coords()
            player_coords = self.canvas.coords(self.id)
            if (player_coords[0]+30) >= attack_coords[0] and player_coords[0] <= (attack_coords[0]+10):
                if (player_coords[1]+30) >= attack_coords[1] and player_coords[1]+30 <= (attack_coords[1]+30):
                    self.canvas.delete(self.id)
                    attack.canvas.delete(attack.id)
                    self.game.attacks.remove(attack)
                    self.game.sprites.remove(self)
                    break

