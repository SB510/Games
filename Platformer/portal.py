from Player import Player
class Portal:
    def __init__(self, player, x1, y1, x2, y2, p2x1, p2y1, p2x2, p2y2, canvas, color):
        self.canvas = canvas
        self.color = color
        self.player = player
        self.id = canvas.create_oval(x1, y1, x2, y2, fill=self.color)
        self.id2 = canvas.create_oval(p2x1, p2y1, p2x2, p2y2, fill=self.color)
##        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
    def draw (self):
        if self.check() == True:
            return True
    def check (self):
        portal_coords = self.canvas.coords(self.id)
        player_coords = self.player.canvas.coords(self.player.id)
        if player_coords[2] >= portal_coords[0] and player_coords[0] <= portal_coords[2]:
            if player_coords[3] >= portal_coords[1] and player_coords[3] <= portal_coords[3]:
                return True
        return False
    
