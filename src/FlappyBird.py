"""Summary
"""
import pygame
import time
from random import randint, randrange
from src.config import initialize


class FlappyBird:

    """Summary

    Attributes:
        configDict (TYPE): Description
    """

    def __init__(self):
        """Summary

        Returns:
            TYPE: Description
        """
        self.configDict = initialize()
        return

    def _display_level(self):
        """Summary

        Returns:
            TYPE: Description
        """
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("Level: " + str(self.configDict["current_level"]), True, self.configDict["color"][0])
        self.configDict["surface"].blit(text, [0, 20])
        return

    def _display_score(self):
        """Summary

        Returns:
            TYPE: Description
        """
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("Score: " + str(self.configDict["current_score"]), True, self.configDict["color"][0])
        self.configDict["surface"].blit(text, [0, 0])
        return

    def _blocks(self, color):
        """Summary

        Args:
            color (TYPE): Description

        Returns:
            TYPE: Description
        """
        pygame.draw.rect(self.configDict["surface"], color, [self.configDict["x_block"], self.configDict["y_block"], self.configDict["block_width"], self.configDict["block_height"]])
        pygame.draw.rect(self.configDict["surface"], color, [self.configDict["x_block"], self.configDict["y_block"] + self.configDict["block_height"] + self.configDict["gap"], self.configDict["block_width"],  self.configDict["surfaceHeight"]])
        return


    def _replay_or_quit(self):
        """Summary

        Returns:
            TYPE: Description
        """
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                continue

            return event.key

        return None


    def _makeTextObjs(self, text, font):
        """Summary

        Args:
            text (TYPE): Description
            font (TYPE): Description

        Returns:
            TYPE: Description
        """
        textSurface = font.render(text, True, self.configDict["sunset"])
        return textSurface, textSurface.get_rect()


    def _msgSurface(self):
        """Summary

        Returns:
            TYPE: Description
        """
        titleTextSurf, titleTextRect = self._makeTextObjs(self.configDict["crash_msg"], self.configDict["largeText"])
        titleTextRect.center = self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2
        self.configDict["surface"].blit(titleTextSurf, titleTextRect)

        # TODO
        #pygame.mixer.Sound.play(crash_sound)
        #pygame.mixer.music.stop()
        typTextSurf, typTextRect = self._makeTextObjs(self.configDict["game_continue_msg"], self.configDict["smallText"])
        typTextRect.center =  self.configDict["surfaceWidth"] / 2, ((self.configDict["surfaceHeight"] / 2) + 100)
        self.configDict["surface"].blit(typTextSurf, typTextRect)

        pygame.display.update()
        time.sleep(1)

        if self._replay_or_quit() == None:
            self.__init__()
            self.fly()
        return

    def _gameOver(self):
        """Summary

        Returns:
            TYPE: Description
        """
        self.configDict["game_over"] = True
        self._msgSurface()
        return

    def _gameVictory(self):
        """

        Returns:
            TYPE: Description
        """
        typTextSurf, typTextRect = self._makeTextObjs(self.configDict["game_complete_msg"], self.configDict["smallText"])
        typTextRect.center = self.configDict["surfaceWidth"] / 2, ((self.configDict["surfaceHeight"] / 2))
        self.configDict["surface"].blit(typTextSurf, typTextRect)

        pygame.display.update()
        quit(0)
        return

    def _update_bird(self):
        """Summary

        Returns:
            TYPE: Description
        """
        self.configDict["surface"].blit(self.configDict["bird_image"], (self.configDict["x"], self.configDict["y"]))

        return

    def _stateValidation(self):
        """

        Return:
            TYPE: Description
        """
        if self.configDict["y"] > self.configDict["surfaceHeight"] - 40 or self.configDict["y"] < 0:
            self._gameOver()
        if self.configDict["x"] + self.configDict["imageWidth"] > self.configDict["x_block"]:
            if self.configDict["x"] < self.configDict["x_block"] + self.configDict["block_width"]:
                if self.configDict["y"] < self.configDict["block_height"]:
                    if self.configDict["x"] - self.configDict["imageWidth"] < self.configDict["block_width"] + \
                            self.configDict["x_block"]:
                        self._gameOver()

        if self.configDict["x"] + self.configDict["imageWidth"] > self.configDict["x_block"]:
            if self.configDict["y"] + self.configDict["imageHeight"] > self.configDict["block_height"] + \
                    self.configDict["gap"]:
                if self.configDict["x"] < self.configDict["block_width"] + self.configDict["x_block"]:
                    self._gameOver()

        return

    def _update_gap(self):
        """


        """
        # Decrease gap for each level
        self.configDict["gap"] = int(self.configDict["gap"] / (0.1 + 0.3 * self.configDict["current_level"]))
        return


    def _update_level(self):
        """

        Return:
            Description
        """
        if self.configDict["current_score"] % self.configDict["max_score_in_level"] == 0:
            # Increase level after a  certain score
            self.configDict["current_level"] += 1
            self._update_gap()
        return

    def _compute_score(self):
        """

        Return:
            Description
        """
        if self.configDict["x_block"] < (-1 * self.configDict["block_width"]):
            self.configDict["x_block"] = self.configDict["surfaceWidth"]
            self.configDict["block_height"] = randint(0, (self.configDict["surfaceHeight"] / 2))
            self.configDict["blockColor"] = self.configDict["color"][randrange(0, len(self.configDict["color"]))]
            self.configDict["current_score"] += 1
            self._update_level()
        return

    def fly(self):
        """Summary

        Returns:
            TYPE: Description
        """
        while not self.configDict["game_over"] and self.configDict["current_level"] <= self.configDict["max_levels"] and self.configDict["current_score"] <= self.configDict["max_score_possible"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    self.configDict["game_over"] = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.configDict["y_move"] = -5

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.configDict["y_move"] = 5
                else:
                    self.configDict["y_move"] = 5

            self.configDict["y"] += self.configDict["y_move"]

            self.configDict["surface"].fill(self.configDict["black"])  # black color fill
            # self.configDict["surface"].blit(self.configDict["background"], (0, 0))
            self._update_bird()
            self._blocks(self.configDict["blockColor"])
            self._display_score()
            self._display_level()
            self.configDict["x_block"] -= self.configDict["block_move"]
            self._stateValidation()
            if not self.configDict["game_over"]:
                self._compute_score()
            else:
                break
            pygame.display.update()
            self.configDict["clock"].tick(60)
        if self.configDict["current_score"] >= self.configDict["max_score_possible"]:
            self._gameVictory()
            print(self.configDict["game_complete_msg"])
        return
