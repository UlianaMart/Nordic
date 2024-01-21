import pygame


def music():
    pygame.mixer.music.load("sounds/музыка на фон.mp3")
    pygame.mixer.music.play(-1)


def conflict():
    conflict = pygame.mixer.Sound("sounds/звук столкновения.mp3")
    conflict.play()

