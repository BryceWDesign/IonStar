def take_off(self):
    self.is_flying = True
    self.thrusters["main"] = 100

def land(self):
    self.is_flying = False
    self.thrusters["main"] = 0

def get_status(self):
    return "Flying" if self.is_flying else "Idle"

def set_thrusters(self, values):
    for k in values:
        if k in self.thrusters:
            self.thrusters[k] = values[k]

def update_stabilization(self, pitch, roll, yaw):
    self.pitch = pitch
    self.roll = roll
    self.yaw = yaw
