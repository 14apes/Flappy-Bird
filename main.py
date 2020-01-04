#!/usr/bin/env python
import pygame
from src.FlappyBird import FlappyBird

if __name__ == '__main__':
    bird = FlappyBird()
    bird.fly()
    pygame.quit()
    quit()
