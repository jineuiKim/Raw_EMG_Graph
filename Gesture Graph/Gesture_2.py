import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("../emgraw.csv")

num_channels = 8

channels = ['Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5', 'Channel 6', 'Channel 7', 'Channel 8']
x = np.arange(len(channels))
std_devs = []
rms_value = []

#gesture 1 by channel
for i in range(num_channels):
    standard_deviation = np.std(dataset.iloc[2600:3400, i+1])
    std_devs.append(standard_deviation)

for i in range(num_channels):
    rms = np.sqrt(np.mean(np.square((dataset.iloc[2600:3400, i+1]))))
    rms_value.append(rms)

plt.bar(x, rms_value, yerr=std_devs, capsize=5, align='center', alpha=0.7)

plt.xticks(x, channels)
plt.xlabel('Channels')
plt.ylabel('RMS Value')
plt.title('RMS Values with Error Bars for EMG Channels')
plt.show()
