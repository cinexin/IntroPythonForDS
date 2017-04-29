# heights and positions are available as lists
heights = [191,
 184,
 185,
 180,
 181,
 187,
 170,
 179,
 183,
 186
]
positions = ['GK',
 'M',
 'A',
 'D',
 'M',
 'D',
 'M',
 'M',
 'M',
 'A',
]


# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights = np.array(heights)
np_positions = np.array(positions)


# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

non_gk_heights = np_heights[np_positions != 'GK']
# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(non_gk_heights)))