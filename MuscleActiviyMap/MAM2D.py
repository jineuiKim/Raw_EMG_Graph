import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("../emgraw.csv")

num_channels = 4

std_devs = []
rms_value = []

## gesture 1 by channel
for i in range(num_channels):
    standard_deviation = np.std(dataset.iloc[9900:10800, i+1])
    std_devs.append(standard_deviation)

for i in range(num_channels):
    rms = np.sqrt(np.mean(dataset.iloc[9900:10800, i+1]**2))
    rms_value.append(rms)
print(rms_value)
rms_matrix = np.array(rms_value).reshape(1, num_channels)
plt.figure(figsize=(8, 8))
plt.imshow(rms_matrix, cmap='jet', interpolation='sinc', aspect='auto')
plt.grid(False)
plt.colorbar()

plt.show()