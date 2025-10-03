# Earth-Satellite Orbit Simulation

This project simulates the orbit of a satellite around the Earth using Newtonian physics. The simulation is visualized with a graphical user interface (GUI) built with Tkinter, allowing users to experiment with different initial velocities and time steps to observe how the satellite's trajectory changes.

## Features
- Realistic simulation of satellite motion under Earth's gravity
- Interactive GUI for inputting initial velocity and time step
- Visualization of the satellite's orbit and Earth
- Adjustable coordinate system display
- Calculation of maximum distance and orbital period

## How to Run
To start the simulation, execute the `Model_Erde_Satellit.py` file. This is the main executable and will launch the GUI.

```bash
python Model_Erde_Satellit.py
```

## Requirements
Before running the simulation, make sure you have the following installed:
- Python 3.x
- Tkinter (usually included with Python)
- Pillow (for image support)

You can install Pillow with:
```bash
pip install pillow
```

## Notes
- The simulation uses an image file `earth64x64.png` for visualization. Make sure this file is present in the same directory as `Model_Erde_Satellit.py`.
- The GUI is in German, but the controls are intuitive: enter the initial velocity (in m/s) and the time step (in simulated seconds), then press "Start" to begin the simulation.

## Author
Leander Steffan
