# src/flight/flight_controller.py

class FlightController:
    def __init__(self):
        self.is_flying = False
        self.thrusters = {'main': 0, 'left': 0, 'right': 0}
        self.pitch = 0.0

    def take_off(self):
        self.is_flying = True
        self.set_thrusters({'main': 100, 'left': 50, 'right': 50})

    def land(self):
        self.is_flying = False
        self.set_thrusters({'main': 0, 'left': 0, 'right': 0})

    def set_thrusters(self, thruster_values):
        for key in thruster_values:
            if key in self.thrusters:
                self.thrusters[key] = thruster_values[key]

    def update_stabilization(self):
        # Simple example: pitch increases by 5 degrees on update
        if self.is_flying:
            self.pitch += 5

    def get_status(self):
        return "Flying" if self.is_flying else "Idle"
