from simulate import run_simulation
from visualize import analyze_vehicle_data
from create_vehicle import create_vehicle_database

create_vehicle_database('truck', 'v1', 6000, 4, 4500)

positions, speeds = run_simulation(dt=0.01, steps=5000, initial_x=0, initial_y=0,
                                   initial_velocity=0, initial_theta=0, initial_steering_angle=0,
                                   vehicle_name='truck', version_number='v1')

analyze_vehicle_data(positions, speeds)
