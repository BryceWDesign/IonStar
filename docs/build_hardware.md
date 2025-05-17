# IonStar Hardware Build and Assembly Guide

## Overview
This document covers all steps required to assemble and build the IonStar drone hardware for space and Earth flight.

---

## Bill of Materials (BOM)

Refer to [`hardware/bom.csv`](../hardware/bom.csv) for the complete list of parts including:

- Frame materials
- Electronics: flight controller, thrusters, sensors
- Power system components
- Wiring, connectors, fasteners

---

## Assembly Steps

### 1. Frame Construction

- Cut and shape lightweight, heat-resistant materials (e.g., carbon fiber composites).
- Assemble frame according to provided CAD files and schematics.
- Ensure structural integrity for launch stresses.

### 2. Electronics Installation

- Mount flight controller securely inside the frame.
- Connect ion thrusters to power bus and control lines.
- Install ambient energy harvesting units in exposed areas.

### 3. Wiring and Power

- Route wiring neatly with insulation.
- Connect batteries, thruster controllers, and sensor modules.
- Verify all connections for continuity and safety.

### 4. Sensor Calibration

- Calibrate IMUs, gyroscopes, and range finders.
- Test sensor outputs for accuracy.

### 5. Final Checks

- Perform power-on self-test (POST).
- Validate communication with ground control and VR interfaces.
- Conduct vacuum chamber tests if available.

---

## Notes

- Maintain strict ESD precautions.
- Use space-rated connectors and materials whenever possible.
- Follow safety protocols during thruster handling.

---

For detailed schematics and wiring diagrams, see the `hardware/schematics/` directory.

---

## Contact and Support

For questions or assistance, refer to the `CONTRIBUTING.md` guide or open an issue on GitHub.

