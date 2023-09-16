import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Number of EEG channels and samples
num_eeg_channels = 33
num_eeg_samples = 1000

# Create empty EEG data array
eeg_data = np.zeros((num_eeg_channels, num_eeg_samples))

# Create EEG subplot
plt.figure(figsize=(15, 8))

# EEG subplot
eeg_subplot = plt.subplot(2, 2, 1)
eeg_lines = eeg_subplot.plot(np.arange(num_eeg_samples), eeg_data.T)
eeg_subplot.set_title("EEG Data")

# Create Amplitude vs. Frequency subplot
amp_freq_subplot = plt.subplot(2, 2, 2)
amp_freq_line, = amp_freq_subplot.plot([], [])
amp_freq_subplot.set_title("Amplitude vs. Frequency")
amp_freq_subplot.set_xlabel("Frequency (Hz)")
amp_freq_subplot.set_ylabel("Amplitude (dB)")

# Create Amplitude vs. Time subplot for EEG
time_subplot = plt.subplot(2, 2, 3)
time_line, = time_subplot.plot([], [])
time_subplot.set_title("Amplitude vs. Time (EEG)")
time_subplot.set_xlabel("Time")
time_subplot.set_ylabel("Amplitude")

# Create Amplitude vs. Time subplot for Brainwaves
brainwave_subplot = plt.subplot(2, 2, 4)
brainwave_lines = [brainwave_subplot.plot([], label=label)[0] for label in ['Delta', 'Theta', 'Alpha', 'Beta']]
brainwave_subplot.set_title("Amplitude vs. Time (Brainwaves)")
brainwave_subplot.set_xlabel("Time")
brainwave_subplot.set_ylabel("Amplitude")
brainwave_subplot.legend(loc="upper right")

# Initialize the plot
plt.ion()
plt.show()

# Create Figure2 for EEG Density Plot
plt.figure(figsize=(15, 6))
plt.title("EEG Data Density Plot")

# Simulate EEG data updates (replace this with your data)
for i in range(num_eeg_samples):
    eeg_data[:, i] = np.random.rand(num_eeg_channels)  # Replace with your EEG data

    # Update EEG plot
    for j in range(num_eeg_channels):
        eeg_lines[j].set_ydata(eeg_data[j, :])

    # Calculate and update Amplitude vs. Frequency plot for EEG
    fs = 1000  # Sample rate (adjust as needed)
    f, Pxx = signal.welch(eeg_data[0, :], fs, nperseg=1024)
    amp_freq_line.set_data(f, 10 * np.log10(Pxx))  # Use a log scale for better visualization
    amp_freq_subplot.relim()
    amp_freq_subplot.autoscale_view()

    # Generate random Delta, Theta, Alpha, and Beta waveforms for Brainwaves
    time = np.arange(num_eeg_samples)
    delta_wave = 0.2 * np.random.rand() * np.sin(2 * np.pi * 0.5 * time / fs + 0.1 * i)  # Delta wave (0.5 Hz)
    theta_wave = 0.2 * np.random.rand() * np.sin(2 * np.pi * 4 * time / fs + 0.2 * i)    # Theta wave (4 Hz)
    alpha_wave = 0.2 * np.random.rand() * np.sin(2 * np.pi * 8 * time / fs + 0.3 * i)    # Alpha wave (8 Hz)
    beta_wave = 0.2 * np.random.rand() * np.sin(2 * np.pi * 16 * time / fs + 0.4 * i)   # Beta wave (16 Hz)

    # Update Amplitude vs. Time subplot for EEG
    time_line.set_data(time, eeg_data[0, :])

    # Update Amplitude vs. Time subplot for Brainwaves
    brainwave_lines[0].set_data(time, delta_wave)
    brainwave_lines[1].set_data(time, theta_wave)
    brainwave_lines[2].set_data(time, alpha_wave)
    brainwave_lines[3].set_data(time, beta_wave)

    # Update EEG Density Plot (Figure2) with 'rainbow' colormap
    plt.figure(2)  # Switch to Figure2
    plt.clf()  # Clear the figure
    plt.imshow(eeg_data, cmap='rainbow', aspect='auto', origin='lower')
    plt.colorbar(label='Density', cmap='rainbow')  # Use 'rainbow' colormap
    plt.title("EEG Data Density Plot")

    # Adjust subplot limits and autoscale
    for subplot in [time_subplot, brainwave_subplot]:
        subplot.relim()
        subplot.autoscale_view()

    plt.figure(1)  # Switch back to Figure1

    plt.draw()
    plt.pause(0.01)  # Adjust the pause duration as needed

# Keep the plot open until manually closed
plt.ioff()
plt.show()
