"""
IonStar Main Control Program
Entry point for drone control system.
"""

import time
from control.flight_controller import FlightController
from energy.ambient_harvester import AmbientEnergyHarvester
from communication.vr_interface import VRInterface

def main():
    print("IonStar control stack initializing...")

    # Initialize subsystems
    flight_controller = FlightController()
    energy_harvester = AmbientEnergyHarvester()
    vr_interface = VRInterface()

    # Power up sequence
    energy_harvester.start()
    flight_controller.initialize()
    vr_interface.connect()

    try:
        while True:
            # Harvest ambient energy
            energy_harvester.collect()

            # Update flight controls based on VR input
            vr_commands = vr_interface.receive_commands()
            flight_controller.update(vr_commands)

            # Send telemetry data to VR interface
            telemetry = flight_controller.get_telemetry()
            vr_interface.send_telemetry(telemetry)

            # Loop delay
            time.sleep(0.02)  # 50 Hz control loop

    except KeyboardInterrupt:
        print("Shutting down IonStar control system...")
        flight_controller.shutdown()
        energy_harvester.stop()
        vr_interface.disconnect()

if __name__ == "__main__":
    main()
