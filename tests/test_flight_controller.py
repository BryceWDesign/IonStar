import unittest
from src.flight.flight_controller import FlightController

class TestFlightController(unittest.TestCase):
    def setUp(self):
        self.controller = FlightController()

    def test_initial_state(self):
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Idle")
        self.assertEqual(self.controller.pitch, 0.0)
        self.assertEqual(self.controller.thrusters, {'main': 0.0, 'left': 0.0, 'right': 0.0, 'rear': 0.0})

    def test_takeoff_and_land(self):
        self.controller.take_off()
        self.assertTrue(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Flying")
        self.assertEqual(self.controller.thrusters['main'], 100.0)

        self.controller.land()
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Idle")
        self.assertTrue(all(power == 0.0 for power in self.controller.thrusters.values()))

    def test_set_thrusters(self):
        self.controller.set_thrusters({'main': 80, 'left': 20, 'right': 15, 'rear': 10})
        self.assertEqual(self.controller.thrusters['main'], 80)
        self.assertEqual(self.controller.thrusters['left'], 20)
        self.assertEqual(self.controller.thrusters['right'], 15)
        self.assertEqual(self.controller.thrusters['rear'], 10)

    def test_update_stabilization(self):
        self.controller.take_off()
        initial_pitch = self.controller.pitch
        self.controller.update_stabilization()
        self.assertEqual(self.controller.pitch, initial_pitch + 5.0)

if __name__ == '__main__':
    unittest.main()
