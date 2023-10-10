import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load your EMG data from a CSV file
dataset = pd.read_csv("../raw_EMG.csv")
# Extract the time values from the first column of the dataset
t = dataset.iloc[:, 0]
print(len(t))
# Define colors for different channels
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Extract EMG data for all channels
num_channels = 8
emg_data = dataset.iloc[:, 1:num_channels + 1] * 1000  # Amplify the data for plotting

# Set the sampling rate (samples per second)
sampling_rate = 1000

# Create a figure for the plot
plt.figure(figsize=(12, 12))

# Create subplots for each channel
subplots = [plt.subplot(num_channels, 1, i + 1) for i in range(num_channels)]

# Initialize the lines in each subplot
lines = [subplot.plot([], [], color=colors[i])[0] for i, subplot in enumerate(subplots)]

# Set titles and labels
for i, subplot in enumerate(subplots):
    subplot.set_title(f'Channel {i + 1}', loc='right', fontsize=10)
    subplot.set_ylabel('Amplitude (uV)', fontsize=7)

# Adjust subplot spacing
plt.subplots_adjust(hspace=0.3)

# Set the x-axis label
plt.xlabel('Time (s)')

# Initialize data for each channel
channel_data = [emg_data.iloc[:, i].values for i in range(num_channels)]

# Function to update the plot with new data
step = 100
window_size = int(5 * sampling_rate)
data_buffer = [np.zeros(window_size) for _ in range(num_channels)]  # Circular buffer
max_x_limit = 1000  # Set the maximum x-axis limit to 20 seconds

def update_plot(i):
    start_index = i * step
    end_index = start_index + window_size

    for j in range(num_channels):
        data_buffer[j] = channel_data[j][start_index:end_index]  # Update buffer
        lines[j].set_data(t[start_index:end_index] / 1000, data_buffer[j])
        subplots[j].set_xlim(t[start_index] / 1000, t[end_index - 1] / 1000)
        subplots[j].set_ylim(-1, 1)

# Function to handle animation frame updates
def animate(frame):
    if frame * step + window_size < len(t):
        update_plot(frame)
    else:
        # Keep shifting the data buffer to the left
        for j in range(num_channels):
            data_buffer[j] = np.roll(data_buffer[j], -step)
            lines[j].set_data(t[:window_size] / 1000, data_buffer[j])
            subplots[j].set_xlim(t[0] / 1000, t[window_size - 1] / 1000)

# Create an animation
ani = FuncAnimation(plt.gcf(), animate, frames=len(t) // step, interval=50)

# Show the plot
plt.tight_layout()
plt.show()

