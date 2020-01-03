import pygame
import time
from random import randint,randrange
from config import initialize

def level(inta, level_color, surface):

    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Level: "+str(inta), True, level_color)
    surface.blit(text, [0,20])

def score(count, score_color, surface):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, score_color)
    surface.blit(text, [0,0])

def blocks(x_block, y_block, block_width, block_height, gap, color, surface, surfaceHeight):

    pygame.draw.rect(surface, color, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, color, [x_block,y_block+block_height+gap,block_width, surfaceHeight])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None


def makeTextObjs(text, font, sunset):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()


def msgSurface(text, configDict):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText, configDict["sunset"])
    titleTextRect.center = configDict["surfaceWidth"] / 2, configDict["surfaceHeight"] / 2
    configDict["surface"].blit(titleTextSurf, titleTextRect)

    #pygame.mixer.Sound.play(crash_sound)
    #pygame.mixer.music.stop()
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText, configDict["sunset"])
    typTextRect.center =  configDict["surfaceWidth"] / 2, ((configDict["surfaceHeight"] / 2) + 100)
    configDict["surface"].blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        configDict["clock"].tick()

    utils_main()

def gameOver(configDict):
    msgSurface('crashed!', configDict)

def bird(x, y, image, surface):
    surface.blit(image, (x,y))


def utils_main():
    configDict = initialize()
    x = 150
    y = 200
    y_move = 0

    x_block = configDict["surfaceWidth"]
    y_block = 0

    block_width = 75
    block_height = randint(0,(configDict["surfaceHeight"]/2))
    gap = configDict["imageHeight"] * 5
    block_move = 4
    current_score = 0
    current_level = 1



    blockColor = configDict["color"][randrange(0,len(configDict["color"]))]

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        configDict["surface"].fill(configDict["black"])  # black color fill
        bird(x ,y, configDict["img"], configDict["surface"])


        blocks(x_block, y_block, block_width, block_height, gap, blockColor, configDict["surface"], configDict["surfaceHeight"])
        score(current_score, configDict["color"][0], configDict["surface"])
        level(current_level, configDict["color"][0], configDict["surface"])
        x_block -= block_move

        if y > configDict["surfaceHeight"]-40 or y < 0:
            gameOver(configDict)

        if x_block < (-1*block_width):
            x_block = configDict["surfaceWidth"]
            block_height = randint(0, (configDict["surfaceHeight"] / 2))
            blockColor = configDict["color"][randrange(0,len(configDict["color"]))]
            current_score+=1

        if x + configDict["imageWidth"] > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - configDict["imageWidth"] < block_width + x_block:
                        gameOver(configDict)

        if x + configDict["imageWidth"] > x_block:
            if y + configDict["imageHeight"] > block_height+gap:
                if x < block_width + x_block:
                    gameOver(configDict)

        if 3 <= current_score < 5:


            block_move = 5
            gap = configDict["imageHeight"] * 4
            current_level += 1
        if 5 <= current_score < 8:

            block_move = 6
            gap = configDict["imageHeight"] *3
            current_level += 1
        if 8 <= current_score < 14:

            block_move = 7
            gap = configDict["imageHeight"] *2.7
            current_level += 1







        pygame.display.update()
        configDict["clock"].tick(60)
    return
