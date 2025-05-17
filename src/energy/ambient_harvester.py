"""
Ambient Energy Harvester Module
Simulates harvesting ambient space energy for IonStar drone power support.
"""

import random
import time

class AmbientEnergyHarvester:
    def __init__(self):
        self.active = False
        self.energy_stored = 0.0  # in Joules

    def start(self):
        print("AmbientEnergyHarvester: Starting energy collection.")
        self.active = True

    def stop(self):
        print("AmbientEnergyHarvester: Stopping energy collection.")
        self.active = False

    def collect(self):
        if not self.active:
            return

        # Simulate energy harvesting from ambient sources
        harvested = self._simulate_harvest()
        self.energy_stored += harvested
        print(f"Harvested {harvested:.4f} Joules, total stored: {self.energy_stored:.4f} Joules")

    def _simulate_harvest(self):
        # Placeholder simulation: random small amount of energy per cycle
        return random.uniform(0.05, 0.15)

    def get_energy(self):
        return self.energy_stored

    def consume_energy(self, amount):
        if amount <= self.energy_stored:
            self.energy_stored -= amount
            return True
        else:
            print("Warning: Not enough energy stored.")
            return False
