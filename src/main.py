from simulate import run_simulation
from visualize import analyze_vehicle_data

# Run the simulation
positions, speeds = run_simulation(dt=0.01, steps=5000)

# Analyze and plot the results
analyze_vehicle_data(positions, speeds)
