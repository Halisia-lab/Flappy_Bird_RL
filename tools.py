import os


REWARD_DEFAULT = -1
ACTION_UP = 'U'
NO_ACTION = '/'
ACTIONS = [ACTION_UP, NO_ACTION]

ACTION_MOVE = {ACTION_UP: (0, 16),
               NO_ACTION: (0, -1)
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
