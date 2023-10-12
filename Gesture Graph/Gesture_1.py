import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("../emgraw.csv")

num_channels = 8

channels = ['Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5', 'Channel 6', 'Channel 7', 'Channel 8']
x = np.arange(len(channels))
std_devs = []
rms_value = []

## 11450 ~ 13114

#gesture 1 by channel
for i in range(num_channels):
    standard_deviation = np.std(dataset.iloc[12000:12600, i+1])
    std_devs.append(standard_deviation)

for i in range(num_channels):
    rms = np.sqrt(np.mean(dataset.iloc[12000:12600, i+1]**2))
    rms_value.append(rms)

plt.bar(x, rms_value, yerr=std_devs, capsize=5, align='center', alpha=0.7)

#plt.errorbar(x, rms_value, yerr=std_devs, marker='o', ## 라인 마커
                 #color='k', ## 라인 색상
                 #ecolor='r', ## 에러 바 라인 색상
                 #elinewidth=1, ## 에러 바 라인 두께
                 #capsize=3, ## 에러 바 양끝 막대 길이
                 #capthick=2, ## 에러 바 양끝 막대 두께
            #)

plt.xticks(x, channels)
plt.xlabel('Channels')
plt.ylabel('RMS Value')
plt.title('RMS Values with Error Bars for EMG Channels')
plt.show()
