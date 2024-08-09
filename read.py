import numpy as np

trajs = np.load("./output_gps.npy")

print(len(trajs))  # ideally output 50000

print(trajs[:10])
