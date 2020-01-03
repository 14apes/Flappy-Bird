import pygame
import time
from random import randint, randrange
from config import initialize


class FlappyBird:
    def __init__(self):
        self.configDict = initialize()
        return

    def _level(self, inta, level_color, surface):

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Level: " + str(inta), True, level_color)
        surface.blit(text, [0, 20])

    def _score(self, count, score_color, surface):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Score: " + str(count), True, score_color)
        surface.blit(text, [0, 0])

    def _blocks(self, x_block, y_block, block_width, block_height, gap, color, surface, surfaceHeight):

        pygame.draw.rect(surface, color, [x_block, y_block, block_width, block_height])
        pygame.draw.rect(surface, color, [x_block, y_block + block_height + gap, block_width,  surfaceHeight])


    def _replay_or_quit(self, ):
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                continue

            return event.key

        return None


    def _makeTextObjs(self, text, font, sunset):
        textSurface = font.render(text, True, sunset)
        return textSurface, textSurface.get_rect()


    def _msgSurface(self, text):
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        largeText = pygame.font.Font('freesansbold.ttf', 150)

        titleTextSurf, titleTextRect = self._makeTextObjs(text, largeText, self.configDict["sunset"])
        titleTextRect.center = self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2
        self.configDict["surface"].blit(titleTextSurf, titleTextRect)

        #pygame.mixer.Sound.play(crash_sound)
        #pygame.mixer.music.stop()
        typTextSurf, typTextRect = self._makeTextObjs('Press any key to continue', smallText, self.configDict["sunset"])
        typTextRect.center =  self.configDict["surfaceWidth"] / 2, ((self.configDict["surfaceHeight"] / 2) + 100)
        self.configDict["surface"].blit(typTextSurf, typTextRect)

        pygame.display.update()
        time.sleep(1)

        while self._replay_or_quit() == None:
            self.configDict["clock"].tick()

        self.fly()

    def _gameOver(self):
        self._msgSurface('crashed!')

    def _bird(self, x, y, image, surface):
        surface.blit(image, (x,y))


    def fly(self):
        x = 150
        y = 200
        y_move = 0

        x_block = self.configDict["surfaceWidth"]
        y_block = 0

        block_width = 75
        block_height = randint(0,(self.configDict["surfaceHeight"]/2))
        gap = self.configDict["imageHeight"] * 5
        block_move = 4
        current_score = 0
        current_level = 1



        blockColor = self.configDict["color"][randrange(0,len(self.configDict["color"]))]

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

            self.configDict["surface"].fill(self.configDict["black"])  # black color fill
            self._bird(x ,y, self.configDict["img"], self.configDict["surface"])


            self._blocks(x_block, y_block, block_width, block_height, gap, blockColor, self.configDict["surface"], self.configDict["surfaceHeight"])
            self._score(current_score, self.configDict["color"][0], self.configDict["surface"])
            self._level(current_level, self.configDict["color"][0], self.configDict["surface"])
            x_block -= block_move

            if y > self.configDict["surfaceHeight"]-40 or y < 0:
                self._gameOver()

            if x_block < (-1*block_width):
                x_block = self.configDict["surfaceWidth"]
                block_height = randint(0, (self.configDict["surfaceHeight"] / 2))
                blockColor = self.configDict["color"][randrange(0,len(self.configDict["color"]))]
                current_score+=1

            if x + self.configDict["imageWidth"] > x_block:
                if x < x_block + block_width:
                    if y < block_height:
                        if x - self.configDict["imageWidth"] < block_width + x_block:
                            self._gameOver()

            if x + self.configDict["imageWidth"] > x_block:
                if y + self.configDict["imageHeight"] > block_height+gap:
                    if x < block_width + x_block:
                        self._gameOver()

            if 3 <= current_score < 5:


                block_move = 5
                gap = self.configDict["imageHeight"] * 4
                current_level += 1
            if 5 <= current_score < 8:

                block_move = 6
                gap = self.configDict["imageHeight"] *3
                current_level += 1
            if 8 <= current_score < 14:

                block_move = 7
                gap = self.configDict["imageHeight"] *2.7
                current_level += 1

            pygame.display.update()
            self.configDict["clock"].tick(60)
        return


if __name__ == '__main__':
    fb = FlappyBird()
    fb.fly()
    pygame.quit()
    quit()
