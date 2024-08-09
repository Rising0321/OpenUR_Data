# Regenerated Data for KDD 2025 Submission

Due to the space limit of github, we divide the data into two parts as output_gps-1.npy and output_gps-2.npy. You can
use merge.py first to generate the output_gps.npy.

The output_gps.npy is the 50k regenerated data. It has the shape of (50000, 96, 2). The first dimension is the number of
samples, the second dimension is the number of time steps, and the third dimension is the number of features. The first
feature is the latitude and the second feature is the longitude.

You can use read.py to see this data.