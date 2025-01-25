import matplotlib.pyplot as plt

def analyze_vehicle_data(positions, speeds):
    """Analyze and plot vehicle data."""
    # Plot position vs time (you can customize this for other data analysis)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)  # Position plot
    plt.plot(positions, label='Position (m)', color='b')
    plt.title('Vehicle Position Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (meters)')
    plt.legend()

    # Plot speed vs time
    plt.subplot(2, 1, 2)  # Speed plot
    plt.plot(speeds, label='Speed (m/s)', color='r')
    plt.title('Vehicle Speed Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speed (m/s)')
    plt.legend()

    plt.tight_layout()
    plt.show()
