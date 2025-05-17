# IonStar Software Build and Run Guide

## Overview
This document explains how to set up, build, and run the IonStar drone control software on a development machine. All work is done in Python 3.9+.

---

## Prerequisites

- Python 3.9 or newer installed on your system.
- Git to clone the repository.
- Optional: A virtual environment tool (venv, virtualenv, conda) for dependency isolation.

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/BryceWDesign/IonStar.git
cd IonStar
```

2. **Create and activate a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows PowerShell
```

3. **Install dependencies**

Currently, IonStar uses only standard Python libraries but you may extend with third-party packages later.

```bash
pip install -r requirements.txt  # If requirements.txt added later
```

4. **Run the main control script**

```bash
python src/main.py
```

You should see:

```
IonStar control stack initializing…
```

---

## Testing

Run basic tests to verify import and setup:

```bash
python -m unittest discover tests
```

---

## Development Notes

- Source code lives in `src/`.
- Tests live in `tests/`.
- Add feature modules incrementally and update `main.py` to integrate.

---

## Next Steps

- Implement control algorithms.
- Integrate VR remote interface.
- Add energy harvesting subsystem simulation.

---

For questions or contributions, see `CONTRIBUTING.md`.

