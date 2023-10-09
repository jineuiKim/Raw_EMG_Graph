import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("../raw_EMG.csv")
print(dataset)

t = dataset.iloc[:,0]

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

y = dataset.iloc[:,-1].values

sampling_rate = 1000
num_channels = 8
plt.figure(figsize=(12,12))



for i in range(num_channels):
    plt.subplot(num_channels, 1 , i+1)
    plt.plot(t/1000, pd.DataFrame(dataset.iloc[:,i+1])*1000, color=colors[i])
    plt.title(f'Channel {i + 1}',loc='right', fontsize =10)
    plt.ylabel('Amplitude(uV)', fontsize = 7 )

plt.subplots_adjust(hspace=0.3)  # Adjust the value as needed
plt.xlabel('Time(s)')

plt.tight_layout
plt.show()


