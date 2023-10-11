import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# Load your EMG data from a CSV file
dataset = pd.read_csv("../emgraw.csv")


# Number of channels (assuming 8 channels)


# Define the layout of the subplots (adjust as needed)
num_subplot_rows = 1
num_subplot_cols = 1  # Adjusted to match 8 channels

# Create a figure with subplots
fig, axes = plt.subplots(num_subplot_rows, num_subplot_cols, figsize=(12, 6))

# Initialize the images list
images = []

def update(i):
    for j in range(1):
        # Calculate the subplot row and column for the current channel
        row = j // num_subplot_cols
        col = j % num_subplot_cols

        # Select the subplot


        # Replace the data loading logic with your dataset
        x = dataset.iloc[4400+i, j+1:j+9].values
        image_data = (x - min(x)) / (max(x) - min(x))
        image_data = image_data.reshape(2, 4)
        if not images or len(images) <= j:
            # If the images list is empty or not long enough, create a new image
            im = plt.imshow(image_data, cmap='gnuplot2', interpolation='spline16')
            images.append(im)

        else:
            # Update the existing image with new data
            images[j].set_data(image_data)
            cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # Adjust the position and size as needed
            cbar = fig.colorbar(images[0], cax=cbar_ax, label='Intensity')

# Set the number of frames
num_frames = 5300
ani = FuncAnimation(fig, update, frames=num_frames, repeat=False, interval=200)



plt.show()
