"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""

# Import pygame and libraries
from pygame.locals import *

# import pygame module
import os
import pygame

import constants

# import sounds module
import configsounds

import gameoverscreen

from platforms import MovingPlatform_dirt, MovingPlatform_dark_brick, MovingPlatform_snow, MovingPlatform_dirt_sand, MovingPlatform_brick_red, MovingPlatform_ancient_brick
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
	""" This class represents the bar at the bottom that the player
	controls. """
	# -- Methods
	def __init__(self):
		""" Constructor function """

		# Call the parent's constructor
		super().__init__()

		# -- Attributes
		# set scores for player
		self.scores = 0
		# set kills for player
		self.kills = 0 
		# set health number for player
		self.health_number = 100
		# set restore health percentage
		self.give_health = 20
		# set damage for enemy
		self.general_enemy_dmg = 30
		self.special_enemy_dmg = 40
		self.false_point_dmg = 40
		# Set speed vector of player
		self.change_x = 0
		self.change_y = 0
 
		# This holds all the images for the animated walk left/right
		# of our player
		self.walking_frames_l = []
		self.walking_frames_r = []
 
		# What direction is the player facing?
		self.direction = "R"

		# removing special enemy
		# Basic Vocal
		self.special_remove_A = False
		self.special_remove_I = False
		self.special_remove_U = False
		self.special_remove_E = False
		self.special_remove_O = False

		# Vocal K
		self.special_remove_KA = False
		self.special_remove_KI = False
		self.special_remove_KU = False
		self.special_remove_KE = False
		self.special_remove_KO = False

		# Vocal S
		self.special_remove_SA = False
		self.special_remove_SI = False
		self.special_remove_SU = False
		self.special_remove_SE = False
		self.special_remove_SO = False

		# Vocal T
		self.special_remove_TA = False
		self.special_remove_TI = False
		self.special_remove_TU = False
		self.special_remove_TE = False
		self.special_remove_TO = False

		# Vocal N
		self.special_remove_NA = False
		self.special_remove_NI = False
		self.special_remove_NU = False
		self.special_remove_NE = False
		self.special_remove_NO = False

		# Vocal H
		self.special_remove_HA = False
		self.special_remove_HI = False
		self.special_remove_HU = False
		self.special_remove_HE = False
		self.special_remove_HO = False

		# Vocal M
		self.special_remove_MA = False
		self.special_remove_MI = False
		self.special_remove_MU = False
		self.special_remove_ME = False
		self.special_remove_MO = False

		# Vocal Y
		self.special_remove_YA = False
		self.special_remove_YU = False
		self.special_remove_YO = False

		# Vocal R
		self.special_remove_RA = False
		self.special_remove_RI = False
		self.special_remove_RU = False
		self.special_remove_RE = False
		self.special_remove_RO = False

		# Vocal W
		self.special_remove_WA = False
		self.special_remove_WO = False

		# Vocal N
		self.special_remove_N = False


		# for fix bug
		self.special_remove_A_lv2 = False
		self.special_remove_I_lv2 = False
		self.special_remove_U_lv2 = False
 
		# List of sprites we can bump against
		self.level = None
 
		sprite_sheet = SpriteSheet("spritesheet/player.png")
		# Load all the right facing images into a list
		image = sprite_sheet.get_image(10, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 7, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 106, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(160, 208, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(10, 305, 66, 90)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(85, 305, 66, 90)
		self.walking_frames_r.append(image)

		# Load all the right facing images, then flip them
		# to face left.
		image = sprite_sheet.get_image(10, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 7, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 106, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(160, 208, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(10, 305, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(85, 305, 66, 90)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
 
		# Set the image the player starts with
		self.image = self.walking_frames_r[0]
 
		# Set a reference to the image rect.
		self.rect = self.image.get_rect()
 
	def update(self):
		""" Move the player. """
		# Gravity
		self.calc_grav()
 
		# Move left/right
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]
 
		# for platform_list
		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right,
			# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right

		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
 
			# Stop our vertical movement
			self.change_y = 0
 
			if isinstance(block, MovingPlatform_dirt):
				self.rect.x += block.change_x

			if isinstance(block, MovingPlatform_dark_brick):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_ancient_brick):
				self.rect.x += block.change_x

			if isinstance(block, MovingPlatform_brick_red):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_dirt_sand):
				self.rect.x += block.change_x
			
			if isinstance(block, MovingPlatform_snow):
				self.rect.x += block.change_x
 

		# For general enemy list
		# If player touched by enemys
		hit_by_enemy_list = pygame.sprite.spritecollide(self, self.level.enemy_list, True)
		for eaten in hit_by_enemy_list:
			self.health_number -= self.general_enemy_dmg
			configsounds.ouch_sfx.play()
			
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()


		# for special enemy list
		# If player touched by special enemys
		# Basic Vocal
		# Symbol A
		special_hit_enemy_list_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A, True)
		for special_eaten_A in special_hit_enemy_list_A:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_A == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol I		
		special_hit_enemy_list_I = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I, True)
		for special_eaten_I in special_hit_enemy_list_I:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_I == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol U
		special_hit_enemy_list_U = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U, True)
		for special_eaten_U in special_hit_enemy_list_U:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_U == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol E
		special_hit_enemy_list_E = pygame.sprite.spritecollide(self, self.level.special_enemy_list_E, True)
		for special_eaten_E in special_hit_enemy_list_E:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_E == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol O
		special_hit_enemy_list_O = pygame.sprite.spritecollide(self, self.level.special_enemy_list_O, True)
		for special_eaten_O in special_hit_enemy_list_O:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_O == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Vocal K
		# Symbol KA
		special_hit_enemy_list_KA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KA, True)
		for special_eaten_KA in special_hit_enemy_list_KA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_KA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol KI		
		special_hit_enemy_list_KI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KI, True)
		for special_eaten_KI in special_hit_enemy_list_KI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_KI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol KU
		special_hit_enemy_list_KU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KU, True)
		for special_eaten_KU in special_hit_enemy_list_KU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_KU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol KE
		special_hit_enemy_list_KE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KE, True)
		for special_eaten_KE in special_hit_enemy_list_KE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_KE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol KO
		special_hit_enemy_list_KO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KO, True)
		for special_eaten_KO in special_hit_enemy_list_KO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_KO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()


		# Vocal S
		# Symbol SA
		special_hit_enemy_list_SA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SA, True)
		for special_eaten_SA in special_hit_enemy_list_SA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_SA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol SI		
		special_hit_enemy_list_SI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SI, True)
		for special_eaten_SI in special_hit_enemy_list_SI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_SI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol SU
		special_hit_enemy_list_SU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SU, True)
		for special_eaten_SU in special_hit_enemy_list_SU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_SU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol SE
		special_hit_enemy_list_SE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SE, True)
		for special_eaten_SE in special_hit_enemy_list_SE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_SE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol SO
		special_hit_enemy_list_SO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SO, True)
		for special_eatenSKO in special_hit_enemy_list_SO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_SO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()


		# Vocal T
		# Symbol TA
		special_hit_enemy_list_TA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TA, True)
		for special_eaten_TA in special_hit_enemy_list_TA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_TA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol TI		
		special_hit_enemy_list_TI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TI, True)
		for special_eaten_TI in special_hit_enemy_list_TI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_TI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol TU
		special_hit_enemy_list_TU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TU, True)
		for special_eaten_TU in special_hit_enemy_list_TU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_TU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol TE
		special_hit_enemy_list_TE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TE, True)
		for special_eaten_TE in special_hit_enemy_list_TE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_TE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol TO
		special_hit_enemy_list_TO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TO, True)
		for special_eaten_TO in special_hit_enemy_list_TO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_TO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		
		# Vocal N
		# Symbol NA
		special_hit_enemy_list_NA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NA, True)
		for special_eaten_NA in special_hit_enemy_list_NA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_NA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol NI		
		special_hit_enemy_list_NI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NI, True)
		for special_eaten_NI in special_hit_enemy_list_NI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_NI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol NU
		special_hit_enemy_list_NU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NU, True)
		for special_eaten_NU in special_hit_enemy_list_NU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_NU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol NE
		special_hit_enemy_list_NE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NE, True)
		for special_eaten_NE in special_hit_enemy_list_NE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_NE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol NO
		special_hit_enemy_list_NO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NO, True)
		for special_eaten_NO in special_hit_enemy_list_NO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_NO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		

		# Vocal H
		# Symbol HA
		special_hit_enemy_list_HA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HA, True)
		for special_eaten_HA in special_hit_enemy_list_HA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_HA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol HI		
		special_hit_enemy_list_HI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HI, True)
		for special_eaten_HI in special_hit_enemy_list_HI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_HI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol HU
		special_hit_enemy_list_HU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HU, True)
		for special_eaten_HU in special_hit_enemy_list_HU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_HU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol HE
		special_hit_enemy_list_HE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HE, True)
		for special_eaten_HE in special_hit_enemy_list_HE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_HE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol HO
		special_hit_enemy_list_HO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HO, True)
		for special_eaten_HO in special_hit_enemy_list_HO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_HO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		

		# Vocal M
		# Symbol MA
		special_hit_enemy_list_MA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MA, True)
		for special_eaten_MA in special_hit_enemy_list_MA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_MA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol MI		
		special_hit_enemy_list_MI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MI, True)
		for special_eaten_MI in special_hit_enemy_list_MI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_MI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol MU
		special_hit_enemy_list_MU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MU, True)
		for special_eaten_MU in special_hit_enemy_list_MU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_MU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol ME
		special_hit_enemy_list_ME = pygame.sprite.spritecollide(self, self.level.special_enemy_list_ME, True)
		for special_eaten_ME in special_hit_enemy_list_ME:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_ME == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol MO
		special_hit_enemy_list_MO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MO, True)
		for special_eaten_MO in special_hit_enemy_list_MO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_MO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		

		# Vocal Y
		# Symbol YA
		special_hit_enemy_list_YA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YA, True)
		for special_eaten_YA in special_hit_enemy_list_YA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_YA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol YU
		special_hit_enemy_list_YU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YU, True)
		for special_eaten_YU in special_hit_enemy_list_YU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_YU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol YO
		special_hit_enemy_list_YO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YO, True)
		for special_eaten_YO in special_hit_enemy_list_YO:
			
			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_YO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		

		# Vocal R
		# Symbol RA
		special_hit_enemy_list_RA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RA, True)
		for special_eaten_RA in special_hit_enemy_list_RA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_RA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol RI		
		special_hit_enemy_list_RI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RI, True)
		for special_eaten_RI in special_hit_enemy_list_RI:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_RI == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol RU
		special_hit_enemy_list_RU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RU, True)
		for special_eaten_RU in special_hit_enemy_list_RU:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_RU == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol RE
		special_hit_enemy_list_RE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RE, True)
		for special_eaten_RE in special_hit_enemy_list_RE:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_RE == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol RO
		special_hit_enemy_list_RO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RO, True)
		for special_eaten_RO in special_hit_enemy_list_RO:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_RO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Vocal W
		# Symbol WA
		special_hit_enemy_list_WA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WA, True)
		for special_eaten_WA in special_hit_enemy_list_WA:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_WA == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol WO
		special_hit_enemy_list_WO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WO, True)
		for special_eaten_WO in special_hit_enemy_list_WO:
			
			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_WO == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Vocal Single N
		special_hit_enemy_list_N = pygame.sprite.spritecollide(self, self.level.special_enemy_list_N, True)
		for special_eaten_N in special_hit_enemy_list_N:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_N == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		


		# for fix bug
		# Symbol A
		special_hit_enemy_list_A_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A_lv2, True)
		for special_eaten_A_lv2 in special_hit_enemy_list_A_lv2:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_A == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()

		# Symbol I		
		special_hit_enemy_list_I_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I_lv2, True)
		for special_eaten_I_lv2 in special_hit_enemy_list_I_lv2:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_I == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# Symbol U
		special_hit_enemy_list_U_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U_lv2, True)
		for special_eaten_U_lv2 in special_hit_enemy_list_U_lv2:

			self.health_number -=  self.special_enemy_dmg
			configsounds.ouch_sfx.play()

			#if self.special_remove_U == False:
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()


		# for portal list
		go_to_portal_list = pygame.sprite.spritecollide(self, self.level.portal_list, True)
		for gate in go_to_portal_list:
			configsounds.portal_sfx.play()
		
		# for restore health
		restore_health_player = pygame.sprite.spritecollide(self, self.level.love_restore_health, True)
		for love_restore in restore_health_player:

			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.health_number += self.give_health
			
			total_health = self.health_number + self.give_health

			if total_health > 100:
				self.health_number = self.health_number - self.give_health
				
		
		# debugging purpose
		#print(self.health_number)
			
		
		# for death sprite
		you_die_in_hell = pygame.sprite.spritecollide(self, self.level.death_place_list, False)
		for water_suicide in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()
		
		for sharp_rock in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()
		
		for lava_water_suicide in you_die_in_hell:
			self.rect.y += 20
			if self.rect.bottom >= constants.SCREEN_HEIGHT or self.rect.bottom < 0:
				gameoverscreen.show_game_over()






		# FOR LEVEL 1 Hiragana Mode
		point1_hiragana_lv1 = pygame.sprite.spritecollide(self, self.level.hiragana_A, True)
		point2_hiragana_lv1 = pygame.sprite.spritecollide(self, self.level.hiragana_I, True)
		point3_hiragana_lv1 = pygame.sprite.spritecollide(self, self.level.hiragana_U, True)
		
		# If user get point hiragana A
		for true_point_lv1 in point1_hiragana_lv1:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_A = True
		
		# If user get point hiragana I
		for true_point_lv1 in point2_hiragana_lv1:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_I = True
		
		# If user get point hiragana U
		for false_point_lv1 in point3_hiragana_lv1:
			configsounds.denied_sfx.play()
			self.scores -= 100
			self.health_number -= self.false_point_dmg
			
			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		



		# FOR LEVEL 2 Hiragana Mode
		point1_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_A_lv2, True)
		point2_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_I_lv2, True)
		point3_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_U_lv2, True)
		point4_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_E, True)
		point5_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_O, True)
		
		point6_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_KA, True)
		point7_hiragana_lv2 = pygame.sprite.spritecollide(self, self.level.hiragana_KI, True)

		# If user get point hiragana U
		for true_point_lv2 in point3_hiragana_lv2:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_U_lv2 = True
		
		# If user get point hiragana I
		for true_point_lv2 in point2_hiragana_lv2:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_I_lv2 = True
		
		# If user get point hiragana O
		for true_point_lv2 in point5_hiragana_lv2:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_O = True
		
		# If user get point hiragana A
		for true_point_lv2 in point1_hiragana_lv2:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_A_lv2 = True
		
		# If user get point hiragana E
		for true_point_lv2 in point4_hiragana_lv2:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_E = True

		# If user get point hiragana KA
		for false_point_lv2 in point6_hiragana_lv2:
			configsounds.denied_sfx.play()
			self.scores -= 100
			self.health_number -= self.false_point_dmg

			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		
		# If user get point hiragana KI
		for false_point_lv2 in point7_hiragana_lv2:
			configsounds.denied_sfx.play()
			self.scores -= 100
			self.health_number -= self.false_point_dmg

			if self.health_number == 0 or self.health_number < 0:
				gameoverscreen.show_game_over()
		


		# FOR LEVEL 3 Hiragana Mode
		point1_hiragana_lv3 = pygame.sprite.spritecollide(self, self.level.hiragana_KA_lv3, True)
		point2_hiragana_lv3 = pygame.sprite.spritecollide(self, self.level.hiragana_KI_lv3, True)
		point3_hiragana_lv3 = pygame.sprite.spritecollide(self, self.level.hiragana_KU, True)
		point4_hiragana_lv3 = pygame.sprite.spritecollide(self, self.level.hiragana_KE, True)
		point5_hiragana_lv3 = pygame.sprite.spritecollide(self, self.level.hiragana_KO, True)

		# If user get point hiragana KA
		for true_point_lv3 in point1_hiragana_lv3:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_KA = True
		
		# If user get point hiragana KI
		for true_point_lv3 in point2_hiragana_lv3:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_KI = True
		
		# If user get point hiragana KU
		for true_point_lv3 in point3_hiragana_lv3:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_KU = True
		
		# If user get point hiragana KE
		for true_point_lv3 in point4_hiragana_lv3:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_KE = True
		
		# If user get point hiragana KO
		for true_point_lv3 in point5_hiragana_lv3:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_KO = True


		# For level 4 Hiragana Mode
		point1_hiragana_lv4 = pygame.sprite.spritecollide(self, self.level.hiragana_SA, True)
		point2_hiragana_lv4 = pygame.sprite.spritecollide(self, self.level.hiragana_SI, True)
		point3_hiragana_lv4 = pygame.sprite.spritecollide(self, self.level.hiragana_SU, True)
		point4_hiragana_lv4 = pygame.sprite.spritecollide(self, self.level.hiragana_SE, True)
		point5_hiragana_lv4 = pygame.sprite.spritecollide(self, self.level.hiragana_SO, True)


		# If user get point hiragana SA
		for true_point_lv4 in point1_hiragana_lv4:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_SA = True
		
		# If user get point hiragana SI
		for true_point_lv4 in point2_hiragana_lv4:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_SI = True
		
		# If user get point hiragana SU
		for true_point_lv4 in point3_hiragana_lv4:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_SU = True
		
		# If user get point hiragana SE
		for true_point_lv4 in point4_hiragana_lv4:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_SE = True
		
		# If user get point hiragana SO
		for true_point_lv4 in point5_hiragana_lv4:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_SO = True



		# For level 5 Hiragana Mode
		point1_hiragana_lv5 = pygame.sprite.spritecollide(self, self.level.hiragana_TA, True)
		point2_hiragana_lv5 = pygame.sprite.spritecollide(self, self.level.hiragana_TI, True)
		point3_hiragana_lv5 = pygame.sprite.spritecollide(self, self.level.hiragana_TU, True)
		point4_hiragana_lv5 = pygame.sprite.spritecollide(self, self.level.hiragana_TE, True)
		point5_hiragana_lv5 = pygame.sprite.spritecollide(self, self.level.hiragana_TO, True)
		

		# If user get point hiragana TA
		for true_point_lv5 in point1_hiragana_lv5:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_TA = True
		
		# If user get point hiragana TI
		for true_point_lv5 in point2_hiragana_lv5:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_TI = True
		
		# If user get point hiragana TU
		for true_point_lv5 in point3_hiragana_lv5:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_TU = True
		
		# If user get point hiragana Te
		for true_point_lv5 in point4_hiragana_lv5:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_TE = True
		
		# If user get point hiragana TO
		for true_point_lv5 in point5_hiragana_lv5:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_TO = True
		



		# For level 6 Hiragana Mode
		point1_hiragana_lv6 = pygame.sprite.spritecollide(self, self.level.hiragana_RA, True)
		point2_hiragana_lv6 = pygame.sprite.spritecollide(self, self.level.hiragana_RI, True)
		point3_hiragana_lv6 = pygame.sprite.spritecollide(self, self.level.hiragana_RU, True)
		point4_hiragana_lv6 = pygame.sprite.spritecollide(self, self.level.hiragana_RE, True)
		point5_hiragana_lv6 = pygame.sprite.spritecollide(self, self.level.hiragana_RO, True)


		# If user get point hiragana RA
		for true_point_lv6 in point1_hiragana_lv6:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_RA = True
		
		# If user get point hiragana RI
		for true_point_lv6 in point2_hiragana_lv6:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_RI = True
		
		# If user get point hiragana RU
		for true_point_lv6 in point3_hiragana_lv6:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_RU = True
		
		# If user get point hiragana Re
		for true_point_lv6 in point4_hiragana_lv6:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_RE = True
		
		# If user get point hiragana RO
		for true_point_lv6 in point5_hiragana_lv6:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_RO = True



		# For level 7 Hiragana Mode
		point1_hiragana_lv7 = pygame.sprite.spritecollide(self, self.level.hiragana_MA, True)
		point2_hiragana_lv7 = pygame.sprite.spritecollide(self, self.level.hiragana_MI, True)
		point3_hiragana_lv7 = pygame.sprite.spritecollide(self, self.level.hiragana_MU, True)
		point4_hiragana_lv7 = pygame.sprite.spritecollide(self, self.level.hiragana_ME, True)
		point5_hiragana_lv7 = pygame.sprite.spritecollide(self, self.level.hiragana_MO, True)


		# If user get point hiragana MA
		for true_point_lv7 in point1_hiragana_lv7:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_MA = True
		
		# If user get point hiragana MI
		for true_point_lv7 in point2_hiragana_lv7:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_MI = True
		
		# If user get point hiragana MU
		for true_point_lv7 in point3_hiragana_lv7:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_MU = True
		
		# If user get point hiragana Me
		for true_point_lv7 in point4_hiragana_lv7:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_ME = True
		
		# If user get point hiragana MO
		for true_point_lv7 in point5_hiragana_lv7:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_MO = True
		


		# For level 8 Hiragana Mode
		point1_hiragana_lv8 = pygame.sprite.spritecollide(self, self.level.hiragana_NA, True)
		point2_hiragana_lv8 = pygame.sprite.spritecollide(self, self.level.hiragana_NI, True)
		point3_hiragana_lv8 = pygame.sprite.spritecollide(self, self.level.hiragana_NU, True)
		point4_hiragana_lv8 = pygame.sprite.spritecollide(self, self.level.hiragana_NE, True)
		point5_hiragana_lv8 = pygame.sprite.spritecollide(self, self.level.hiragana_NO, True)


		# If user get point hiragana NA
		for true_point_lv8 in point1_hiragana_lv8:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_NA = True
		
		# If user get point hiragana NI
		for true_point_lv8 in point2_hiragana_lv8:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_NI = True
		
		# If user get point hiragana NU
		for true_point_lv8 in point3_hiragana_lv8:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_NU = True
		
		# If user get point hiragana NE
		for true_point_lv8 in point4_hiragana_lv8:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_NE = True
		
		# If user get point hiragana NO
		for true_point_lv8 in point5_hiragana_lv8:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_NO = True
		


		# For level 9 Hiragana Mode
		point1_hiragana_lv9 = pygame.sprite.spritecollide(self, self.level.hiragana_HA, True)
		point2_hiragana_lv9 = pygame.sprite.spritecollide(self, self.level.hiragana_HI, True)
		point3_hiragana_lv9 = pygame.sprite.spritecollide(self, self.level.hiragana_HU, True)
		point4_hiragana_lv9 = pygame.sprite.spritecollide(self, self.level.hiragana_HE, True)
		point5_hiragana_lv9 = pygame.sprite.spritecollide(self, self.level.hiragana_HO, True)


		# If user get point hiragana HA
		for true_point_lv9 in point1_hiragana_lv9:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_HA = True
		
		# If user get point hiragana HI
		for true_point_lv9 in point2_hiragana_lv9:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_HI = True
		
		# If user get point hiragana HU
		for true_point_lv9 in point3_hiragana_lv9:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_HU = True
		
		# If user get point hiragana HE
		for true_point_lv9 in point4_hiragana_lv9:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_HE = True
		
		# If user get point hiragana HO
		for true_point_lv9 in point5_hiragana_lv9:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_HO = True
		


		# For level 10 Hiragana Mode
		point1_hiragana_lv10 = pygame.sprite.spritecollide(self, self.level.hiragana_YA, True)
		point2_hiragana_lv10 = pygame.sprite.spritecollide(self, self.level.hiragana_YU, True)
		point3_hiragana_lv10 = pygame.sprite.spritecollide(self, self.level.hiragana_YO, True)
		
	
		# If user get point hiragana YA
		for true_point_lv10 in point1_hiragana_lv10:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_YA = True
		
		# If user get point hiragana YU
		for true_point_lv10 in point2_hiragana_lv10:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_YU = True
		
		# If user get point hiragana YO
		for true_point_lv10 in point3_hiragana_lv10:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_YO = True
		

		
		
		# For level 11 Hiragana Mode
		point1_hiragana_lv11 = pygame.sprite.spritecollide(self, self.level.hiragana_WA, True)
		point2_hiragana_lv11 = pygame.sprite.spritecollide(self, self.level.hiragana_WO, True)
		point3_hiragana_lv11 = pygame.sprite.spritecollide(self, self.level.hiragana_N, True)


		# If user get point hiragana WA
		for true_point_lv11 in point1_hiragana_lv11:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_WA = True
		
		# If user get point hiragana WO
		for true_point_lv11 in point2_hiragana_lv11:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_WO = True

		# If user get point hiragana N
		for true_point_lv11 in point3_hiragana_lv11:
			configsounds.coin_sfx.play()
			configsounds.coin_sfx.set_volume(0.5)
			self.scores += 100
			self.special_remove_N = True






		# debuing purpose
		#print(self.special_remove_U)

	def calc_grav(self):
		""" Calculate effect of gravity. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35

		# See if we are on the ground.
		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
	
	def jump(self):
		""" Called when user hits 'jump' button. """

		# move down a bit and see if there is a platform below us.
		# Move down 2 pixels because it doesn't work well if we only move down 1
		# when working with a platform moving down.
		
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		# If it is ok to jump, set our speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
			# play the sound
			configsounds.jump_sfx.play()
			self.change_y = -10
		
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -6
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 6
		self.direction = "R"

	def stop(self):
		""" Called when the user lets off the keyboard. """
		self.change_x = 0
	


# class for bullet
class Bullet(Player):
	""" This Class represent the bullet from player"""
	def __init__(self, player):
		super().__init__()

		self.image = pygame.Surface([4, 10])
		self.image.fill(constants.MAGIC_BULLET)

		self.rect = self.image.get_rect()

		self.bullet_list = pygame.sprite.Group()

		# access variable from player class
		self.direction = player.direction
		self.level = player.level
		
		# for special enemy
		# Basic Vocal
		self.special_remove_A = player.special_remove_A
		self.special_remove_I = player.special_remove_I
		self.special_remove_U = player.special_remove_U
		self.special_remove_E = player.special_remove_E
		self.special_remove_O = player.special_remove_O

		# for fix bugs
		self.special_remove_A_lv2 = player.special_remove_A_lv2
		self.special_remove_I_lv2 = player.special_remove_I_lv2
		self.special_remove_U_lv2 = player.special_remove_U_lv2

		# Vocal K
		self.special_remove_KA = player.special_remove_KA
		self.special_remove_KI = player.special_remove_KI
		self.special_remove_KU = player.special_remove_KU
		self.special_remove_KE = player.special_remove_KE
		self.special_remove_KO = player.special_remove_KO

		# Vocal S
		self.special_remove_SA = player.special_remove_SA
		self.special_remove_SI = player.special_remove_SI
		self.special_remove_SU = player.special_remove_SU
		self.special_remove_SE = player.special_remove_SE
		self.special_remove_SO = player.special_remove_SO

		# Vocal T
		self.special_remove_TA = player.special_remove_TA
		self.special_remove_TI = player.special_remove_TI
		self.special_remove_TU = player.special_remove_TU
		self.special_remove_TE = player.special_remove_TE
		self.special_remove_TO = player.special_remove_TO

		# Vocal N
		self.special_remove_NA = player.special_remove_NA
		self.special_remove_NI = player.special_remove_NI
		self.special_remove_NU = player.special_remove_NU
		self.special_remove_NE = player.special_remove_NE
		self.special_remove_NO = player.special_remove_NO

		# Vocal H
		self.special_remove_HA = player.special_remove_HA
		self.special_remove_HI = player.special_remove_HI
		self.special_remove_HU = player.special_remove_HU
		self.special_remove_HE = player.special_remove_HE
		self.special_remove_HO = player.special_remove_HO

		# Vocal M
		self.special_remove_MA = player.special_remove_MA
		self.special_remove_MI = player.special_remove_MI
		self.special_remove_MU = player.special_remove_MU
		self.special_remove_ME = player.special_remove_ME
		self.special_remove_MO = player.special_remove_MO

		# Vocal Y
		self.special_remove_YA = player.special_remove_YA
		self.special_remove_YU = player.special_remove_YU
		self.special_remove_YO = player.special_remove_YO

		# Vocal R
		self.special_remove_RA = player.special_remove_RA
		self.special_remove_RI = player.special_remove_RI
		self.special_remove_RU = player.special_remove_RU
		self.special_remove_RE = player.special_remove_RE
		self.special_remove_RO = player.special_remove_RO

		# Vocal W
		self.special_remove_WA = player.special_remove_WA
		self.special_remove_WO = player.special_remove_WO

		# Vocal N
		self.special_remove_N = player.special_remove_N
		
		self.kills = player.kills

	def update(self):
		""" move the bullet """
		if self.direction == "R":
			self.rect.x += 5
		#print(self.special_remove_A)
		#print(self.special_remove_I)
		elif self.direction == "L":
			self.rect.x -= 5

		# when hit enemy the bullet is gone
		hitting_enemy = pygame.sprite.spritecollide(self, self.level.enemy_list, True)

		for eaten in hitting_enemy:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		# just for special enemy list they are immune
		# if the player not get point mission enemy are immnune
		# for point mission symbol A
		if self.special_remove_A == False:
			hitting_special_enemy_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A, False)
		# if the player get point mission enemy are not immnune
		elif self.special_remove_A == True:
			hitting_special_enemy_A = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A, True)
		
		# for point mission symbol I
		if self.special_remove_I == False:
			hitting_special_enemy_I = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I, False)
		elif self.special_remove_I == True:
			hitting_special_enemy_I = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I, True)

		# for point mission symbol U
		if self.special_remove_U == False:
			hitting_special_enemy_U = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U, False)
		elif self.special_remove_U == True:
			hitting_special_enemy_U = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U, True)
		

		# for fix bugs
		if self.special_remove_A_lv2 == False:
			hitting_special_enemy_A_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A_lv2, False)
		# if the player get point mission enemy are not immnune
		elif self.special_remove_A_lv2 == True:
			hitting_special_enemy_A_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_A_lv2, True)
		
		# for point mission symbol I
		if self.special_remove_I_lv2 == False:
			hitting_special_enemy_I_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I_lv2, False)
		elif self.special_remove_I_lv2 == True:
			hitting_special_enemy_I_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_I_lv2, True)

		# for point mission symbol U
		if self.special_remove_U_lv2 == False:
			hitting_special_enemy_U_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U_lv2, False)
		elif self.special_remove_U_lv2 == True:
			hitting_special_enemy_U_lv2 = pygame.sprite.spritecollide(self, self.level.special_enemy_list_U_lv2, True)



		# for point mission symbol E
		if self.special_remove_E == False:
			hitting_special_enemy_E = pygame.sprite.spritecollide(self, self.level.special_enemy_list_E, False)
		elif self.special_remove_E == True:
			hitting_special_enemy_E = pygame.sprite.spritecollide(self, self.level.special_enemy_list_E, True)

		# for point mission symbol O
		if self.special_remove_O == False:
			hitting_special_enemy_O = pygame.sprite.spritecollide(self, self.level.special_enemy_list_O, False)
		elif self.special_remove_O == True:
			hitting_special_enemy_O = pygame.sprite.spritecollide(self, self.level.special_enemy_list_O, True)
		

		# for point mission symbol KA
		if self.special_remove_KA == False:
			hitting_special_enemy_KA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KA, False)
		elif self.special_remove_KA == True:
			hitting_special_enemy_KA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KA, True)
		
		# for point mission symbol KI
		if self.special_remove_KI == False:
			hitting_special_enemy_KI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KI, False)
		elif self.special_remove_KI == True:
			hitting_special_enemy_KI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KI, True)

		# for point mission symbol KI
		if self.special_remove_KU == False:
			hitting_special_enemy_KU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KU, False)
		elif self.special_remove_KU == True:
			hitting_special_enemy_KU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KU, True)

		# for point mission symbol KE
		if self.special_remove_KE == False:
			hitting_special_enemy_KE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KE, False)
		elif self.special_remove_KE == True:
			hitting_special_enemy_KE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KE, True)

		# for point mission symbol KO
		if self.special_remove_KO == False:
			hitting_special_enemy_KO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KO, False)
		elif self.special_remove_KO == True:
			hitting_special_enemy_KO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_KO, True)


		# for point mission symbol SA
		if self.special_remove_SA == False:
			hitting_special_enemy_SA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SA, False)
		elif self.special_remove_SA == True:
			hitting_special_enemy_SA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SA, True)
		
		# for point mission symbol SI
		if self.special_remove_SI == False:
			hitting_special_enemy_SI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SI, False)
		elif self.special_remove_SI == True:
			hitting_special_enemy_SI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SI, True)

		# for point mission symbol SI
		if self.special_remove_SU == False:
			hitting_special_enemy_SU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SU, False)
		elif self.special_remove_SU == True:
			hitting_special_enemy_SU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SU, True)

		# for point mission symbol SE
		if self.special_remove_SE == False:
			hitting_special_enemy_SE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SE, False)
		elif self.special_remove_SE == True:
			hitting_special_enemy_SE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SE, True)

		# for point mission symbol SO
		if self.special_remove_SO == False:
			hitting_special_enemy_SO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SO, False)
		elif self.special_remove_SO == True:
			hitting_special_enemy_SO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_SO, True)

		

		# for point mission symbol TA
		if self.special_remove_TA == False:
			hitting_special_enemy_TA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TA, False)
		elif self.special_remove_TA == True:
			hitting_special_enemy_TA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TA, True)
		
		# for point mission symbol TI
		if self.special_remove_TI == False:
			hitting_special_enemy_TI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TI, False)
		elif self.special_remove_TI == True:
			hitting_special_enemy_TI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TI, True)

		# for point mission symbol TI
		if self.special_remove_TU == False:
			hitting_special_enemy_TU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TU, False)
		elif self.special_remove_TU == True:
			hitting_special_enemy_TU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TU, True)

		# for point mission symbol TE
		if self.special_remove_TE == False:
			hitting_special_enemy_TE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TE, False)
		elif self.special_remove_TE == True:
			hitting_special_enemy_TE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TE, True)

		# for point mission symbol TO
		if self.special_remove_TO == False:
			hitting_special_enemy_TO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TO, False)
		elif self.special_remove_TO == True:
			hitting_special_enemy_TO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_TO, True)

		

		# for point mission symbol NA
		if self.special_remove_NA == False:
			hitting_special_enemy_NA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NA, False)
		elif self.special_remove_NA == True:
			hitting_special_enemy_NA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NA, True)
		
		# for point mission symbol NI
		if self.special_remove_NI == False:
			hitting_special_enemy_NI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NI, False)
		elif self.special_remove_NI == True:
			hitting_special_enemy_NI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NI, True)

		# for point mission symbol NU
		if self.special_remove_NU == False:
			hitting_special_enemy_NU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NU, False)
		elif self.special_remove_NU == True:
			hitting_special_enemy_NU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NU, True)

		# for point mission symbol NE
		if self.special_remove_NE == False:
			hitting_special_enemy_NE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NE, False)
		elif self.special_remove_NE == True:
			hitting_special_enemy_NE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NE, True)

		# for point mission symbol NO
		if self.special_remove_NO == False:
			hitting_special_enemy_NO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NO, False)
		elif self.special_remove_NO == True:
			hitting_special_enemy_NO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_NO, True)
		


		# for point mission symbol HA
		if self.special_remove_HA == False:
			hitting_special_enemy_HA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HA, False)
		elif self.special_remove_HA == True:
			hitting_special_enemy_HA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HA, True)
		
		# for point mission symbol HI
		if self.special_remove_HI == False:
			hitting_special_enemy_HI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HI, False)
		elif self.special_remove_HI == True:
			hitting_special_enemy_HI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HI, True)

		# for point mission symbol HU
		if self.special_remove_HU == False:
			hitting_special_enemy_HU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HU, False)
		elif self.special_remove_HU == True:
			hitting_special_enemy_HU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HU, True)

		# for point mission symbol HE
		if self.special_remove_HE == False:
			hitting_special_enemy_HE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HE, False)
		elif self.special_remove_HE == True:
			hitting_special_enemy_HE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HE, True)

		# for point mission symbol HO
		if self.special_remove_HO == False:
			hitting_special_enemy_HO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HO, False)
		elif self.special_remove_HO == True:
			hitting_special_enemy_HO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_HO, True)



		# for point mission symbol MA
		if self.special_remove_MA == False:
			hitting_special_enemy_MA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MA, False)
		elif self.special_remove_MA == True:
			hitting_special_enemy_MA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MA, True)
		
		# for point mission symbol MI
		if self.special_remove_MI == False:
			hitting_special_enemy_MI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MI, False)
		elif self.special_remove_MI == True:
			hitting_special_enemy_MI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MI, True)

		# for point mission symbol MI
		if self.special_remove_MU == False:
			hitting_special_enemy_MU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MU, False)
		elif self.special_remove_MU == True:
			hitting_special_enemy_MU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MU, True)

		# for point mission symbol ME
		if self.special_remove_ME == False:
			hitting_special_enemy_ME = pygame.sprite.spritecollide(self, self.level.special_enemy_list_ME, False)
		elif self.special_remove_ME == True:
			hitting_special_enemy_ME = pygame.sprite.spritecollide(self, self.level.special_enemy_list_ME, True)

		# for point mission symbol MO
		if self.special_remove_MO == False:
			hitting_special_enemy_MO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MO, False)
		elif self.special_remove_MO == True:
			hitting_special_enemy_MO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_MO, True)



		# for point mission symbol YA
		if self.special_remove_YA == False:
			hitting_special_enemy_YA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YA, False)
		elif self.special_remove_YA == True:
			hitting_special_enemy_YA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YA, True)
		
		# for point mission symbol YU
		if self.special_remove_YU == False:
			hitting_special_enemy_YU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YU, False)
		elif self.special_remove_YU == True:
			hitting_special_enemy_YU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YU, True)
		
		# for point mission symbol YO
		if self.special_remove_YO == False:
			hitting_special_enemy_YO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YO, False)
		elif self.special_remove_YO == True:
			hitting_special_enemy_YO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_YO, True)


		# for point mission symbol RA
		if self.special_remove_RA == False:
			hitting_special_enemy_RA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RA, False)
		elif self.special_remove_RA == True:
			hitting_special_enemy_RA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RA, True)
		
		# for point mission symbol RI
		if self.special_remove_RI == False:
			hitting_special_enemy_RI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RI, False)
		elif self.special_remove_RI == True:
			hitting_special_enemy_RI = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RI, True)

		# for point mission symbol RU
		if self.special_remove_RU == False:
			hitting_special_enemy_RU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RU, False)
		elif self.special_remove_RU == True:
			hitting_special_enemy_RU = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RU, True)

		# for point mission symbol RE
		if self.special_remove_RE == False:
			hitting_special_enemy_RE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RE, False)
		elif self.special_remove_RE == True:
			hitting_special_enemy_RE = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RE, True)

		# for point mission symbol RO
		if self.special_remove_RO == False:
			hitting_special_enemy_RO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RO, False)
		elif self.special_remove_RO == True:
			hitting_special_enemy_RO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_RO, True)


		# for point mision symbol WA
		if self.special_remove_WA == False:
			hitting_special_enemy_WA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WA, False)
		elif self.special_remove_WA == True:
			hitting_special_enemy_WA = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WA, True)
		
		# for point mission symbol WO
		if self.special_remove_WO == False:
			hitting_special_enemy_WO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WO, False)
		elif self.special_remove_WO == True:
			hitting_special_enemy_WO = pygame.sprite.spritecollide(self, self.level.special_enemy_list_WO, True)


		# for point mission symbol N
		if self.special_remove_N == False:
			hitting_special_enemy_N = pygame.sprite.spritecollide(self, self.level.special_enemy_list_N, False)
		elif self.special_remove_N == True:
			hitting_special_enemy_N = pygame.sprite.spritecollide(self, self.level.special_enemy_list_N, True)




		# for debugging purpose
		#print(self.special_remove_A)

		# attack a special enemy
		# Basic Vocal
		for special_eaten_A in hitting_special_enemy_A:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_I in hitting_special_enemy_I:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_U in hitting_special_enemy_U:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()


		# for fix bugs
		for special_eaten_A_lv2 in hitting_special_enemy_A_lv2:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_I_lv2 in hitting_special_enemy_I_lv2:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_U_lv2 in hitting_special_enemy_U_lv2:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()




		for special_eaten_E in hitting_special_enemy_E:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_O in hitting_special_enemy_O:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			


		# Vocal K
		for special_eaten_KA in hitting_special_enemy_KA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_KI in hitting_special_enemy_KI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_KU in hitting_special_enemy_KU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_KE in hitting_special_enemy_KE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_KO in hitting_special_enemy_KO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		


		# Vocal S
		for special_eaten_SA in hitting_special_enemy_SA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_SI in hitting_special_enemy_SI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_SU in hitting_special_enemy_SU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_SE in hitting_special_enemy_SE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_SO in hitting_special_enemy_SO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()



		# Vocal T
		for special_eaten_TA in hitting_special_enemy_TA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_TI in hitting_special_enemy_TI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_TU in hitting_special_enemy_TU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_TE in hitting_special_enemy_TE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_TO in hitting_special_enemy_TO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()




		# Vocal N
		for special_eaten_NA in hitting_special_enemy_NA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_NI in hitting_special_enemy_NI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_NU in hitting_special_enemy_NU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_NE in hitting_special_enemy_NE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_NO in hitting_special_enemy_NO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		


		# Vocal H
		for special_eaten_HO in hitting_special_enemy_HA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

		
		for special_eaten_HI in hitting_special_enemy_HI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_HU in hitting_special_enemy_HU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_HE in hitting_special_enemy_HE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_HO in hitting_special_enemy_HO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			


		# Vocal M
		for special_eaten_MA in hitting_special_enemy_MA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_MI in hitting_special_enemy_MI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_MU in hitting_special_enemy_MU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_ME in hitting_special_enemy_ME:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_MO in hitting_special_enemy_MO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		


		# Vocal Y
		for special_eaten_YA in hitting_special_enemy_YA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		

		for special_eaten_YU in hitting_special_enemy_YU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		

		for special_eaten_YO in hitting_special_enemy_YO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()



		# Vocal R
		for special_eaten_RA in hitting_special_enemy_RA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()

			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_RI in hitting_special_enemy_RI:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_RU in hitting_special_enemy_RU:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_RE in hitting_special_enemy_RE:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		
		for special_eaten_RO in hitting_special_enemy_RO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()




		# Vocal W
		for special_eaten_WA in hitting_special_enemy_WA:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
		


		for special_eaten_WO in hitting_special_enemy_WO:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()



		# Vocal N
		for special_eaten_N in hitting_special_enemy_N:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()
			
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
				configsounds.ouch_sfx.play()


		
		# when hit platform the bullet is gone
		hitting_platform = pygame.sprite.spritecollide(self, self.level.platform_list, False)

		for block in hitting_platform:
			if self.direction == "R":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
			elif self.direction == "L":
				pygame.sprite.spritecollide(self, self.bullet_list, True)
