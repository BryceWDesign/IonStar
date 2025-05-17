import math

class NavigationController:
    def __init__(self):
        self.current_position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.destination = None
        self.velocity = 1.0  # m/s, for simulation purposes

    def set_destination(self, x, y, z):
        self.destination = {'x': x, 'y': y, 'z': z}

    def update_position(self):
        if not self.destination:
            return

        dx = self.destination['x'] - self.current_position['x']
        dy = self.destination['y'] - self.current_position['y']
        dz = self.destination['z'] - self.current_position['z']
        distance = math.sqrt(dx**2 + dy**2 + dz**2)

        if distance < 0.1:
            self.current_position = self.destination
            self.destination = None
            return

        ratio = self.velocity / distance
        self.current_position['x'] += dx * ratio
        self.current_position['y'] += dy * ratio
        self.current_position['z'] += dz * ratio

    def get_position(self):
        return self.current_position

    def has_arrived(self):
        return self.destination is None
