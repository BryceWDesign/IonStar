# IonStar Drone Hardware Overview

## Introduction
This document provides a detailed overview of all hardware components required for the IonStar drone project. It is intended for engineers, technicians, and developers who will be assembling, testing, or integrating the physical drone platform.

## Hardware Components Summary

| Component           | Description                                     | Quantity | Notes                          |
|---------------------|------------------------------------------------|----------|--------------------------------|
| Frame               | Custom carbon fiber drone frame                 | 1        | Lightweight and durable        |
| Flight Controller   | IonStar Flight Controller PCB                   | 1        | Core control unit              |
| Motors              | Brushless DC motors (BLDC), 4x                   | 4        | High RPM, matched for stability |
| Electronic Speed Controllers (ESC) | ESC modules compatible with motors         | 4        | For precise motor speed control |
| Propellers          | Drone propellers (matched pitch and diameter)  | 4        | Balanced for stability         |
| Battery             | LiPo battery pack, 4S (14.8V nominal)           | 1        | High capacity for extended flight |
| Power Distribution Board (PDB) | Distributes battery power to ESCs and components | 1 | Must support max current draw  |
| Sensors             | IMU (Inertial Measurement Unit), Barometer, GPS| 1 each   | For stabilization and navigation|
| Radio Receiver      | 2.4 GHz RC receiver                              | 1        | Compatible with transmitter    |
| Telemetry Module    | 915 MHz telemetry radio module                   | 1        | For data link to ground station|
| Wiring and Connectors | High-quality wires, connectors, and shrink tubing | Varied   | For robust and reliable connections |
| Mounting Hardware   | Screws, spacers, vibration dampers               | Varied   | To securely mount components   |

## Hardware Notes

- **Frame:** Designed for optimal weight-to-strength ratio; recommended to verify all dimensions before assembly.
- **Motors & ESCs:** Use ESCs supporting at least 30A continuous current; calibrate ESCs before first flight.
- **Battery:** LiPo batteries must be handled with care; follow all safety guidelines for charging and storage.
- **Sensors:** Ensure sensors are securely mounted and calibrated before flight to guarantee accurate readings.
- **Wiring:** Use appropriate gauge wiring for current load; minimize wire length to reduce weight and resistance.

## Recommended Tools for Hardware Assembly

- Precision screwdrivers (Phillips and flathead)
- Soldering iron with fine tip
- Heat shrink tubing and heat gun
- Multimeter
- Wire cutters and strippers
- Thread locker (e.g., Loctite)
- Tweezers or small pliers

## Summary

This hardware overview outlines all critical components and considerations needed for building the IonStar drone platform. The following documents will provide the detailed parts list, wiring schematics, assembly instructions, and firmware setup.

---
