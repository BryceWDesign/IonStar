"""
Basic unit tests for FlightController
Run with: python -m unittest tests/test_flight_controller.py
"""

import unittest
from src.flight.flight_controller import FlightController

class TestFlightController(unittest.TestCase):
    def setUp(self):
        self.controller = FlightController()

    def test_initial_state(self):
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Idle")

    def test_takeoff_and_land(self):
        self.controller.take_off()
        self.assertTrue(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Flying")

        self.controller.land()
        self.assertFalse(self.controller.is_flying)
        self.assertEqual(self.controller.get_status(), "Landed")

    def test_update_stabilization(self):
        self.controller.take_off()
        self.controller.update_stabilization(pitch=5, roll=-3, yaw=15)
        self.assertEqual(self.controller.pitch, 5)
        self.assertEqual(self.controller.roll, -3)
        self.assertEqual(self.controller.yaw, 15)

    def test_set_thrusters(self):
        self.controller.set_thrusters({'main': 80, 'left': 20})
        self.assertEqual(self.controller.thrusters['main'], 80)
        self.assertEqual(self.controller.thrusters['left'], 20)

if __name__ == '__main__':
    unittest.main()
