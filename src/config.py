import os
import pygame
from random import randint, randrange


def initialize():
    configDict = {}

    black = (0,0,0)
    sunset = (253,72,47)

    white = (255,255,255)
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

    configDict["number_of_colors"] = len(configDict["color"])

    configDict["black"] = black
    configDict["sunset"] = sunset

    configDict["surfaceWidth"] = 1500
    configDict["surfaceHeight"] = 900

    configDict["imageHeight"] = 20
    configDict["imageWidth"] = 20

    # Py Game Initialization
    pygame.init()
    _ = pygame.mixer.Sound("media/crash.wav")
    # this object will be useful when we want to add music volume contol functionality to the game
    # configDict["pygame_sound_obj"] = pygame.mixer.Sound("media/crash.wav")

    configDict["surface"] = pygame.display.set_mode((configDict["surfaceWidth"], configDict["surfaceHeight"]))
    pygame.display.set_caption('Flappy Bird Escape')
    configDict["clock"] = pygame.time.Clock()

    configDict["bird_image"] = pygame.image.load("media/bird.png")


    configDict["x"] = 150
    configDict["y"] = 200
    configDict["y_move"] = 0

    configDict["x_block"] = configDict["surfaceWidth"]
    configDict["y_block"] = 0

    configDict["block_width"] = 75
    configDict["block_height"] = randint(0,(configDict["surfaceHeight"]/2))
    configDict["gap"] = configDict["imageHeight"] * 8
    configDict["block_move"] = 4
    configDict["current_score"] = 0
    configDict["current_level"] = 1

    configDict["blockColor"] = configDict["color"][randrange(0,len(configDict["color"]))]

    configDict["game_over"] = False

    configDict["crash_msg"] = "Crashed!"
    configDict["game_continue_msg"] = "Press any key to continue"
    configDict["max_user_score"] = 0
    configDict["user_name"] = None
    configDict["max_levels"] = 10
    configDict["max_score_in_level"] = 10
    configDict["max_score_possible"] = configDict["max_levels"] * configDict["max_score_in_level"]
    configDict["game_complete_msg_hurray"] = "Hurray!"
    configDict["game_complete_msg_desc"] = "You have completed all levels"
    configDict["smallText"] = pygame.font.SysFont("Arial", 20)
    configDict["largeText"] = pygame.font.SysFont("Arial", 150)

    background = pygame.Surface(configDict["surface"].get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    #
    charRect = pygame.Rect((0, 0), (10, 10))
    # print(os.path.abspath("airbender.png"))
    charImage = pygame.image.load(os.path.abspath("media/background1.png"))
    charImage = pygame.transform.scale(charImage, charRect.size)
    charImage = charImage.convert()

    background.blit(charImage, charRect)  # This just makes it in the same location
    # # and prints it the same size as the image
    #
    # Almost Original Background
    configDict["background"] = pygame.image.load("media/background1.png")
    # Space nebula background
    # configDict["background"] = pygame.image.load("media/space_nebula1.jpg")
    # Image needs to be of higher resolution
    # configDict["background"] = pygame.image.load("media/space_galaxy1.jpg")

    # configDict["background"] = background
    configDict["speed"] = 1


    return configDict
