# name file: level_01.py
# python version 3

# import pygame module
import pygame

# import constants variable
import constants

# import platforms modules
from platforms import (
    platforms_dirt, platforms_bad_sprite,
    platforms_item, platforms_katakana,
    platforms_enemy, platforms_special_enemy
)

# import levels module
from katakana_mode.levels import Level


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create Level 1 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            "spritesheet/day_background.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1166

        # Array with type of platform, and x, y location of the platform.
        # for level 01
        level01 = [[platforms_dirt.dirt_wall, -140, 0],
                   [platforms_dirt.dirt_medium_long_land, 0, 460],
                   [platforms_dirt.dirt_medium_long_land, 700, 460],
                   [platforms_dirt.dirt_medium_short_land, 770, 196],
                   [platforms_dirt.dirt_short_land, 1330, 460],
                   [platforms_dirt.dirt_grass_rounded, 1146, 319],
                   [platforms_dirt.dirt_medium_short_land, 1218, 125],
                   [platforms_dirt.dirt_medium_long_land, 1680, 460],
                   [platforms_dirt.dirt_big_wall, 2100, 0]]

        water_level01 = [[platforms_bad_sprite.medium_long_water, 490, 531],
                         [platforms_bad_sprite.medium_short_water, 1190, 531],
                         [platforms_bad_sprite.medium_long_water, 1470, 531]]

        portal = [[platforms_item.portal_snow, 2030, 380]]

        love_health = [[platforms_item.restore_health, 1380, 400]]

        katakana_a = [[platforms_katakana.katakana_a, 400, 200]]
        katakana_i = [[platforms_katakana.katakana_i, 600, 48]]
        katakana_u = [[platforms_katakana.katakana_u, 200, 200]]

        toxic_frog = [[platforms_enemy.fat_frog, 300, 405],
                      [platforms_enemy.fat_frog, 400, 405],
                      [platforms_enemy.fat_frog, 1680, 405]]

        # for special enemy
        special_enemy_a = [[platforms_special_enemy.big_ogre_a, 700, 360]]
        special_enemy_i = [[platforms_special_enemy.big_ogre_i, 1250, 20]]

        for platform in level01:
            block = platforms_dirt.Platform_dirt(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in water_level01:
            water_suicide = platforms_dirt.Platform_dirt(platform[0])
            water_suicide.rect.x = platform[1]
            water_suicide.rect.y = platform[2]
            water_suicide.player = self.player
            self.death_place_list.add(water_suicide)

        for platform in love_health:
            love_restore = platforms_item.Platform_hiragana_katakana(
                platform[0])
            love_restore.rect.x = platform[1]
            love_restore.rect.y = platform[2]
            love_restore.player = self.player
            self.love_restore_health.add(love_restore)

        for platform in portal:
            gate = platforms_item.Platform_snow(platform[0])
            gate.rect.x = platform[1]
            gate.rect.y = platform[2]
            gate.player = self.player
            self.portal_list.add(gate)

        # True Point increease scores player
        # katakana A Point
        for platform in katakana_a:
            true_point_lv1 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.katakana_A.add(true_point_lv1)

        # katakana I Point
        for platform in katakana_i:
            true_point_lv1 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            true_point_lv1.rect.x = platform[1]
            true_point_lv1.rect.y = platform[2]
            true_point_lv1.player = self.player
            self.katakana_I.add(true_point_lv1)

        # False point decrease health player
        # katakana U Point
        for platform in katakana_u:
            false_point_lv1 = platforms_katakana.Platform_hiragana_katakana(
                platform[0])
            false_point_lv1.rect.x = platform[1]
            false_point_lv1.rect.y = platform[2]
            false_point_lv1.player = self.player
            self.katakana_U.add(false_point_lv1)

        for platform in toxic_frog:
            eaten = platforms_enemy.Platform_enemy(platform[0])
            eaten.rect.x = platform[1]
            eaten.rect.y = platform[2]
            eaten.player = self.player
            self.enemy_list.add(eaten)

        # for special enemy/immune enemys
        for platform in special_enemy_a:
            special_eaten_A = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_A.rect.x = platform[1]
            special_eaten_A.rect.y = platform[2]
            special_eaten_A.player = self.player
            self.special_enemy_list_A.add(special_eaten_A)

        for platform in special_enemy_i:
            special_eaten_I = platforms_special_enemy.Platform_special_enemy(
                platform[0])
            special_eaten_I.rect.x = platform[1]
            special_eaten_I.rect.y = platform[2]
            special_eaten_I.player = self.player
            self.special_enemy_list_I.add(special_eaten_I)

        # Moving Enemy
        eaten = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten.rect.x = 780
        eaten.rect.y = 405
        eaten.boundary_left = 700
        eaten.boundary_right = 1100
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten.rect.x = 790
        eaten.rect.y = 140
        eaten.boundary_left = 790
        eaten.boundary_right = 1000
        eaten.change_x = 6
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)

        eaten = platforms_enemy.MovingEnemy(platforms_enemy.fat_frog)
        eaten.rect.x = 1300
        eaten.rect.y = 70
        eaten.boundary_left = 1300
        eaten.boundary_right = 1450
        eaten.change_x = 3
        eaten.player = self.player
        eaten.level = self
        self.enemy_list.add(eaten)
