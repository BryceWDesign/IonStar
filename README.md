# IonStar – Next‑Generation Space Drone

**IonStar** is an open‑source space‑and‑atmosphere drone engineered for high‑speed, autonomous missions. It fuses Hall‑effect ion propulsion, ambient‑energy harvesting, and VR‑ready control into a single sub‑10 kg platform intended for SpaceX‑class exploration and real‑time astronaut support.

## Key Features
- **Ion Propulsion:** Miniaturized Hall thrusters (Isp 1600–3000 s) delivering up to 90 000 mph exhaust velocity for silent deep‑space acceleration.  
- **Ambient Energy Scythe Core:** Multi‑layer photovoltaic skin, RF/particle siphon coils, and thermoelectric scavengers—enabling indefinite operation without refueling.  
- **Dual‑Mode Flight:** Racing‑grade brushless motors + folding props for atmospheric agility; automatic switch to ion mode in vacuum.  
- **VR Remote Ops:** Starlink‑compatible low‑latency video, haptic feedback, and gesture override for astronaut or ground control.  
- **Modular Frame:** Graphene‑carbon composite delta wing with hex‑core spine; hot‑swap payload bay for sensors or tools.  

## Objectives
1. Demonstrate cost‑effective ion propulsion on a drone scale.  
2. Validate ambient energy harvesting for perpetual power.  
3. Provide an open platform for research, racing, and mission support.  

## Repository Layout
```
/src          – flight software, VR interface, AI nav  
/hardware     – CAD, PCB, STL, BOM  
/docs         – schematics, white‑papers, UX flows  
/tests        – unit + hardware‑in‑loop tests  
/examples     – demo missions, configs  
LICENSE       – MIT License  
```

## Getting Started
No local installs needed—everything is web‑based. See `/docs/setup_web.md` for browser‑only workflow.

## License
IonStar is released under the MIT License – see the [LICENSE](LICENSE) file for details.
