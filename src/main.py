from simulate import run_simulation
from visualize import analyze_vehicle_data

positions, speeds = run_simulation(dt=0.01, steps=15000, initial_x=0, initial_y=0, initial_velocity=0, initial_theta=0)

analyze_vehicle_data(positions, speeds)
