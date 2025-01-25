import time
from vehicle_model import Vehicle

vehicle = Vehicle()
dt = 0.01

for _ in range(200):
    vehicle.update(acceleration=10, omega=3, dt=dt)  # Apply throttle & slight turn
    print(vehicle)
    time.sleep(dt)  # Simulate real-time updates
