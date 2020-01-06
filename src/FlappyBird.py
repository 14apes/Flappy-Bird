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
        self._update_display()
        self._play_music(self.configDict["game_music"])
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
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

            # elif event.type == pygame.KEYDOWN:
            #     continue

            return event.key

        return None

    def _makeTextObjs(self, text, font, color):
        """Summary

        Args:
            text (TYPE): Description
            font (TYPE): Description
            color (TYPE): Description

        Returns:
            TYPE: Description
        """
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def _msgSurface(self, screen_message, font, centre_offset_x=0, centre_offset_y=0, color=None):
        """Summary

        Returns:
            TYPE: Description

        Args:
            screen_message (TYPE): Description
            font (TYPE): Description
            centre_offset_x (int, optional): Description
            centre_offset_y (int, optional): Description
            color (None, optional): Description
        """
        if color is None:
            color = self.configDict["sunset"]
        titleTextSurf, titleTextRect = self._makeTextObjs(screen_message, font, color)
        titleTextRect.center = centre_offset_x, centre_offset_y
        self.configDict["surface"].blit(titleTextSurf, titleTextRect)
        return

    def _gameOver(self):
        """Summary

        Returns:
            TYPE: Description
        """
        print("Game Over!")
        self._play_music(self.configDict["crash_music"])
        self.configDict["game_over"] = True
        self._msgSurface(self.configDict["crash_msg"],  self.configDict["largeText"], self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2)
        self._msgSurface(self.configDict["game_continue_msg"], self.configDict["smallText"], self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2 + 100)

        # TODO
        #pygame.mixer.Sound.play(crash_sound)
        #pygame.mixer.music.stop()

        pygame.display.update()
        time.sleep(1)

        if self._replay_or_quit() == None:
            self.__init__()
            self.fly()
        return

    def _gameVictory(self):
        """
        Returns:
            TYPE: Description
        """
        print("You Won!")
        self._play_music(self.configDict["victory_music"])
        self._msgSurface(self.configDict["game_complete_msg_hurray"], self.configDict["largeText"], self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2)
        self._msgSurface(self.configDict["game_complete_msg_desc"], self.configDict["smallText"], self.configDict["surfaceWidth"] / 2, self.configDict["surfaceHeight"] / 2 + 100)
        pygame.display.update()
        time.sleep(2)
        while True:
            key = self._replay_or_quit
            if key == pygame.K_SPACE:
                self.__init__()
                self.fly()
                return
            elif key == pygame.QUIT or key == pygame.K_ESCAPE:
                quit(0)
                return

    def _play_music(self, sound):
        """Summary

        Returns:
            TYPE: Description
        """
        if self.configDict["mute"]:
            pass
        else:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play(0)
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
        Returns:
            TYPE: Description


        """
        # Decrease gap for each level
        self.configDict["gap"] = int(self.configDict["gap"] / (0.1 + 0.3 * self.configDict["current_level"]))
        return

    def _update_speed(self):
        """Summary

        Returns:
            TYPE: Description
        """
        self.configDict["speed"] += 0.2 * self.configDict["current_level"]
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
            self._update_speed()
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

    def _update_background(self):
        """Summary

        Returns:
            TYPE: Description
        """
        # self.configDict["surface"].fill(self.configDict["black"])  # black color fill
        self.configDict["image_translation_offset"].x = self.configDict["image_translation_offset"].x - self.configDict["speed"] * self.configDict["block_move"]
        # print(self.configDict["image_translation_offset"].x, self.configDict["image_rect"].w)
        if -self.configDict["image_translation_offset"].x  >= self.configDict["image_rect"].w - self.configDict["surfaceWidth"]:
            # self.configDict["image_translation_offset"].x = (-1 * self.configDict["image_translation_offset"].x) - self.configDict["image_rect"].w
            self.configDict["image_translation_offset"].x = -self.configDict["surfaceWidth"]
            # self.configDict["background"].blit(self.configDict["background"], (0, 0))
            # self.configDict["surface"].blit(self.configDict["background"], self.configDict["image_translation_offset"])
            # print("##:", self.configDict["image_translation_offset"].x)
        self.configDict["surface"].blit(self.configDict["background"], self.configDict["image_translation_offset"])
        # x_offset = x_offset - self.configDict["speed"] * self.configDict["block_move"]
        # self.configDict["surface"].scroll(, 0)
        return

    def _update_display(self):
        """Summary

        Returns:
            TYPE: Description
        """
        self._update_background()
        self._blocks(self.configDict["blockColor"])
        self._update_bird()
        self._display_score()
        self._display_level()

        return

    def _update_coordinates(self):

        # updated coordinates of bird
        self.configDict["y"] += self.configDict["y_move"]
        # updated coordinates of pillars
        self.configDict["x_block"] = self.configDict["x_block"] - self.configDict["speed"] * self.configDict["block_move"]

        return

    def _update_event(self):
        """Summary

        Returns:
            TYPE: Description
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                self.configDict["game_over"] = True

            if self.configDict["pause"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Game Unpause! 00")
                        self.configDict["pause"] = False
                    else:
                        # print("Game in Pause")
                        return 1
                else:
                    # print("Game in Pause")
                    return 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        print("Game Unpause! 01")
                        self.configDict["pause"] = False
                    else:
                        # print("Game in Pause")
                        return 1
                else:
                    # print("Game in Pause")
                    return 1

            elif event.type == pygame.VIDEORESIZE:
                old_surface_saved = self.configDict["surface"]
                self.configDict["surface"] = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                self.configDict["surface"].blit(old_surface_saved, (0,0))
                del old_surface_saved

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.configDict["y_move"] = -5
                elif event.key == pygame.K_SPACE:
                    if self.configDict["pause"]:
                        print("Game Unpause! 2")
                        self.configDict["pause"] = False
                    else:
                        print("Game Paused! 2")
                        self.configDict["pause"] = True
                        return 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.configDict["y_move"] = 5
                elif event.key == pygame.K_SPACE:
                    if self.configDict["pause"]:
                        print("Game Unpause! 1")
                        self.configDict["pause"] = False
                    else:
                        print("Game Paused! 1")
                        self.configDict["pause"] = True
                        return 1

            else:
                self.configDict["y_move"] = 5
        self._update_coordinates()
        return 0

    def fly(self):
        """Summary

        Returns:
            TYPE: Description
        """
        # while self._replay_or_quit() is None:
        #     # Waiting for user input
        #     # self._msgSurface(self.configDict["start_game_message"], self.configDict["largeText"])
        #     pass
        # x_offset = 0
        while not self.configDict["game_over"] and self.configDict["current_level"] <= self.configDict["max_levels"] and self.configDict["current_score"] <= self.configDict["max_score_possible"]:
            if self._update_event() == 1:
                continue
            self._update_display()
            self._stateValidation()
            if not self.configDict["game_over"]:
                self._compute_score()
            else:
                break
            pygame.display.update()
            self.configDict["clock"].tick(60)
        if self.configDict["current_score"] >= self.configDict["max_score_possible"]:
            self._gameVictory()
            print(self.configDict["game_complete_msg_hurray"], self.configDict["game_complete_msg_desc"])
        return
