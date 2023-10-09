import numpy as np
import matplotlib.pyplot as plt

# Sample EMG data (replace with your actual data)
emg_data = np.random.rand(8, 8)  # Replace with your EMG data (8x8 grid)

# Create a colormap for muscle activity
cmap = plt.get_cmap('viridis')  # You can choose other colormaps

# Plot the muscle activity color map
plt.imshow(emg_data, cmap=cmap, origin='lower', interpolation='none', aspect='auto')
plt.colorbar(label='Muscle Activity')

# Customize the appearance of the plot
plt.title('Muscle Activity Color Map')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()

