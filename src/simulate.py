from vehicle_model import Vehicle

def run_simulation(dt, steps, initial_x, initial_y, initial_velocity, initial_theta):
    vehicle = Vehicle(initial_x, initial_y, initial_velocity, initial_theta)

    positions = []
    speeds = []

    for step in range(steps):
        acceleration = 2
        omega = 0

        vehicle.update(acceleration, omega, dt)

        # Collect data (position and speed) for analysis
        positions.append((vehicle.x, vehicle.y))
        speeds.append(vehicle.velocity)

        print(vehicle.x, end='\n')
    return positions, speeds
