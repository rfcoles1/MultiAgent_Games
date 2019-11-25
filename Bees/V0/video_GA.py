import numpy as np
import gym
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from Tkinter import *

import os
import sys
sys.path.insert(0,'../../../')
import MultiAgent_Games

sys.path.insert(0,'../../../Genetic_Algorithms')
from GA_Config import Config
from GA_Network import Network

config = Config()
config.num_layers = 2
config.num_hidden = 128
config.env_name = 'Bees-v0'
config.a_size = 5

network = Network(config)
weights = np.load('./models/Bees-v0/1750.npz')
network.w_in = weights['w_in']
network.w_hidden = weights['w_h']
network.w_out = weights['w_out']

env = gym.make(config.env_name)

s = env.reset()

def plt_model(ind, s, r):
   
    state = np.zeros([env.unwrapped.engine.xmax, env.unwrapped.engine.ymax])
    state[env.unwrapped.engine.bee_position[:,0], env.unwrapped.engine.bee_position[:,1]] = 1
    state[env.unwrapped.engine.flower_position[:,0], env.unwrapped.engine.flower_position[:,1]] = 2
    state[env.unwrapped.engine.hive_position[0], env.unwrapped.engine.hive_position[1]] = 3
     
    rgbarray = np.vstack([[1,1,1], [1,1,0], [0.5,0,0.5], [1,0.5,0]])
    cmap = mcolors.ListedColormap(rgbarray)
    plt.imshow(state.T, origin = 'lower', cmap=cmap)
    
    plt.tight_layout()
    fname = '__trainingvid%05d.png'%(ind)
    plt.savefig(fname, dpi = 150)
    plt.clf()

i=0
while True:
    a = network.predict(s.flatten())
    a = np.argmax(a)
    s, reward, done, _, = env.step(a)

    plt_model(i,s,reward)
    print(i, a, s, reward)
    i += 1
    if done:
        break

vidname = 'learner' + '0' + '.mp4'
os.system('ffmpeg -r 10 -i __trainingvid%05d.png -vcodec mpeg4 -y ' + str(vidname))
for i in range(0,i):
    os.remove('__trainingvid%05d.png'%(i))


