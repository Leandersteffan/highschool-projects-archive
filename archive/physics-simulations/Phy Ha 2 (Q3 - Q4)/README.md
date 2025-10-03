
# Half-Life Visualization

This project provides an interactive visualization of radioactive decay and half-life processes using a graphical user interface (GUI) built with Tkinter. The simulation models a chain decay:

- Substance 1 decays into Substance 2 (with its own half-life)
- Substance 2 then decays into a final, stable end substance

You can set the half-lives for both decay steps and observe how the proportions of all three substances change over time. The simulation displays both bar charts and line diagrams to illustrate the process.

## Features
- Simulates chain decay: Substance 1 → Substance 2 → End substance
- User-defined half-lives for both decay steps
- Interactive GUI for setting parameters (half-lives, calculation interval, stop threshold)
- Real-time bar chart visualization of substance proportions
- Option to display line diagrams of the decay process
- Adjustable calculation accuracy and stop conditions

## How to Run
To start the simulation, execute the `HalbwertszeitveranschaulichungLeanderSteffan.py` file. This is the main executable and will launch the GUI.

```bash
python HalbwertszeitveranschaulichungLeanderSteffan.py
```

## Requirements
Before running the simulation, make sure you have the following installed:
- Python 3.x
- Tkinter (usually included with Python)

## Usage
- Enter the half-life values for Substance 1 and Substance 2.
- Set the calculation interval (smaller values are more accurate but slower).
- Set the stop threshold (the percentage at which the simulation stops).
- Click "Set Start" to initialize, then "Start" to begin the simulation.
- Use the "Diagramme" button to display the line diagram after the simulation is complete.

## Author
Leander Steffan
