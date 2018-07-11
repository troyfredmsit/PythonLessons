#new text based RPG tutorial

#IMPORTS
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100
screen_height = 100


#### Player Setup ####
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = 'start'




myplayer = player()
#### Title Screen ####

def title_screen_selection():
	answer = input('enter an option here --> ')
	print("this is the option right after")
	if answer.lower() == ("play"):
		start_game() # TODO
	elif answer.lower() == ("help"):
		help_menu() #TODO
	elif answer.lower() == ("quit"):
		sys.exit()
	while answer.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command")
		answer = input("--> ")
		if answer.lower() == "play":
			start_game() # TODO
		elif answer.lower() == "help":
			help_menu() #TODO
		elif answer.lower() == "quit":
			sys.exit()

def title_screen():
	os.system('clear')
	print('###########################')
	print('# Welcome to the text RPG #')
	print('###########################')
	print('#           PLAY          #')
	print('#           HELP          #')
	print('#           QUIT          #')
	print('###########################')
	title_screen_selection()

def help_menu():
	print("help menu")
	title_screen_selection()

#### Game interaction ####
def print_location():
	print('\n' + ('#' *(4 + len(myplayer.location))))
	print('#' + myplayer.location.upper() + '#')
	print('#' + zonemap[myplayer.position][DESCRIPTION]+ '#')
	print('\n' + ('#' *(4 + len(myplayer.location))))

def prompt():
	print('\n' + "================================")
	print("What would you like to do?")
	action = input("--->")
	acceptable_actions = ['move','go','travel','walk', 'quit','examine','inspect','interact','look']
	while action.lower() not in acceptable_actions:
		print("unknown action try again")
		action = input("-->>")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move','go','travel','walk']:
		 player_move(action.lower())
	elif action.lower() in ['examine','inspect','interact','look']
		player_examine(action.lower())

def player_move(myaction):
	print('Where would you like to move to?\n')
	dest = input(ask)
	if dest in ['up','north']:
	elif dest in ['down','south']:
	elif dest in ['right','east']:
	elif dest in ['left','west']:
#### Game Items ####
def start_game():
	print("Game woot!")

"""MAP
A1 - A4
D1 - D4 in rectangle
"""
ZONENAME = ''
DESCRIPTION = 'descrption'
EXAMINE = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False
				 'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False
				 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False
				 'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False
				 }
zonemap = {
	'a1': {
	ZONENAME = 'A1',
	DESCRIPTION = 'Area A1',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a1',
	DOWN = 'b2',
	LEFT = 'a1',
	RIGHT = 'a2'
	},
	'b1': {
	ZONENAME = 'B1',
	DESCRIPTION = 'Area B1',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a1',
	DOWN = 'c1',
	LEFT = 'b1',
	RIGHT = 'b2'
	},
	'c1': {
	ZONENAME = 'C1',
	DESCRIPTION = 'Area C1',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'b1',
	DOWN = 'd1',
	LEFT = 'c1',
	RIGHT = 'c2'
	},
	'd1': {
	ZONENAME = 'D1',
	DESCRIPTION = 'Area D1',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'c1',
	DOWN = 'd1',
	LEFT = 'd1',
	RIGHT = 'd2'
	},
	'a2': {
	ZONENAME = 'A2',
	DESCRIPTION = 'Area A2',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a2',
	DOWN = 'b2',
	LEFT = 'a1',
	RIGHT = 'a3'
	},
	'b2': {
	ZONENAME = 'B2',
	DESCRIPTION = 'Area B2',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a2',
	DOWN = 'c2',
	LEFT = 'b1',
	RIGHT = 'b3'
	},
	'c2': {
	ZONENAME = 'C2',
	DESCRIPTION = 'Area C2',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'b2',
	DOWN = 'd2',
	LEFT = 'c1',
	RIGHT = 'c4'
	},
	'd2': {
	ZONENAME = 'D2',
	DESCRIPTION = 'Area D2',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'c2',
	DOWN = 'd2',
	LEFT = 'd1',
	RIGHT = 'd3'
	},
	'a3': {
	ZONENAME = 'A3',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a3',
	DOWN = 'b3,
	LEFT = 'a2,
	RIGHT = 'a4'
	},
	'b3': {
	ZONENAME = 'B3',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a3',
	DOWN = 'c3',
	LEFT = 'b2',
	RIGHT = 'b4'
	},
	'c3': {
	ZONENAME = 'C3',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'b3',
	DOWN = 'd3',
	LEFT = 'c2',
	RIGHT = 'c4'
	},
	'd3': {
	ZONENAME = 'D3'
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'c3',
	DOWN = 'd3',
	LEFT = 'd2',
	RIGHT = 'd4'
	},
	'a4': {
	ZONENAME = 'A4',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a4',
	DOWN = 'b4',
	LEFT = 'a3',
	RIGHT = 'a4'
	},
	'b4': {
	ZONENAME = 'B4',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'a4',
	DOWN = 'c4',
	LEFT = 'b3',
	RIGHT = 'b4'
	},
	'c4': {
	ZONENAME = 'C4',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'b4',
	DOWN = 'd4',
	LEFT = 'c3',
	RIGHT = 'c4'
	},
	'd4': {
	ZONENAME = 'D4',
	DESCRIPTION = 'descrpti',
	EXAMINE = 'examine',
	SOLVED = False,
	UP = 'c4',
	DOWN = 'd4',
	LEFT = 'd3',
	RIGHT = 'd4'
	}
}
title_screen()
