import pygame
import math
import os

def load_image(filename, scale=None):
    path = os.path.join("assets", filename)
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except (pygame.error, FileNotFoundError):
        fallback = pygame.Surface(scale if scale else (32, 32))
        fallback.fill((255, 0, 255))
        return fallback

def get_distance(pos1, pos2):
    return math.hypot(pos2[0] - pos1[0], pos2[1] - pos1[1])

def get_angle(pos1, pos2):
    return math.atan2(pos2[1] - pos1[1], pos2[0] - pos1[0])

def rotate_towards(image, pos, target):
    angle = math.degrees(get_angle(pos, target))
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pos)
    return rotated_image, new_rect