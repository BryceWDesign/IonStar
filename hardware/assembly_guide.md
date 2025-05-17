# IonStar Hardware Assembly Guide

## Introduction
This guide details the step-by-step assembly of the IonStar drone hardware components.

---

## Tools Required

- Precision screwdriver set  
- Soldering station with fine tip  
- Wire strippers and cutters  
- Heat shrink tubing and electrical tape  
- Multimeter for continuity and voltage checks  
- ESD wrist strap

---

## Assembly Steps

### Step 1: Frame Preparation
- Cut carbon fiber sheets according to CAD blueprints.
- Assemble the frame panels using fasteners from the kit.
- Double-check alignment and rigidity.

### Step 2: Mount Electronics
- Secure flight controller board inside the central cavity.
- Attach ion thrusters to the four corners, ensuring correct orientation.
- Fix ambient energy harvesters on exposed surfaces facing potential energy sources.

### Step 3: Wiring Harness
- Cut and strip wires according to the wiring diagram in `schematics/`.
- Solder connectors to wires where necessary.
- Route wires through the frame’s built-in channels.
- Use heat shrink tubing to insulate exposed connections.

### Step 4: Power System Integration
- Connect battery packs to power distribution board.
- Connect thrusters and controllers to power outputs.
- Install any necessary voltage regulators or converters.

### Step 5: Sensor Installation
- Mount IMU and other sensors on vibration-dampened mounts.
- Connect sensors to flight controller ports.

### Step 6: Final System Checks
- Verify all mechanical fasteners are secure.
- Perform continuity tests on all wiring.
- Power up system briefly to check startup sequences.
- Test communication links with ground or VR control station.

---

## Troubleshooting Tips

- If power does not reach thrusters, check connectors and solder joints.
- Ensure no short circuits before full power-up.
- Confirm sensor calibrations in software after assembly.

---

## Safety Precautions

- Always wear ESD protection.
- Handle batteries carefully; avoid puncture or overcharging.
- Follow safe soldering practices to avoid burns or damage.

---

For wiring diagrams and detailed CAD files, see the `hardware/schematics/` folder.

