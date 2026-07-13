import pygame
class Player:
    def __init__(self, x, y):
        self.width = 40
        self.height = 40
        self.color  = (255, 255, 255)
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.normal_speed = 4
        self.sprint_speed = 7
        self.speed = self.normal_speed

        self.max_health = 100
        self.health = self.max_health

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.k_LSHIFT]:
            self.speed = self.sprint_speed
        else:
            self.speed = self.normal_speed
        
        if keys[pygame.k_z] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        health_bar_width = self.width
        health_bar_height = 5
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width * health_ratio, health_bar_height))