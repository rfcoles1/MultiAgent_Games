import numpy as np
import gym
import gym.spaces 
from Bees_Engine import BeeEngine

class BeeEnv(gym.Env):
    def __init__(self):
        self.engine = BeeEngine()

        self.actions = {0: self.engine.move_left,
                        1: self.engine.move_right,
                        2: self.engine.move_down,
                        3: self.engine.move_up,
                        4: self.engine.no_move}

        self.action_space = gym.spaces.Discrete(5)

        #each bee contributes a step every timestep
        self.max_steps = 50*self.engine.num_bees

    def reset(self):
        self.done = False
        self.engine.reset()
        self.steps = 0
        return self.get_state(0)

    def get_state(self, beeID):
        state = self.engine.get_state(beeID)
        state[:,0] = state[:,0]/float(self.engine.xmax)
        state[:,1] = state[:,1]/float(self.engine.ymax)
        return state

    def step(self,a, beeID): 
        self.actions[a](beeID)
        self.engine.check_bee_pos(beeID)
        next_state = self.get_state(beeID)
        reward = np.sum(self.engine.bee_food) 
            
        self.steps += 1
        if self.steps > self.max_steps:
            self.done = True
        return next_state, reward, self.done, {}

    def render(self):
        return 0 
