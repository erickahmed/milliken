import matplotlib.pyplot as plt

def analyze_vehicle_data(positions, speeds):

    # Plot position as XY coordinates
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)  # Position plot
    x, y = zip(*positions)
    plt.plot(x, y, label='Path', color='b')
    plt.title('Vehicle Path')
    plt.xlabel('X Coordinate [m]')
    plt.ylabel('Y Coordinate [m]')
    plt.legend()

    # Plot speed vs time
    plt.subplot(2, 1, 2)  # Speed plot
    plt.plot(speeds, label='Speed [m/s]', color='r')
    plt.title('Vehicle Speed Over Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Speed [m/s]')
    plt.legend()

    plt.tight_layout()
    plt.show()
