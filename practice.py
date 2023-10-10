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
window_size = int(20 * sampling_rate)  # 20-second window size
data_buffer = [np.zeros(window_size) for _ in range(num_channels)]  # Circular buffer

def update_plot(i):
    # Determine the start and end indices for the data to be plotted
    start_index = max(0, i * step)
    end_index = min((i + 1) * step, len(t))

    for j in range(num_channels):
        data_buffer[j] = np.roll(data_buffer[j], -step)  # Shift the buffer
        data_buffer[j][-step:] = channel_data[j][start_index:end_index]  # Update buffer
        lines[j].set_data(t[:window_size] / 1000, data_buffer[j])

# Function to handle animation frame updates
def animate(frame):
    if frame * step < len(t):
        update_plot(frame)
        for subplot in subplots:
            subplot.set_xlim(0, 20)  # Display a fixed 20-second window

# Create an animation
ani = FuncAnimation(plt.gcf(), animate, frames=len(t) // step, interval=50)

# Show the plot
plt.tight_layout()
plt.show()
