# Factory Production Optimization Algorithm in Python

## Overview

This project implements a Python-based algorithm designed to optimize the process of collecting five types of materials—Wheat, Fruit, Iron, Water, and Silver—by managing the construction, upgrading, collection, and demolition of factories. The goal of the algorithm is to collect a required amount of each material in the shortest possible time by dynamically making decisions about factory production, capacity upgrades, and material collection.

The algorithm simulates the following processes:
- Building factories in a limited number of available spaces.
- Upgrading production rate and capacity of the factories.
- Collecting materials from the factories.
- Demolishing factories if necessary for optimizing production.

The logic accounts for simultaneous actions, different upgrade times for production and capacity, and the balance between building, upgrading, and collecting to minimize the total time required to gather the materials.

## Features

- **Dynamic Factory Management**: The algorithm builds factories for different materials and upgrades their production rates and capacities based on efficiency.
- **Simultaneous Actions**: Two actions (building/upgrading/collecting) can be performed simultaneously, as allowed by game rules.
- **Optimal Collection**: Materials are collected from factories once they reach 25% of their capacity, ensuring continuous production.
- **Upgrade Strategy**: The algorithm determines the best time to upgrade factory production or capacity based on efficiency gains.
- **Configurable Design**: The base production rate and required materials for each game session are configurable, allowing the algorithm to be reused with different scenarios.

## Project Structure

The project contains two main files:

- **`factory.py`**: Defines the `Factory` class and methods for building, upgrading, collecting, and demolishing factories.
- **`game.py`**: Contains the simulation logic, including the main algorithm that optimizes factory management based on the rules provided.

```
factory_production_optimization/
│
├── factory.py       # Factory class and operations for building, upgrading, and collecting materials
├── game.py          # Main simulation logic for optimizing factory actions
├── README.md        # Documentation and setup instructions
└── requirements.txt # (Optional) Dependencies for the project, if any
```

## Prerequisites

- Python 3.x
- (Optional) Required dependencies (listed in `requirements.txt`)

### Installing Dependencies

If any external dependencies are required, they can be installed with:

```bash
pip install -r requirements.txt
```

## Setup and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/Juliusmidega/factory-production-optimization-python.git
cd factory-production-optimization-python
```

### Step 2: Run the Simulation

You can execute the simulation by running:

```bash
python game.py
```

### Step 3: Customize Material Requirements

You can modify the material requirements and base production rates directly in `game.py`:

```python
materials_required = {
    "wheat": 75700,
    "fruit": 219000,
    "iron": 206000,
    "water": 164000,
    "silver": 86300
}

base_production_rates = {
    "wheat": 14.017,  # units per minute
    "fruit": 42.733,
    "iron": 40.217,
    "water": 31.733,
    "silver": 16.133
}
```

Adjust these values to simulate different game scenarios and optimize production accordingly.

### Step 4: View Results

Once you run the simulation, the output will display a step-by-step breakdown of the factory management process and show the total time taken to gather the required materials. The algorithm ensures optimal time management across all actions.

## How the Algorithm Works

1. **Factory Construction**: The algorithm selects which factories to build based on material demand and available space.
2. **Upgrading**: It upgrades factories' production rates and capacities based on which actions would yield the highest efficiency.
3. **Material Collection**: It collects materials when the factories reach 25% of their capacity to maximize production uptime.
4. **Simultaneous Actions**: The algorithm ensures no more than two actions are happening at once (building, upgrading, or collecting).
5. **Demolition**: Once the required material is gathered, unnecessary factories are demolished to free up space for other needed factories.

## Example Scenario

To simulate the collection of materials based on the given base production rates and required materials, run the default configuration in `game.py`:

```python
materials_required = {
    "wheat": 75700,
    "fruit": 219000,
    "iron": 206000,
    "water": 164000,
    "silver": 86300
}

base_production_rates = {
    "wheat": 14.017,  # units per minute
    "fruit": 42.733,
    "iron": 40.217,
    "water": 31.733,
    "silver": 16.133
}
```

The algorithm will calculate the optimal way to gather the materials and output the total time taken for completion.

## Future Enhancements

- **Graphical User Interface**: A future version could include a graphical interface to visualize the building and upgrading processes.
- **Additional Factory Types**: Extend the system to include more complex factory types and production strategies.
- **Performance Optimization**: Improvements for handling larger datasets or more complex scenarios could be added.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

Developed by [Julius Midega](https://github.com/Juliusmidega3).

---

This **README** follows the format of the example you provided, with all the required sections and an explanation of the Python code structure and functionality. Let me know if you need further changes!
