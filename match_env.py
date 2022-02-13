import gym
import numpy as np
from gym import spaces, error
from gym import utils
from gym.utils import seeding



class MatchEnv(gym.Env):
    def __init__(self,
                 mtwl=10):
        self.mtwl = mtwl
        self.action_spaces = n