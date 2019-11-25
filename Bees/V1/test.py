import numpy as np
import matplotlib.pyplot as plt
from Bees_Environment import BeeEnv

E = BeeEnv()

def print_status():
    print 'Food Stores: ' + str([E.engine.hive_food, E.engine.flower_food, E.engine.bee_food])

def plot():
    E.engine.display()
