import time
from vehicle_model import Vehicle

def run_simulation(dt, steps):
    vehicle = Vehicle(x=0, y=0, velocity=0, theta=0.5)

    positions = []
    speeds = []

    for step in range(steps):
        acceleration = 2
        omega = 0.05

        vehicle.update(acceleration, omega, dt)

        # Collect data (position and speed) for analysis
        positions.append((vehicle.x, vehicle.y))
        speeds.append(vehicle.velocity)

    return positions, speeds
