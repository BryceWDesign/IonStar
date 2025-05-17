# src/flight/flight_controller.py

class FlightController:
    def __init__(self):
        self.status = "initialized"

    def start(self):
        self.status = "in-flight"

    def stop(self):
        self.status = "stopped"
