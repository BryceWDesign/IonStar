# IonStar Autonomous Space Drone

🚀 **IonStar** is an advanced autonomous drone designed for high-precision space exploration and research missions. This open-source project integrates state-of-the-art flight control software with a robust hardware platform tailored for extreme environments.

---

## Project Overview

IonStar combines modular hardware and intelligent software to achieve stable flight, autonomous navigation, and environmental data acquisition in space or high-altitude conditions.

---

## Features

- Fully autonomous flight control system
- Modular hardware design for easy maintenance and upgrades
- Advanced stabilization and thruster control algorithms
- Real-time telemetry and sensor integration
- Open-source software with unit-tested modules

---

## Repository Contents

- `src/`: Core flight control software modules
- `tests/`: Unit and integration tests for software validation
- `docs/`: Documentation including hardware schematics, assembly, and build instructions
- `hardware/`: Electrical schematics and PCB design files
- `scripts/`: Utility scripts for deployment and diagnostics

---

## Software Setup

### Prerequisites

- Python 3.11+
- Required Python packages (install via `pip install -r requirements.txt`)
- Git (for cloning repository)
- Compatible development environment (IDE or CLI)

### Installation

```bash
git clone https://github.com/BryceWDesign/IonStar.git
cd IonStar
pip install -r requirements.txt
python -m unittest discover -s tests -v
Hardware Assembly and Build Instructions
To build the IonStar drone hardware, follow these detailed steps:

Tools Required
Phillips and flathead screwdrivers

Hex wrenches (sizes per parts list)

Needle nose pliers and tweezers

Medium-strength thread locker

Torque driver (optional)

Step 1: Frame Assembly
Assemble the main drone frame arms to the central hub using provided fasteners.

Use thread locker on screws to prevent loosening from vibrations.

Confirm all screws are securely tightened.

Step 2: Motor Installation
Attach brushless motors to motor mounts on each frame arm.

Secure motors firmly and verify free rotation of motor shafts.

Step 3: Power Distribution Board (PDB)
Mount the PDB at the designated frame location with standoffs.

Ensure isolation from conductive parts to avoid electrical shorts.

Step 4: Flight Controller Installation
Install the flight controller on vibration-damping mounts atop the PDB.

Verify orientation matches software configuration (forward-facing).

Step 5: Wiring
Route wiring neatly along arms, securing with zip ties or clips.

Connect motors, sensors, and power lines to the PDB and flight controller per schematic.

Step 6: Propeller Attachment
Install propellers according to motor rotation direction.

Secure with safety washers and nuts.

Step 7: Final System Checks
Inspect all mechanical and electrical connections.

Balance drone’s center of gravity.

Power on system and verify sensor and motor responses.

Parts List and Cost Estimation
Please refer to the docs/PARTS_LIST.md file for a detailed list of components, suppliers, and estimated costs.

Contribution Guidelines
We welcome contributions! Please review the CONTRIBUTING.md for information on how to report issues, request features, and submit pull requests.

License
This project is licensed under the MIT License. See LICENSE for details.
Thank you for your interest in IonStar! Together, we are pushing the boundaries of autonomous drone technology for space exploration. 🌌
