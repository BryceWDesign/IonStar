"""
Flight Controller Module for IonStar Drone
Handles stabilization, thruster control, and sensor fusion
"""

import math
import random  # placeholder for sensor data simulation

class FlightController:
    def __init__(self):
        self.imu_data = None
        self.thruster_power = [0, 0, 0, 0]  # Four thrusters power levels (0-100%)
        self.telemetry = {}

    def initialize(self):
        # Initialize sensors and control loops
        print("FlightController: Initializing sensors and control systems.")
        self.imu_data = self.read_imu()

    def read_imu(self):
        # Placeholder: Simulate IMU readings (pitch, roll, yaw)
        pitch = random.uniform(-5, 5)
        roll = random.uniform(-5, 5)
        yaw = random.uniform(-180, 180)
        return {'pitch': pitch, 'roll': roll, 'yaw': yaw}

    def update(self, vr_commands):
        """
        Update flight control based on VR input commands.
        vr_commands expected format:
        {
            'pitch': float,
            'roll': float,
            'yaw': float,
            'thrust': float (0 to 100)
        }
        """
        self.imu_data = self.read_imu()
        # Simple stabilization logic: adjust thrusters to maintain orientation
        pitch_error = vr_commands.get('pitch', 0) - self.imu_data['pitch']
        roll_error = vr_commands.get('roll', 0) - self.imu_data['roll']
        yaw_error = vr_commands.get('yaw', 0) - self.imu_data['yaw']
        thrust = vr_commands.get('thrust', 0)

        # Map errors to thruster power adjustments (simplified)
        base_power = thrust
        self.thruster_power[0] = self._clamp(base_power + pitch_error - roll_error + yaw_error)
        self.thruster_power[1] = self._clamp(base_power - pitch_error - roll_error - yaw_error)
        self.thruster_power[2] = self._clamp(base_power + pitch_error + roll_error - yaw_error)
        self.thruster_power[3] = self._clamp(base_power - pitch_error + roll_error + yaw_error)

        # Update telemetry
        self.telemetry = {
            'imu': self.imu_data,
            'thrusters': self.thruster_power
        }

    def get_telemetry(self):
        return self.telemetry

    def shutdown(self):
        # Shut down thrusters and sensors safely
        print("FlightController: Shutting down, setting thrusters to zero.")
        self.thruster_power = [0, 0, 0, 0]

    def _clamp(self, value, min_value=0, max_value=100):
        return max(min_value, min(max_value, value))
