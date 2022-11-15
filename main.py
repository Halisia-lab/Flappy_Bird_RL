import arcade

import tools
import environment
import agent
import window
import time
import matplotlib.pyplot as plt



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    env = environment.Environment(tools.ENV)
    print(f'Number of states {len(env.states) * 4}')
    agent = agent.Agent(env)

    print(agent.state)

    window = window.Window(agent)
    window.setup()
    arcade.run()

    history = []
    for epoch in range(100):
        iteration = 0
        agent.reset()
        while agent.state != env.goal:
            action, reward = agent.step()
            iteration += 1

        history.append(agent.score)
        print(iteration, agent.score)

    plt.plot(history)
    plt.show()

"""
    agent.reset()
    
    while agent.state != env.goal:
       action, reward = agent.step()
       env.print(agent)
       time.sleep(0.03)
"""

