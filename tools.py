import os

ENV0 = """
#########################################
                                        #
                                        #
      #####         #####               #
.              £             #####      *
#########################################
"""

ENV1 = """
########################################
         #              #              #
         #              #              #
         #              #              #
         #     #        #       #      #         
               #                #      #
               #                #      #
.              #                #      *
########################################
"""

ENV = """
#########################################
         #               #              #
         #               #              #
         #               #              #
         #     #         #       #      #         
               #                 #      #
               #                 #      #
.              #                 #      *
%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%#%%%%%%%
"""
MAP_WALL = '#'
MAP_START = '.'
MAP_GOAL = '*'
MAP_GROUND = '%'
REWARD_DEFAULT = -1
ACTION_UP = 'U'
ACTION_DOWN = 'D'
NO_ACTION = '/'
ACTIONS = [ACTION_UP, NO_ACTION]

ACTION_MOVE = {ACTION_UP: (16, 0),
               NO_ACTION: (-1, 0)
 }

SPRITE_SCALE = 0.25
SPRITE_SIZE = round(128 * SPRITE_SCALE)

FILE_AGENT = 'agent.txt'

SCREENWIDTH  = 288
SCREENHEIGHT = 512
BASEY = SCREENHEIGHT * 0.79

PIPES = ["images" + os.sep + "pipe-green.png"]
BACKGROUND = "images" + os.sep + "game_background.png"
GROUND = "images" + os.sep + "game_ground.png"
BIRD = "images" + os.sep + "yellow_bird.png"
WALL_GAPS = [120, 140, 90]
