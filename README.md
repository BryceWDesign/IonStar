# 🚀 IonStar – Next‑Generation Space Drone

[![CI Status](https://github.com/BryceWDesign/IonStar/actions/workflows/ci.yml/badge.svg)](../../actions)

IonStar is an open‑source, energy‑autonomous drone purpose‑built for space missions and high‑performance atmospheric flight.  
Combining **ion propulsion**, **ambient energy harvesting**, and **VR remote control**, IonStar aims to out‑pace and out‑last conventional spacecraft while remaining lightweight and low‑cost.

---

## ✨ Key Capabilities
| Feature | Highlights |
|---------|------------|
| **Dual‑Mode Flight** | Racing‑grade brushless fans for atmosphere; Hall‑effect ion thrusters for vacuum. |
| **Ambient Energy Scythe Core** | Triboelectric mesh + radiant absorber + graphene supercaps → perpetual power. |
| **VR Ops** | Low‑latency stereo video, haptics, and full headset control for astronauts or ground crews. |
| **Modular Frame** | Carbon‑fiber delta shell with swappable payload bay (< 2.5 kg target mass). |
| **Open & Hackable** | MIT‑licensed code, CAD, and PCB files—perfect for research, racing, or off‑world utility bots. |

---

## 📂 Repository Layout
IonStar/
├── src/ # Control, energy, comm modules
├── hardware/
│ ├── bom.csv # Parts & pricing
│ ├── assembly_guide.md # Step‑by‑step build
│ └── schematics/ # Wiring & PCB docs
├── docs/
│ ├── build_software.md # Dev setup & test guide
│ ├── build_hardware.md # Full hardware build HOW‑TO
│ ├── power_system.md # Ambient energy theory & design
│ ├── vr_control.md # VR control system overview
│ └── parts_costs.md # Professional parts list
├── tests/ # Unit & HIL tests
├── .github/workflows/ci.yml
├── LICENSE
└── README.md

---

## 🛠️ Quick Start

### Software Simulation
```bash
git clone https://github.com/BryceWDesign/IonStar.git
cd IonStar
python src/main.py
Runs a 10‑cycle demo loop printing energy harvest, VR commands, and telemetry.

Browser‑Only Contribution
Press . on any repo page to open github.dev.

Follow docs/build_software.md for details.

Submit pull requests—CI tests run automatically.

🧩 Build It IRL
Review hardware/bom.csv and docs/parts_costs.md for sourcing.

Follow hardware/assembly_guide.md step by step.

Flash the control stack (src/) onto the Pixhawk (or your MCU).

Strap in, power up, and go orbital 🛰️.

🤝 Contributing
We welcome PRs, issues, and ambitious forks—see CONTRIBUTING.md and CODE_OF_CONDUCT.md for guidelines.
📜 License
Released under the MIT License – use it, hack it, fly it, improve it.

IonStar: built for the stars, by the community.
