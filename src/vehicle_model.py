### This is a prototype in Python.
### The final vehicle model should be written in a compiled langauge for faster execution.
### This first version is a kinematic model.

import sqlite3
import math
import os

class Vehicle:
    def __init__(self, x, y, velocity, theta, steering_angle, vehicle_name):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.theta = theta
        self.steering_angle = steering_angle

        # Load vehicle parameters from the vehicle-specific database
        self.load_vehicle_params(vehicle_name)

    def load_vehicle_params(self, vehicle_name):
        # Construct the path to the vehicle's specific database
        db_path = os.path.join('../db/vehicles/', vehicle_name, 'vehicle_specs.db')

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database for vehicle '{vehicle_name}' not found at {db_path}.")

        # Open the SQLite database that stores vehicle specifications
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query the database for the vehicle's parameters (mass, wheelbase, inertia)
        cursor.execute('''
            SELECT mass, wheelbase, inertia FROM vehicle_specs WHERE name = ?
        ''', (vehicle_name,))

        row = cursor.fetchone()
        if row:
            self.mass, self.wheelbase, self.inertia = row
        else:
            raise ValueError(f"Vehicle '{vehicle_name}' not found in the database.")

        conn.close()

    def update(self, acceleration, omega, dt):
        # Update the vehicle's position and velocity based on input acceleration and angular velocity (omega)
        self.velocity += acceleration * dt
        self.theta += omega * dt

        self.x += self.velocity * math.cos(self.theta) * dt
        self.y += self.velocity * math.sin(self.theta) * dt

    def __repr__(self):
            return f"Vehicle(x={self.x:.2f}, y={self.y:.2f}, v={self.velocity:.2f}, theta={math.degrees(self.theta):.1f}°)"
