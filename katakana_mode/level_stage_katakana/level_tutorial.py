# name file: level_intro_npc.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import constants variable
from platforms import platforms_snow, platforms_item

# import levels module
from katakana_mode.level_stage_katakana.levels import Level


# for intro how to play the game
class Level_Tutorial(Level):
    """ This class for introduce the player """

    def __init__(self, player):
        """ Create intro """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/intro_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 165

        intro = [[platforms_snow.snow_dirt_wall, -140, 0],
                 [platforms_snow.snow_dirt_intro, 0, 460],
                 [platforms_snow.snow_dirt_big_wall, 769, 0]]

        portal = [[platforms_item.portal_snow, 700, 380]]

        for platform in intro:
            block = platforms_snow.Platform_snow(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in portal:
            gate = platforms_snow.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)
