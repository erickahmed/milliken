### This is a prototype in Python.
### The final vehicle model should be written in a compiled langauge for faster execution.

import sqlite3
import math
import os

class Steering:
    def __init__(self, vehicle_name, vehicle_version, steering_wheel_angle):
        self.vehicle_name = vehicle_name
        self.vehicle_version = vehicle_version
        self.steering_wheel_angle = steering_wheel_angle

        self.load_steering_parameters(vehicle_name, vehicle_version)
        self.steering_model(steering_wheel_angle)

    def load_steering_parameters(self, vehicle_name, vehicle_version):
        """Load steering parameters from the database"""

        db_path = os.path.join('../db/vehicles/', vehicle_name, vehicle_version, 'parameters.db')

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database for vehicle '{self.vehicle_name}' not found at {db_path}.")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT steering_ratio
                FROM tire_specs
                WHERE vehicle_name = ? AND vehicle_version = ?
            ''', (self.vehicle_name, self.vehicle_version))

            row = cursor.fetchone()
            if row:
                (self.steering_ratio) = row
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            raise
        finally:
            conn.close()

    def steering_model(self, steering_wheel_angle):
        """
        Compute the steering angles based on the steering wheel angle and loaded parameters.
        """
        # angle of the front wheel(s) in the siigle track model
        wheel_angle_F = self.steering_ratio * self.steering_wheel_angle
        return wheel_angle_F

    def update(self, dt):
        wheel_angle_F = self.steering_model(self.steering_wheel_angle)
        self.wheel_angle_F = wheel_angle_F * dt

    #def __repr__(self):


class Vehicle:
    def __init__(self, vehicle_name, vehicle_version,
                x, y, z, roll, pitch, yaw,
                halfbase_F, halfbase_R,
                velocity, theta,
                steering: Steering):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw      # positive is anti-clockwise
        self.wheelbase = halfbase_F + halfbase_R #ideally dynamics will be evaluated with formulas that do not require wheelbase (useful for vehicles with more than 2 axles)
        self.velocity = velocity
        self.wheel_angle_F = steering

        self.load_vehicle_parameters(vehicle_name, vehicle_version)

    def load_vehicle_parameters(self, vehicle_name, vehicle_version):
        """Load vehicle parameters from the database"""
        db_path = os.path.join('../db/vehicles/', vehicle_name, vehicle_version, 'parameters.db')

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database for vehicle '{vehicle_name}' not found at {db_path}.")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT mass, COG_x, COG_y, COG_z,
            FROM vehicle_specs WHERE name = ?
        ''', (vehicle_name,))

        row = cursor.fetchone()
        if row:
            self.mass, self.COG_x, self.COG_y, self.COG_z = row
        else:
            raise ValueError(f"Vehicle '{vehicle_name}' not found in the database.")

        conn.close()

    def single_track_model(self, velocity, wheel_angle):
        #this is just a very rude approximation!
        longitudinal_velocity = velocity * math.sin(wheel_angle)
        lateral_velocity = velocity * math.cos(wheel_angle)

        slip_angle = math.atan(lateral_velocity / longitudinal_velocity)
        ackermann_angle = math.atan((self.wheelbase * self.yaw) / longitudinal_velocity)

        return longitudinal_velocity, lateral_velocity, slip_angle, ackermann_angle

    def update(self, dt):
        longitudinal_velocity, lateral_velocity, slip_angle, ackermann_angle = self.single_track_model(self.velocity, self.wheel_angle_F)

        self.x += longitudinal_velocity * dt
        self.y += lateral_velocity * dt


    # TODO: Take a look at this thing
    #def __repr__(self):
    #        return f"Vehicle(x={self.x:.2f}, y={self.y:.2f}, v={self.velocity:.2f}, theta={math.degrees(self.theta):.1f}°)"
