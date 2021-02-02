from tkinter import *
from platform_object import Platform
import time
import random
import winsound

class Player:
    def __init__(self, canvas, color, platform = None, platform2= None, platform3= None, platform4= None, platform5= None, platform6 = None, platform7= None, x1=42, y1=380, x2=67, y2=405, jump_time=0, jump_count=0):
        self.canvas = canvas
        self.platform = platform
        self.platform2 = platform2
        self.platform3 = platform3
        self.platform4 = platform4
        self.platform5 = platform5
        self.platform6 = platform6
        self.platform7 = platform7
        self.color = color
        self.id = canvas.create_oval(x1, y1, x2, y2, fill=self.color)
##        print(self.platform.id)
##        print(self.platform2.id)
##        self.canvas.move(self.id, 200, 300)
        self.jump_time = jump_time
        self.jump_count = jump_count
        self.x = 0
        self.y = 0
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-w>", self.turn_up)
        self.canvas.bind_all("<KeyPress-a>", self.turn_left)
        self.canvas.bind_all("<KeyPress-d>", self.turn_right)
        self.canvas.bind_all("<KeyPress-f>", self.tag)
    def draw(self):
        self.jump_time += 1
        self.canvas.move(self.id, self.x, self.y)
##        if self.check(self.platform6.id) == True or self.check(self.platform7.id) == True:
##            platform6_coords = self.platform6.canvas.coords(self.platform6.id)
##            platform7_coords = self.platform7.canvas.coords(self.platform7.id)
##            pos = self.canvas.coords(self.id)
##            if self.x == 2 and platform6_coords[0] == pos[2]:
##                print('hi')
##                self.x = 0
##            elif self.x == 2 and platform7_coords[0] == pos[2]:
##                self.x = 0
##            elif self.x == -2 and platform6_coords[2] == pos[0]:
##                self.x = 0
##            elif self.x == -2 and platform7_coords[2] == pos[0]:
##                self.x = 0
        
        pos = self.canvas.coords(self.id)
        if self.check(self.platform6.id) == True or self.check(self.platform7.id) == True:
            self.y = 0
            self.x = 0
            self.jump_count = 0
        
        if self.y ==0 and self.check(self.platform.id) == False or self.y ==0 and self.check(self.platform2.id) == True or self.y ==0 and self.check(self.platform3.id) == True or self.y ==0 and self.check(self.platform4.id) == True or self.y ==0 and self.check(self.platform5.id) == True or self.y ==0 and self.check(self.platform6.id) == True or self.y ==0 and self.check(self.platform7.id) == True:
##            if pos[3] >= self.canvas_height:
##                self.y = 0
##            else:
                self.y = 4
        if self.check(self.platform.id) == True or self.check(self.platform2.id) == True or self.check(self.platform3.id) == True or self.check(self.platform4.id) == True or self.check(self.platform5.id) == True or self.check(self.platform6.id)== True or self.check(self.platform7.id)== True:
            self.jump_count = 0
            self.y = 0
        if self.jump_time == 20:
            self.y = 4
        if pos[1] == 0:
            self.y = 2
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        
        if pos[3] >= self.canvas_height:
            self.jump_count = 0
            self.jump_time = 0
            self.y = 0
        
        
    def turn_left(self, why):
        pos = self.canvas.coords(self.id)
        if self.y != -4 and pos[1] <= 0:
            self.y = 4
        elif self.x == -2:
            self.x = 0
        else:
            self.x = -2
##        self.y = 0
    def turn_right(self, why):
        pos = self.canvas.coords(self.id)
        if self.y != -4 and pos[1] <= 0:#or self.y ==0 and self.check(self.platform) == False:
            self.y = 4
        elif self.x==2:
            self.x = 0
        else:
            self.x = 2
##        self.y = 0
    def turn_up(self, why):
        if self.jump_count ==0:
##            winsound.PlaySound('jump01.mp4', winsound.SND_ASYNC| winsound.SND_NOSTOP)
            self.y = -4
            self.jump_time = 0
            self.jump_count = 1

    
##    def turn_down(self, why):
##        self.y = 2

    def tag(self, why):
        print(self.canvas.coords(self.id))

    def check (self, platform):
        plat_coords = self.platform.canvas.coords(platform)
        player_coords = self. canvas.coords(self.id)
        if player_coords[2] >= plat_coords[0] and player_coords[0] <= plat_coords[2]:
            if player_coords[3] >= plat_coords[1] and player_coords[3] <= plat_coords[3]:
                return True
        return False
    def check_wall (self, wall):
        plat_coords = self.wall.canvas.coords(wall)
        player_coords = self. canvas.coords(self.id)
        if player_coords[2] >= plat_coords[0] and player_coords[0] <= plat_coords[2]:
            if player_coords[3] >= plat_coords[1] and player_coords[3] <= plat_coords[3]:
                return True
        return False
    



