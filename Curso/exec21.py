# Faça um programa que reproduza um audio mp3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play()
pygame.event.wait()
