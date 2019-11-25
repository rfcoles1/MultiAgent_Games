import numpy as np
import matplotlib.pyplot as plt

class BeeEngine(object):
    def __init__(self):
        self.xmax = 10
        self.ymax = 10
        self.increment = 1
        
        self.num_bees = 2
        self.num_flowers = 2
        
        self.reset()
  
    def reset(self):
        self.gen_bees() 
        self.gen_flowers()
        self.bee_food = 0

    def get_state(self, beeID): 
        controlled_bee = self.bee_position[beeID]
        flower_state = self.flower_position

        if self.num_bees > 1:
            other_bees = self.bee_position[np.arange(self.num_bees) != beeID][0]
        
            state = np.vstack([controlled_bee, other_bees, self.flower_position, self.flower_food])
            return state
        else:
            state = np.vstack([controlled_bee, self.flower_position])
            return state

    def gen_flowers(self):
        self.flower_position = np.reshape(np.random.randint(0,self.xmax,2*self.num_flowers), [1,self.num_flowers,2])[0]
        self.flower_food = np.ones(self.num_flowers)

    def gen_bees(self):
        self.bee_position = np.reshape(np.random.randint(0,self.xmax,2*self.num_bees), [1,self.num_bees,2])[0]

    def move_left(self, i):
        if self.bee_position[i][0] > 0:
            self.bee_position[i][0] -= self.increment

    def move_right(self, i):
        if self.bee_position[i][0] < self.xmax - 1:
            self.bee_position[i][0] += self.increment

    def move_down(self, i):
        if self.bee_position[i][1] > 0:
            self.bee_position[i][1] -= self.increment

    def move_up(self, i):    
        if self.bee_position[i][1] < self.ymax - 1:
            self.bee_position[i][1] += self.increment
       
    def no_move(self, i):
        return

    def check_bee_pos(self, beeID):
        for i in range(self.num_flowers):
            if np.array_equal(self.bee_position[beeID], self.flower_position[i]):
                if self.flower_food[i] > 0:
                    self.bee_food += 1
                    self.flower_food[i] -= 1
    
        if sum(self.flower_food) < 1:
            self.gen_flowers()

    def display(self):
        state = np.zeros([self.xmax, self.ymax])
        state[self.bee_position[:,0], self.bee_position[:,1]] = 1
        state[self.flower_position[:,0], self.flower_position[:,1]] = 2

        rgbarray = np.vstack([[1,1,1], [1,1,0], [0.5,0,0.5]])
        cmap = mcolors.ListedColormap(rgbarray)
        plt.imshow(state.T, origin = 'lower', cmap=cmap)
        plt.show()
