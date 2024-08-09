import numpy as np

traj1 = np.load("./output_gps-1.npy")
traj2 = np.load("./output_gps-2.npy")

trajs = np.concatenate((traj1, traj2), axis=0)
np.save("./output_gps.npy", trajs)
