# tests/test_flight_controller.py

import unittest
from src.flight.flight_controller import FlightController

class TestFlightController(unittest.TestCase):
    def setUp(self):
        self.controller = FlightController()

    def test_initial_state(self):
        self.assertEqual(self.controller.get_status(), "Idle")
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.thrusters, {'main': 0, 'left': 0, 'right': 0})
        self.assertEqual(self.controller.pitch, 0.0)

    def test_takeoff_and_land(self):
        self.controller.take_off()
        self.assertTrue(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Flying")
        self.controller.land()
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Idle")

    def test_set_thrusters(self):
        self.controller.set_thrusters({'main': 80, 'left': 20, 'right': 20})
        self.assertEqual(self.controller.thrusters, {'main': 80, 'left': 20, 'right': 20})

    def test_update_stabilization(self):
        self.controller.take_off()
        self.controller.update_stabilization()
        self.assertEqual(self.controller.pitch, 5.0)

if __name__ == '__main__':
    unittest.main()
