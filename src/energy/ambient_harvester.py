"""
Ambient Energy Harvester
Simulates harvesting ambient space energy to power the drone indefinitely.
"""

class AmbientEnergyHarvester:
    def __init__(self):
        self.energy = 0
        self.active = False

    def start(self):
        self.active = True
        print("Ambient Energy Harvester started.")

    def stop(self):
        self.active = False
        print("Ambient Energy Harvester stopped.")

    def collect(self):
        if self.active:
            # Simulate energy collection per cycle
            harvested = 10  # Arbitrary energy units
            self.energy += harvested
            print(f"Collected {harvested} units of ambient energy. Total: {self.energy}")

    def get_energy(self):
        return self.energy
