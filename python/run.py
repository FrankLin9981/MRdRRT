#!/usr/bin/env python

import numpy as np

# from simple_robot import SimpleRobot
from simple_environment import SimpleEnvironment
from prm_planner import PRMPlanner
from mrdrrt_planner import MRdRRTPlanner

# assert 1>5, "it works!" TODO add these throughout code

map_id = 2
test = 4

def main():
    print("Starting...")
    # Map IDs: 1=cube center, 2=T
    prm = PRMPlanner(n_nodes=1000, map_id=map_id, load=False, visualize=True, filepath=None)

    # TODO: Change start and goal configs for new map (3, 4 already corrected)
    if test == 1:
        # Test 1 robot in cube map
        sconfigs = np.array([[0, -30]])
        gconfigs = np.array([[30, 0]])

    if test == 2:
        # Test 2 robots in cube map
        sconfigs = np.array([[0, 30], [-40, -30]])
        gconfigs = np.array([[40, -30], [0, 20]])

    if test == 3:
        # Test 2 robots in T map
        sconfigs = np.array([[-25, -7.5], [25, -7.5]])
        gconfigs = np.array([[25, -7.5], [-25, -7.5]])

    if test == 4:
        # Test 3 robots in T map
        sconfigs = np.array([[-25, -7.5], [25, -7.5], [0, 25]])
        gconfigs = np.array([[25, -7.5], [0, 25], [-25, -7.5]])

    if test == 5:
        # Test 4 robots in T map
        sconfigs = np.array([[-25, -35], [5, -30], [0, 0], [20, -35]])
        gconfigs = np.array([[5, 30], [15, 35], [40, -35], [-20, -38]])

    if test == 6:
        # Test 5 robots in T map
        sconfigs = np.array([[-40, -35], [5, -30], [0, 0], [20, -35], [35, -30]])
        gconfigs = np.array([[5, 30], [15, 35], [40, -35], [-20, -38], [-5, 45]])

    mrdrrt = MRdRRTPlanner(prm, n_robots=sconfigs.shape[0], visualize=True)
    path = mrdrrt.FindPath(sconfigs, gconfigs)

if __name__ == "__main__":
    main()

    # import IPython
    # IPython.embed()
