import time
import winsound

# Function to play beep sound for a specified duration
def beep(duration):
    frequency = 440  # Frequency in Hertz (default is A440)
    winsound.Beep(frequency, duration * 1000)  # winsound.Beep takes duration in milliseconds

# Play beep sounds with a 5-second gap for 2 minutes
total_duration = 2 * 60  # 2 minutes in seconds
gap_duration = 5  # 5 seconds gap between beeps

start_time = time.time()

while time.time() - start_time < total_duration:
    # Play beep sound for 1 second
    beep(1)

    # Wait for 5 seconds before the next beep
    time.sleep(gap_duration)
