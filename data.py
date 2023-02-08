

import pandas as pd 

# Create a dataframe with 3 columns 
data = {'Feature1':[1, 2, 3, 4, 5], 'Feature2':[6, 7, 8, 9, 10], 'Feature3':[11, 12, 13, 14 ,15]} 
df = pd.DataFrame(data) 
  
# Export the dataframe to csv file 
df.to_csv('dataset.csv', index=False)
