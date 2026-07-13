import pygame

class Map:
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        
        
        self.tile_size = 40

        self.grid_color = (40, 40, 40)

    def draw_grid(self, screen):
        
        for x in range(0, self.width, self.tile_size):
            pygame.draw.line(screen, self.grid_color, (x, 0), (x, self.height))
        
        for y in range(0, self.height, self.tile_size):
            pygame.draw.line(screen, self.grid_color, (0, y), (self.width, y))

    def keep_inside(self, player_rect):
       
        if player_rect.left < 0:
            player_rect.left = 0
            
        if player_rect.right > self.width:
            player_rect.right = self.width
            
        if player_rect.top < 0:
            player_rect.top = 0
            
        if player_rect.bottom > self.height:
            player_rect.bottom = self.height