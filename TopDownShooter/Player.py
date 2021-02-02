from tkinter import *
from Sprite import Sprite
from bullet import Attack
import math
class Player(Sprite):
    def __init__(self, game, canvas):
        Sprite.__init__(self, game)
        self.speed = 5
        self.canvas = canvas
        self.game = game
        self.image = PhotoImage(file="Player.gif")
        self.x1 = 100
        self.y1 = 100
        self.x = 0
        self.y = 0
        self.cooldown = 10
        self.id = self.game.canvas.create_image(self.x1, self.y1, image=self.image, anchor='nw')
        self.game.canvas.bind_all('<KeyPress-space>', self.shoot)
        self.game.canvas.bind_all('<KeyPress-w>', self.up)
        self.game.canvas.bind_all('<KeyPress-a>', self.left)
        self.game.canvas.bind_all('<KeyPress-s>', self.down)
        self.game.canvas.bind_all('<KeyPress-d>', self.right)
    def up(self, evt):
        self.x = 0
        if self.y == -5:
            self.y = 0
        else:
            self.y = -5
    def down(self, evt):
        self.x = 0
        if self.y == 5:
            self.y = 0
        else:
            self.y = 5
    def left(self, evt):
        self.y = 0
        if self.x == -5:
            self.x = 0
        else:
            self.x = -5
    def right(self, evt):
        self.y = 0
        if self.x == 5:
            self.x = 0
        else:
            self.x = 5
    def shoot(self, evt):
        if self.cooldown >= 10:
            bullet = Attack(self.game, self.coords()[0], self.coords()[1], self.canvas)
            self.game.attacks.append(bullet)
            self.cooldown = 0
    def coords(self):
        return self.canvas.coords(self.id)
    def move(self):
        self.cooldown += 1
        self.canvas.move(self.id, self.x, self.y)
        for sprite in self.game.sprites:
            if sprite != self:
                sprite_coords = sprite.coords()
                player_coords = self.canvas.coords(self.id)
                if (player_coords[0]+30) >= sprite_coords[0] and player_coords[0] <= (sprite_coords[0]+30):
                    if (player_coords[1]+30) >= sprite_coords[1] and player_coords[1]+30 <= (sprite_coords[1]+30):
                        self.canvas.delete(self.id)
                        sprite.canvas.delete(sprite.id)
                        sprite.game.sprites.remove(sprite)
                        self.game.sprites.remove(self)
                        break




