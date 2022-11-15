import tools
import arcade

import wall


class Environment:
    def __init__(self):
        row = 0
        col = 0
        self.__states = {}

        for i in range(288):
            for j in range(512):
                self.__states[i, j] = (i, j)

        self.__start = (50, 256)
        self.__reward_goal = 10


        self.__reward_wall_passed = len(self.__states)
        self.__reward_wall_crashed = -2 * self.__reward_goal
        self.__reward_ground = -3 * self.__reward_goal
        self.__reward_ceiling = -3 * self.__reward_goal

    def do(self, state, action):

        move = tools.ACTION_MOVE[action]
        new_state = (state[0] + move[0], state[1] + move[1])

        # check ground + sky

        if new_state not in self.__states:
            reward = self.__reward_wall_crashed

            # if new_state not in self.states \
            #         or self.__states[new_state] in [tools.MAP_WALL, tools.MAP_GROUND]:
            #     move = tools.ACTION_MOVE[tools.ACTION_DOWN]
            #     reward = -4000

            # if new_state != self.__goal:
            #     move = tools.ACTION_MOVE[tools.ACTION_RIGHT]
            # new_state = (state[0] + move[0], state[1] + move[1])
        else:
            state = new_state
            # if new_state == self.__goal:
            #     reward = self.__reward_goal
            # else:
            reward = tools.REWARD_DEFAULT

        return state, reward

    @property
    def states(self):
        return list(self.__states.keys())

    @property
    def start(self):
        return self.__start

    @property
    def goal(self):
        return self.__reward_goal



