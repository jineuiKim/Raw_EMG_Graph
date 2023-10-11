import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your EMG data from a CSV file
dataset = pd.read_csv("../emgraw.csv")

# Number of channels (assuming 8 channels)
num_channels = 8

# Set the figure size
plt.figure(figsize=(12, 12))

max_y = np.max(np.abs(dataset.iloc[2600:3400, 1:num_channels + 1].values))
# Create a 4x4 grid of subplots for each channel
for i in range(num_channels):
    plt.subplot(2, 4, i + 1)

    # Extract data for the current channel and take the absolute values
    channel_data = np.abs(dataset.iloc[8100:9000, i + 1].values) * 1000

    # Create a histogram-like plot
    plt.hist(channel_data, bins=100, color='b', alpha=0.7, rwidth=0.85)

    # Set titles and labels
    plt.title(f'Channel {i + 1}', loc='right', fontsize=10)
    plt.xlabel('Amplitude (uV)')
    plt.ylabel('Occurrence')
    plt.ylim(0, 200)

# Adjust subplot spacing
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle("Radial Deviation", fontsize=10)
# Show the plot
plt.tight_layout()
plt.show()
