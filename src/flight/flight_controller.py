class FlightController:
    def __init__(self):
        self.is_flying = False
        self.thrusters = {
            'main': 0,
            'left': 0,
            'right': 0,
            'rear': 0,
            'front': 0
        }
        self.stabilization_data = {
            'pitch': 0.0,
            'roll': 0.0,
            'yaw': 0.0
        }

    def take_off(self):
        self.is_flying = True
        self.set_thrusters({'main': 100})  # initial upward thrust

    def land(self):
        self.set_thrusters({'main': 0})
        self.is_flying = False

    def update_stabilization(self, pitch, roll, yaw):
        self.stabilization_data['pitch'] = pitch
        self.stabilization_data['roll'] = roll
        self.stabilization_data['yaw'] = yaw

    def set_thrusters(self, thrust_dict):
        for k, v in thrust_dict.items():
            if k in self.thrusters:
                self.thrusters[k] = v

    def get_status(self):
        return {
            'is_flying': self.is_flying,
            'thrusters': self.thrusters,
            'stabilization': self.stabilization_data
        }
