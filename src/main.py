"""
IonStar Main Program
Simulates startup, control loop, and shutdown of the drone system.
"""

import time
from src.flight.flight_controller import FlightController
from src.energy.ambient_harvester import AmbientEnergyHarvester
from src.communication.vr_interface import VRInterface

def main():
    print("IonStar Drone Simulation Starting...")

    # Initialize components
    flight_controller = FlightController()
    energy_harvester = AmbientEnergyHarvester()
    vr_interface = VRInterface()

    # Start systems
    energy_harvester.start()
    vr_interface.connect()

    # Simulate main loop
    try:
        flight_controller.take_off()
        for _ in range(10):  # Simulate 10 control cycles
            energy_harvester.collect()
            commands = vr_interface.receive_commands()
            if commands:
                flight_controller.update_stabilization(
                    pitch=commands.get('pitch', 0),
                    roll=commands.get('roll', 0),
                    yaw=commands.get('yaw', 0)
                )
                flight_controller.set_thrusters({'main': commands.get('thrust', 0)})
                telemetry = {
                    'pitch': flight_controller.pitch,
                    'roll': flight_controller.roll,
                    'yaw': flight_controller.yaw,
                    'energy': energy_harvester.get_energy()
                }
                vr_interface.send_telemetry(telemetry)
            time.sleep(1)

        flight_controller.land()
    except KeyboardInterrupt:
        print("Simulation interrupted.")
    finally:
        vr_interface.disconnect()
        energy_harvester.stop()
        print("IonStar Drone Simulation Ended.")

if __name__ == "__main__":
    main()
