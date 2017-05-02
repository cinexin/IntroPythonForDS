# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print (cars)
