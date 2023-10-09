import numpy as np
import matplotlib.pyplot as plt

# Sample data
rms_values = [10, 15, 8, 12]  # Replace with your RMS values
std_devs = [1, 1.5, 0.8, 1.2]  # Replace with your standard deviations

# Variables (e.g., channels)
variables = ['Channel 1', 'Channel 2', 'Channel 3', 'Channel 4']

# Create an array of x values for the bars
x = np.arange(len(variables))
print(x)
# Create a bar graph with error bars
plt.bar(x, rms_values, yerr=std_devs, capsize=5, align='center', alpha=0.7)

# Set x-axis labels and title
plt.xticks(x, variables)
plt.xlabel('Channels')
plt.ylabel('RMS Value')
plt.title('RMS Values with Error Bars for EMG Channels')

# Show the plot
plt.show()
