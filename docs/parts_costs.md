# IonStar Prototype — Parts & Cost Estimate

This document outlines the estimated parts, quantities, and cost for constructing one IonStar functional prototype. All prices are ballpark USD and may vary based on supplier and scale.

---

## 1. Core Flight Frame & Structure

| Component                         | Qty | Unit Price | Total  | Notes                          |
|----------------------------------|-----|------------|--------|--------------------------------|
| Carbon Fiber Frame (custom CNC)  | 1   | $150.00    | $150.00| Lightweight, heat resistant    |
| Mounting Brackets + Screws       | 1   | $20.00     | $20.00 | Includes spare fasteners       |
| Protective Canopy Shell          | 1   | $30.00     | $30.00 | Thermoformed polycarbonate     |

---

## 2. Propulsion & Control

| Component                          | Qty | Unit Price | Total  | Notes                        |
|-----------------------------------|-----|------------|--------|------------------------------|
| Electric Ducted Fans (80mm, HV)   | 4   | $75.00     | $300.00| Directional thrust control   |
| ESC (60A HV with telemetry)       | 4   | $40.00     | $160.00| Supports bi-directional comm |
| Flight Controller (Pixhawk 6C)    | 1   | $125.00    | $125.00| Modular and space-proven     |
| IMU + GPS Combo (space-hardened)  | 1   | $90.00     | $90.00 | Optional GPS-free fallback   |

---

## 3. VR Remote Control System

| Component                           | Qty | Unit Price | Total  | Notes                              |
|------------------------------------|-----|------------|--------|------------------------------------|
| Stereo Cam Pair (HD WDR)           | 2   | $35.00     | $70.00 | Forward + rear view feeds          |
| Video Encoder Module (H.265 HW)    | 1   | $60.00     | $60.00 | Low-latency live stream            |
| VR Interface Node (RPi 5 or Jetson)| 1   | $95.00     | $95.00 | Streams data to VR headset         |
| Haptic Feedback (tactile pad)      | 2   | $25.00     | $50.00 | Optional astronaut use             |

---

## 4. Ambient Energy System (IonStar Power)

| Component                                | Qty | Unit Price | Total  | Notes                              |
|-----------------------------------------|-----|------------|--------|------------------------------------|
| Graphene Supercapacitors (20Wh equiv)   | 2   | $85.00     | $170.00| Long-life, radiation tolerant      |
| NanoLayer TENG Film Sheets (custom)     | 1   | $100.00    | $100.00| Triboelectric harvesting           |
| Radiant Absorber Coating (200ml)        | 1   | $40.00     | $40.00 | Applies over shell surface         |
| MPPT Regulator (custom config)          | 1   | $45.00     | $45.00 | Adapts variable voltages safely    |

---

## 5. Additional & Build Resources

| Component                           | Qty | Unit Price | Total  | Notes                          |
|------------------------------------|-----|------------|--------|--------------------------------|
| Thermal Insulation Foam/Wrap       | 1   | $15.00     | $15.00 | For electronics compartment    |
| Wiring + Connectors Set            | 1   | $25.00     | $25.00 | Includes space-rated cabling   |
| Assembly Tools (bits, adhesives)   | 1   | $30.00     | $30.00 | One-time purchase              |

---

## 💰 Total Estimated Cost: **$1,775.00 USD**

### Notes:
- Prices reflect single-unit prototype cost
- Bulk production could reduce total cost by ~35–50%
- Substitutions are available for most non-core parts
- Weight target: under 2.5kg fully equipped
- Compatible with low-orbit, ISS, or lunar testbed missions

> This parts list is versioned and updated per prototype iteration. Always check for compatibility with mission specs.
