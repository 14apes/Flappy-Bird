#!/usr/bin/env python
import pygame
from src.FluffyBird import FluffyBird

if __name__ == '__main__':
    bird = FluffyBird()
    bird.fly()
    pygame.quit()
    quit()
