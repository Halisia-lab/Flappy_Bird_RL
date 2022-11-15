import arcade

import tools
import pickle

import environment

class Agent:
    def __init__(self, env, alpha=1, gamma=0.3):
        self.__qtable = {}
        for state in env.states:
            self.__qtable[state] = {}
            for action in tools.ACTIONS:
                self.__qtable[state][action] = 0.0
        self.__env = env
        self.__alpha = alpha
        self.__gamma = gamma
        self.__history = []
        self.reset(False)
        self.texture = arcade.load_texture(tools.BIRD)

    def reset(self, store_history=True):
        if store_history:
            self.__history.append(self.__score)
        self.__state = self.__env.start
        self.__score = 0

    def best_action(self):
        q = self.__qtable[self.__state]
        return max(q, key=q.get)

    def step(self):

        action_all = self.best_action()
        state, reward = self.__env.do(self.__state, action_all)

        maxQ = max(self.__qtable[state].values())
        delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qtable[self.__state][action_all])
        self.__qtable[self.__state][action_all] += delta

        self.__state = state
        self.__score += reward

        return action_all, reward

    @property
    def state(self):
        return self.__state

    @property
    def score(self):
        return self.__score

    @property
    def environment(self):
        return self.__env

    @property
    def history(self):
        return self.__history

    def load(self, filename):
        with open(filename, 'rb') as file:
            self.__qtable, self.__history = pickle.load(file)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.__qtable, self.__history), file)

    def __repr__(self):
        res = f'Agent {agent.state}\n'
        res += str(self.__qtable)
        return res