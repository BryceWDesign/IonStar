# src/flight/flight_controller.py

class FlightController:
    def __init__(self):
        self.is_flying = False
        self.thrusters = {
            "main": 0,
            "left": 0,
            "right": 0,
            "rear": 0
        }
        self.pitch = 0.0
        self.roll = 0.0
        self.yaw = 0.0

    def take_off(self):
        self.is_flying = True
        self.thrusters["main"] = 100

    def land(self):
        self.is_flying = False
        for key in self.thrusters:
            self.thrusters[key] = 0

    def get_status(self):
        return "Flying" if self.is_flying else "Idle"

    def set_thrusters(self, thruster_values):
        for key, value in thruster_values.items():
            if key in self.thrusters:
                self.thrusters[key] = value

    def update_stabilization(self, pitch, roll, yaw):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
