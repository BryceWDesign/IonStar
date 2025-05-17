# IonStar Drone Hardware Schematics

This document provides a detailed overview of the hardware schematics for the IonStar drone project, including the flight controller, power distribution, and sensor connections.

## 1. Flight Controller Overview

The flight controller board integrates the main MCU, sensor modules, power regulation, and communication interfaces. Below is a summary of key components and their connections:

- **Microcontroller Unit (MCU):** ARM Cortex-M4 based STM32F4 series.
- **Power Input:** 3S to 4S LiPo battery input regulated through a buck converter.
- **ESC Signal Outputs:** Four PWM outputs controlling Brushless DC motor ESCs.
- **Sensor Inputs:**
  - IMU (Gyroscope, Accelerometer, Magnetometer) via I2C.
  - Barometric Pressure sensor via SPI or I2C.
  - GPS module via UART.
- **Telemetry and RC Receiver:** UART and PWM signal inputs.
- **USB Port:** For programming and debugging.

## 2. Power Distribution Board (PDB)

- Receives power from the LiPo battery.
- Provides regulated 5V output for the flight controller and peripherals.
- Distributes battery voltage directly to ESCs and motors.

## 3. Wiring Diagram

```plaintext
 LiPo Battery (4S)
      |
      V
+-------------+       +----------------+
| Power Dist. |------>| ESCs (4x)      |-----> Motors (4x)
| Board (PDB) |       +----------------+
      |                 
      |                
      +--------> Flight Controller Board
                    |      |       |       |
                 IMU( I2C) Baro(SPI) GPS(UART) RC Receiver(PWM)
4. Sensor Pinouts and Connections
Sensor	Interface	MCU Pins	Notes
IMU (BNO055)	I2C	SDA (PB7), SCL (PB6)	Pull-up resistors required
Barometric Sensor	SPI/I2C	MOSI, MISO, SCK	Use SPI for better speed
GPS Module	UART	RX (PA10), TX (PA9)	Baud rate 9600 default
RC Receiver	PWM	GPIO Pins (PCx)	Interrupt capable pins

5. PCB Layout Considerations
Keep signal and power grounds separate until the ground plane.

Place decoupling capacitors close to MCU and sensors.

Shield and route RF signals carefully to reduce noise.

Ensure motor and ESC wiring is twisted to minimize EMI.

6. Additional Resources
Refer to datasheets of each component for pinouts and specifications.

Use KiCad or Eagle for schematic capture and PCB layout.

Test continuity and voltages carefully before powering entire system.

