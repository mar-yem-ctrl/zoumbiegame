import pygame
import sys

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.title_font = pygame.font.SysFont(None, 80)
        self.option_font = pygame.font.SysFont(None, 50)

        self.title_color = (0, 205, 0)      
        self.text_color = (255, 255, 255)    
        self.hover_color = (255, 255, 0)   

        self.play_rect = pygame.Rect(self.width // 2 - 100, 250, 200, 50)
        self.exit_rect = pygame.Rect(self.width // 2 - 100, 350, 200, 50)

    def draw(self, screen):
        title_text = self.title_font.render("ZOMBIE GAME", True, self.title_color)
        screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        title_text = self.title_font.render("ZOMBIE GAME", True, self.title_color)
        screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        mouse_pos = pygame.mouse.get_pos()

        if self.play_rect.collidepoint(mouse_pos):
            play_color = self.hover_color
        else:
            play_color = self.text_color
            
        play_text = self.option_font.render("PLAY", True, play_color)
        screen.blit(play_text, (self.play_rect.x + (self.play_rect.width - play_text.get_width()) // 2, self.play_rect.y))

        if self.exit_rect.collidepoint(mouse_pos):
            exit_color = self.hover_color
        else:
            exit_color = self.text_color
            
        exit_text = self.option_font.render("EXIT", True, exit_color)
        screen.blit(exit_text, (self.exit_rect.x + (self.exit_rect.width - exit_text.get_width()) // 2, self.exit_rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if self.play_rect.collidepoint(event.pos):
                    return "play"
                
                if self.exit_rect.collidepoint(event.pos):
                    return "exit"
                
        return"menu"