### Vehicle Model for the Racing Manager game. This is a prototype in Python.
### The final model should be written in a compiled langauge for faster execution.
### This first version in a kinematic model.

import math

# x,y,z are the space coordinate of the vehicle, theta is  its the heading angle
class Vehicle:
    def __init__(self, x=0, y=0, velocity =0, theta=0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.theta = theta

# acceleration and speed of the vehicle, omega is the angular speed, dt is the time step
    def updatePosition(self, acceleration, omega, dt):
        self.velocity += acceleration * dt
        self.theta += omega * dt

        self.x += self.velocity * math.cos(self.theta) * dt
        self.y += self.velocity * math.sin(self.theta) * dt

    def __repr__(self):
            return f"Car(x={self.x:.2f}, y={self.y:.2f}, v={self.v:.2f}, theta={math.degrees(self.theta):.1f}°)"
