import pygame

def initialize():
    configDict = {}
    black = (0,0,0)
    white = (255,255,255)
    sunset = (253,72,47)
    blue = (0,0,225)
    maroon = (128,0,0)
    olive = (128,128,128)
    silver = (192,192,192)
    greenyellow = (184,255,0)
    brightblue = (47,228,253)
    orange = (255,113,0)
    yellow = (255,236,0)
    purple = (252,67,255)
    configDict["color"] = [white, blue, maroon, olive, silver, greenyellow, brightblue, orange, yellow, purple]
    configDict["black"] = black
    configDict["sunset"] = sunset
    # Py Game Initialization
    pygame.init()
    configDict["pygame_sound_obj"] = pygame.mixer.Sound("../media/crash.wav")

    configDict["surfaceWidth"] = 800
    configDict["surfaceHeight"] = 500

    configDict["imageHeight"] = 43
    configDict["imageWidth"] = 100

    configDict["surface"] = pygame.display.set_mode((configDict["surfaceWidth"], configDict["surfaceHeight"]))
    pygame.display.set_caption('Flappy Bird Escape')
    configDict["clock"] = pygame.time.Clock()

    configDict["img"] = pygame.image.load("../media/bird.png")
    return configDict
