#! /usr/bin/env python
__author__ = 'frankhe'

"""
Execute DQN or Episodic control

"""

import launcher
import sys


class Defaults:
    # ----------------------
    # Experiment Parameters
    # ----------------------
    STEPS_PER_EPOCH = 10000
    EPOCHS = 5000
    STEPS_PER_TEST = 0

    # ----------------------
    # ALE Parameters
    # ----------------------
    BASE_ROM_PATH = "../roms/"
    ROM = 'ms_pacman.bin'
    FRAME_SKIP = 4
    REPEAT_ACTION_PROBABILITY = 0

    # ----------------------
    # Agent/Network parameters:
    # ----------------------
    UPDATE_RULE = 'deepmind_rmsprop'
    BATCH_ACCUMULATOR = 'sum'
    LEARNING_RATE = .00025
    DISCOUNT = .99
    RMS_DECAY = .95 # (Rho)
    RMS_EPSILON = .01
    MOMENTUM = 0 # Note that the "momentum" value mentioned in the Nature
                 # paper is not used in the same way as a traditional momentum
                 # term.  It is used to track gradient for the purpose of
                 # estimating the standard deviation. This package uses
                 # rho/RMS_DECAY to track both the history of the gradient
                 # and the squared gradient.
    CLIP_DELTA = 1.0
    EPSILON_START = 1.0
    EPSILON_MIN = .005
    EPSILON_DECAY = 10000
    PHI_LENGTH = 4
    UPDATE_FREQUENCY = 4
    REPLAY_MEMORY_SIZE = 1000000
    BATCH_SIZE = 32
    NETWORK_TYPE = "nature_dnn"
    FREEZE_INTERVAL = 10000
    REPLAY_START_SIZE = 50000
    RESIZE_METHOD = 'scale'
    RESIZED_WIDTH = 84
    RESIZED_HEIGHT = 84
    DEATH_ENDS_EPISODE = 'true'
    MAX_START_NULLOPS = 30
    DETERMINISTIC = True
    CUDNN_DETERMINISTIC = False

    DQN = False
    EPISODIC_CONTROL = True
    K_NEAREST_NEIGHBOR = 11
    EC_DISCOUNT = 1.0
    BUFFER_SIZE = 1000000
    REBUILD_KNN_FREQUENCY = 1000000/3
    N_TREES = 20
    SEARCH_K = 100000
    DIMENSION_OF_STATE = 64
    PROJECTION_TYPE = 'random'  # or VAE
    TESTING = False

if __name__ == "__main__":
    launcher.launch(sys.argv[1:], Defaults, __doc__)
