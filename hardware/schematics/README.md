# IonStar Hardware Schematics

This directory contains references and explanations for IonStar’s electrical wiring, PCB layouts, and connector specifications.

## 📡 Power System & Harvesting Modules

- **Ambient Harvester Coil Wiring:**  
  Coil to supercapacitor array via graphene-regulated routing.  
  Connect shielded leads directly to capacitor charge bus.

- **Supercapacitor Cell Stack:**  
  Series-connected 2.7V units with thermal sensors and overflow bleed resistors.  
  Ground ring uses graphite paste thermal spreader to chassis.

- **Motor Controller Board:**  
  Custom ESC design with ion drive interface & digital thrust loop monitoring.  
  Each thruster module uses adaptive current injection via programmable PID feedback.

## 🧠 Control Bus & Sensors

- **I2C Bus Layout:**  
  - IMU  
  - Orientation sensor  
  - VR depth telemetry  
  - Ultrasonic backup (ground mode)

- **USB-C Debug Ports:**  
  Onboard diagnostic serial shell during test phase.

## 🧾 To-Do

- Upload Altium schematics  
- Export Gerber files  
- Document pinouts for modular rebuild  
- Diagram control flow from MCU to thruster array

> More to be added as hardware matures.
