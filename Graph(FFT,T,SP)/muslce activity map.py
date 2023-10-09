import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Sample EMG data (replace with your actual data)
dataset = np.random.rand(8, 8)  # An 8x8 grid of EMG values
print(dataset)
# Create a muscle activity map
plt.figure(figsize=(8, 6))
plt.imshow(dataset, cmap='viridis', interpolation='gaussian', aspect='auto')
plt.colorbar(label='EMG Intensity')
plt.title('Muscle Activity Map')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(False)
plt.show()