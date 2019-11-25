import numpy as np
import gym
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import os
import sys
sys.path.insert(0,'../../../')
import MultiAgent_Games

sys.path.insert(0,'../../../MultiAgent_GA')
from GA_Config import Config
from GA_Network import Network

config = Config()
config.num_layers = 2
config.num_hidden = 128
config.env_name = 'Bees-v1'
config.a_size = 5

network = Network(config)
weights = np.load('./models/Bees-v1_22/22800.npz')
network.w_in = weights['w_in']
network.w_hidden = weights['w_h']
network.w_out = weights['w_out']

env = gym.make(config.env_name).unwrapped
env.engine.num_bees = 2
env.engine.num_flowers = 2 
s = env.reset()

def plt_model(ind, s, r):
   
    state = np.zeros([env.unwrapped.engine.xmax, env.unwrapped.engine.ymax])
    state[env.unwrapped.engine.bee_position[:,0], env.unwrapped.engine.bee_position[:,1]] = 1
    state[env.unwrapped.engine.flower_position[:,0], env.unwrapped.engine.flower_position[:,1]] = 2
     
    rgbarray = np.vstack([[1,1,1], [1,1,0], [0.5,0,0.5]])
    cmap = mcolors.ListedColormap(rgbarray)
    plt.imshow(state.T, origin = 'lower', cmap=cmap)
    
    plt.tight_layout()
    fname = '__trainingvid%05d.png'%(ind)
    plt.savefig(fname, dpi = 150)
    plt.clf()

i=0
while i < 50:
    s0 = env.get_state(0)
    a0 = network.predict(s0.flatten())
    a0 = np.argmax(a0)
    _, reward, done, _, = env.step(a0,0)

    

    s1 = env.get_state(1)
    a1 = network.predict(s1.flatten())
    a1 = np.argmax(a1)
    _, reward, done, _, = env.step(a1,1)

    plt_model(i,s1,reward)
    print(i,s1,reward)
    i += 1

vidname = 'learner' + '0' + '.mp4'
os.system('ffmpeg -r 10 -i __trainingvid%05d.png -vcodec mpeg4 -y ' + str(vidname))
for i in range(0,i):
    os.remove('__trainingvid%05d.png'%(i))


