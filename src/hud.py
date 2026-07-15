import pygame

class HUD:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

        self.font = pygame.font.SysFont("Arial", 24, bold=True)

        self.WHITE = (255, 255, 255)
        self.RED = (200, 30, 30)
        self.GREEN = (30, 200, 30)
        self.GRAY = (50, 50, 50)

        self.hp_bar_width = 200
        self.hp_bar_height = 20
        self.hp_bar_x = 20
        self.hp_bar_y = 20

    def draw(self):
        self.draw_health_bar()
        self.draw_score_and_ammo()

    def draw_health_bar(self):
        
        pygame.draw.rect(
            self.screen, 
            self.GRAY, 
            (self.hp_bar_x, self.hp_bar_y, self.hp_bar_width, self.hp_bar_height)
        )
        
        
        health_ratio = max(0, min(1, self.player.health / self.player.max_health))
        current_bar_width = int(self.hp_bar_width * health_ratio)
        
        
        bar_color = self.GREEN if health_ratio > 0.3 else self.RED
        
        
        pygame.draw.rect(
            self.screen, 
            bar_color, 
            (self.hp_bar_x, self.hp_bar_y, current_bar_width, self.hp_bar_height)
        )
        
        
        pygame.draw.rect(
            self.screen, 
            self.WHITE, 
            (self.hp_bar_x, self.hp_bar_y, self.hp_bar_width, self.hp_bar_height), 
            2
        )

    def draw_score_and_ammo(self):
        
        score_text = self.font.render(f"Score: {self.player.score}", True, self.WHITE)
        self.screen.blit(score_text, (20, 50))
        
        
        ammo_string = f"Ammo: {self.player.ammo} / {self.player.max_ammo}"
        ammo_text = self.font.render(ammo_string, True, self.WHITE)
        
        
        screen_width = self.screen.get_width()
        ammo_x = screen_width - ammo_text.get_width() - 20
        self.screen.blit(ammo_text, (ammo_x, 20))
