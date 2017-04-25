baseball = [
    [  7.40000000e+04,   1.80000000e+02,   2.29900000e+01],
    [  7.40000000e+01,   2.15000000e+02,   3.46900000e+01],
    [  7.20000000e+01,   2.10000000e+02,   3.07800000e+01],
    [  7.50000000e+01,   2.05000000e+02,   2.51900000e+01],
    [  7.50000000e+01,   1.90000000e+02,   3.10100000e+01],
    [  7.30000000e+01,   1.95000000e+02,   2.79200000e+01]
            ]

# Import numpy
import numpy as np

np_baseball = np.array(baseball)

# Create np_height from np_baseball
np_height = np_baseball[:,0]

print (np_height)

# Print out the mean of np_height
print (np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
