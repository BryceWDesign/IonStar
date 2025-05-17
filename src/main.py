from src.flight.flight_controller import FlightController

def main():
    controller = FlightController()
    print("Initial status:", controller.get_status())

    controller.take_off()
    print("Status after takeoff:", controller.get_status())

    controller.set_thrusters({'main': 75, 'left': 30, 'right': 30, 'rear': 20})
    print("Thrusters set:", controller.thrusters)

    controller.update_stabilization()
    print("Pitch after stabilization update:", controller.pitch)

    controller.land()
    print("Status after landing:", controller.get_status())

if __name__ == "__main__":
    main()
