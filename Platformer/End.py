from tkinter import *

class End:
    def __init__(self,x1, y1, x2, y2, canvas, color, player):
        self.canvas = canvas
        self.color = color
        self.player = player
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
    def draw (self):
        if self.check() == True:
            return True
    def check (self):
        door_coords = self.canvas.coords(self.id)
        player_coords = self.player.canvas.coords(self.player.id)
        if player_coords[2] >= door_coords[0] and player_coords[0] <= door_coords[2]:
            if player_coords[3] >= door_coords[1] and player_coords[3] <= door_coords[3]:
                return True
        return False
