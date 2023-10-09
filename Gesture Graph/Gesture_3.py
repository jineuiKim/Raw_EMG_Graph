import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("../emgraw.csv")


t = dataset.iloc[:,0]
g = dataset.iloc[:,-1]
prev_number = None
prev_count = 0

count = 0
#gesture 1 by channel
c1 = dataset.iloc[4400:5300,1]
c1_avg = np.sqrt(np.mean(c1**2))
c2 = dataset.iloc[4400:5300,2]
c2_Avg = np.sqrt(np.mean(c2**2))
c3 = dataset.iloc[4400:5300,3]
c3_Avg = np.sqrt(np.mean(c3**2))
c4 = dataset.iloc[4400:5300,4]
c4_Avg = np.sqrt(np.mean(c4**2))
c5 = dataset.iloc[4400:5300,5]
c5_avg = np.sqrt(np.mean(c5**2))
c6 = dataset.iloc[4400:5300,6]
c6_Avg = np.sqrt(np.mean(c6**2))
c7 = dataset.iloc[4400:5300,7]
c7_Avg = np.sqrt(np.mean(c7**2))
c8 = dataset.iloc[4400:5300,8]
c8_Avg = np.sqrt(np.mean(c8**2))


variables = ['C1', 'C2', 'C3', 'C4', 'C5','C6','C7', 'C8']
amplitude = [c1_avg, c2_Avg, c3_Avg, c4_Avg, c5_avg, c6_Avg, c7_Avg, c8_Avg ]

plt.bar(variables, amplitude)

plt.xlabel('Channel')
plt.ylabel('Amplitude')
plt.title('Gesture 3')

# Show the plot
plt.show()
