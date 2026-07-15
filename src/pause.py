import pygame
import sys

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.text_font = pygame.font.SysFont("Arial", 28, bold=True)
        self.WHITE = (255, 255, 255)
        self.GRAY = (150, 150, 150)
        self.BLACK = (0, 0, 0)
        self.RED = (200, 30, 30)

    def draw(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128)) 
        self.screen.blit(overlay, (0, 0))
        title_surf = self.title_font.render("GAME PAUSED", True, self.WHITE)
        title_rect = title_surf.get_rect(center=(width // 2, height // 2 - 80))
        self.screen.blit(title_surf, title_rect)
        resume_surf = self.text_font.render("Press 'ESC' or 'P' to Resume", True, self.GRAY)
        resume_rect = resume_surf.get_rect(center=(width // 2, height // 2))
        self.screen.blit(resume_surf, resume_rect)
        quit_surf = self.text_font.render("Press 'Q' to Quit Game", True, self.RED)
        quit_rect = quit_surf.get_rect(center=(width // 2, height // 2 + 50))
        self.screen.blit(quit_surf, quit_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    return "RESUME"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        return "PAUSED"