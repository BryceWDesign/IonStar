# IonStar Electrical Wiring Guide

This document details the electrical wiring and connector pinouts necessary to assemble the IonStar drone’s electronic systems.

## 1. Battery Connection

- Use a 4S LiPo battery (14.8V nominal).
- Connect battery leads to the Power Distribution Board (PDB) input terminals.
- Ensure correct polarity: Red wire to positive (+), Black wire to negative (-).
- Use an XT60 connector for secure battery connection.

## 2. Power Distribution Board (PDB)

- Battery input feeds the PDB.
- PDB outputs:
  - Direct battery voltage to ESCs and motors.
  - Regulated 5V output (via BEC) for flight controller and peripherals.
- Wire ESC power leads (usually red and black) to PDB motor outputs.
- Connect PDB 5V and GND to the flight controller power input pins.

## 3. ESC to Motor Wiring

- Each ESC connects to a single brushless DC motor.
- Connect the three motor phase wires from the ESC to the motor wires.
- Secure connections with solder and heat shrink tubing.
- Ensure ESC signal wires connect to the flight controller’s PWM output pins as per schematic.

## 4. Flight Controller Wiring

- **Power:**
  - Connect flight controller 5V and GND to the PDB regulated output.
- **ESC Signal Wires:**
  - Connect four ESC PWM signal wires to flight controller GPIO pins configured for PWM output.
- **Sensors:**
  - IMU connected via I2C lines (SDA, SCL) with 4.7kΩ pull-up resistors.
  - Barometric sensor connected via SPI or I2C as per schematic.
  - GPS connected via UART pins (RX, TX).
- **RC Receiver:**
  - Connect PWM signal lines to flight controller GPIO pins capable of input capture.

## 5. Connector Pinouts Summary

| Connector        | Pin 1        | Pin 2        | Pin 3         | Notes                    |
|------------------|--------------|--------------|---------------|--------------------------|
| Battery (XT60)   | Positive (+) | Negative (-) | N/A           | Ensure correct polarity  |
| ESC Signal       | PWM Signal   | 5V           | Ground (GND)  | PWM to flight controller |
| IMU (I2C)        | SDA          | SCL          | GND, VCC      | Pull-ups required        |
| GPS UART         | RX           | TX           | GND           | Baud rate 9600 default   |
| RC Receiver PWM  | Signal       | 5V           | Ground (GND)  | Use interrupt pins       |

## 6. Safety and Best Practices

- Double-check all wiring before powering up.
- Use heat shrink tubing and cable management for durability.
- Test individual components (motors, ESCs, sensors) separately prior to integration.
- Always remove propellers when testing electronics to avoid injury.

---

