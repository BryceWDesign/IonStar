# src/flight/flight_controller.py

class FlightController:
    def __init__(self):
        # Flight state flag
        self.is_flying = False
        
        # Thrusters with initial 0 power
        self.thrusters = {
            "main": 0,
            "left": 0,
            "right": 0,
            "rear": 0
        }
        
        # Stabilization angles initialized to 0
        self.pitch = 0.0
        self.roll = 0.0
        self.yaw = 0.0

    def take_off(self):
        # Set flying flag true and main thruster to max power for takeoff
        self.is_flying = True
        self.thrusters["main"] = 100

    def land(self):
        # Reset flying flag and thrusters to idle on landing
        self.is_flying = False
        for key in self.thrusters:
            self.thrusters[key] = 0

    def get_status(self):
        # Return status string based on flying state
        return "Flying" if self.is_flying else "Idle"

    def set_thrusters(self, thruster_values):
        # Update thruster power values; ignore unknown thrusters
        for key, value in thruster_values.items():
            if key in self.thrusters:
                self.thrusters[key] = value

    def update_stabilization(self, pitch, roll, yaw):
        # Update stabilization angles
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
