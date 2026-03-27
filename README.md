# Forest Fire Simulation using Cellular Automata

This project models the spread of a forest fire using a **cellular automata approach**. It simulates how fire propagates across a grid of trees based on local interaction rules and probabilistic behaviour.

---

## Features

* Grid-based forest fire simulation
* Probabilistic fire spread between neighbouring cells
* Visual representation of fire progression
* Cross-platform support (Windows, macOS, Linux)
* Optional Docker support for consistent environments

---

## Model Overview

The simulation represents a forest as a 2D grid where each cell can be in one of three states:

* Tree
* Burning
* Empty

### Rules:

* A burning tree turns into an empty cell
* A tree ignites if at least one neighbour is burning
* Fire spread is influenced by probability

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/forest-fire-model.git
cd forest-fire-model
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Simulation

---

### Option 1: Run the Graphical Interface (requires CAPyle)

The project includes a **graphical interface** for running cellular automata simulations:

1. **Download** `CAPyle_releaseV2` from CAPyle releases and place it in the project directory or a known path.
2. **Run the run_tool.py script:**

```bash
python run_tool.py
```

---

### Option 2: Run using Docker (optional)

If you prefer using Docker:

1. Install Docker Desktop:
   https://www.docker.com/products/docker-desktop/

2. Run the appropriate script for your OS:

* Windows:

```bash
.\windows.bat
```

* Linux:

```bash
./linux.sh
```

* macOS:

```bash
./mac.sh
```

Then inside the container:

```bash
python run.py
```

---

## Visual Output

The simulation displays the spread of fire over time using a graphical interface.

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* (Optional) CAPyLE framework

---

## Notes

This project was developed as an independent extension of an academic exercise and has been adapted into a standalone simulation.

---

## Future Improvements

* Wind direction and speed effects
* Variable terrain and fuel density
* Real-world data integration
* Performance optimisation for large grids

---

## License

This project is open-source and available for educational and personal use.
