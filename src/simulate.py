from vehicle_model import Vehicle

# TODO: make user choose between step-based, time-based simulation and unlimited time simulation
def run_simulation(dt, steps, initial_x, initial_y,
        initial_velocity, initial_theta, initial_steering_angle,
        vehicle_name, version_number):
    # Create a vehicle instance with parameters loaded from its specific database
    vehicle = Vehicle(initial_x, initial_y,
                      initial_velocity, initial_theta, initial_steering_angle,
                      vehicle_name, version_number)

    positions = []
    speeds = []

    # Instead of using acceleration, use wheel torque given by the engine model
    for step in range(steps):
        acceleration = 2  # This should be replaced with your torque model
        omega = 0  # Update this with your steering model

        vehicle.update(acceleration, omega, dt)

        # Collect data (position and speed) for analysis
        positions.append((vehicle.x, vehicle.y))
        speeds.append(vehicle.velocity)

        print(vehicle.x, end='\n')

    return positions, speeds
