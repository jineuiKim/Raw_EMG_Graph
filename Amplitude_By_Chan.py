import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("emgraw.csv")


t = dataset.iloc[:,0]
g = dataset.iloc[:,-1]
prev_number = None
prev_count = 0

count = 0
#gesture 1 by channel
g1 = dataset.iloc[500:1600,1]
g1_avg = abs(g1.mean())
g2 = dataset.iloc[500:1600,2]
g2_Avg = abs(g2.mean())
g3 = dataset.iloc[500:1600,3]
g3_Avg = abs(g3.mean())
g4 = dataset.iloc[500:1600,4]
g4_Avg = abs(g4.mean())
g5 = dataset.iloc[500:1600,5]
g5_avg = abs(g5.mean())
g6 = dataset.iloc[500:1600,6]
g6_Avg = abs(g6.mean())
g7 = dataset.iloc[500:1600,7]
g7_Avg = abs(g7.mean())
g8 = dataset.iloc[500:1600,8]
g8_Avg = abs(g8.mean())


variables = ['C1', 'C2', 'C3', 'C4', 'C5','C6','C7', 'C8']
amplitude = [g1_avg, g2_Avg, g3_Avg, g4_Avg, g5_avg, g6_Avg, g7_Avg, g8_Avg ]

plt.bar(variables, amplitude)

plt.xlabel('Variables')
plt.ylabel('Amplitude')
plt.title('Gesture 1')

# Show the plot
plt.show()


