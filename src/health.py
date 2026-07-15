import pygame

class HealthPack(pygame.sprite.Sprite):
    def __init__(self, x, y, heal_amount=30):
        super().__init__()
        self.heal_amount = heal_amount  
        
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        
       
        pygame.draw.rect(self.image, (240, 240, 240), (0, 0, 30, 30), border_radius=5)
        
        pygame.draw.rect(self.image, (255, 0, 0), (12, 5, 6, 20))  # Khet l-waqf
        pygame.draw.rect(self.image, (255, 0, 0), (5, 12, 20, 6))  # Khet l-na3ess
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def apply_heal(self, player):
        """Kat-zid l-health l-player u mad-douzsh l-max_health dyalu"""
        if player.health < player.max_health:
            player.health += self.heal_amount
            if player.health > player.max_health:
                player.health = player.max_health
            return True  