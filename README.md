# Network Simulator with Primal and Dual Algorithms for NUM Problem

This project offers a network simulator and an implementation of the Primal and Dual algorithms to solve the Network Utility Maximization (NUM) problem.

## Features

- **Network Initialization and Visualization**: 
  - Create a network topology with nodes, links, and users based on a configuration file.
  - Visualize the network to ensure correct initialization.

- **Primal Algorithm**:
  - Implement rate updates for users based on the sum of Lagrange multipliers.
  - Calculate the objective function values over iterations.
  - Plot user rates and objective function values to visualize convergence.

- **Dual Algorithm**:
  - Use projected gradient ascent to update Lagrange multipliers while ensuring non-negative values.
  - Recalculate rates based on updated Lagrange multipliers.
  - Plot user rates and objective function values to visualize convergence.

- **Flexible Configuration**:
  - Configure network parameters, algorithm type, alpha value, step size, and number of iterations through a parameter file.

## Usage

1. **Configuration**:
   - Edit the `config.py` file to set the network parameters, including nodes, links, users, and simulation parameters.

2. **Running the Simulation**:
   - Run the `main.py` script to initialize the network, execute the specified algorithm, and visualize the results.
   ```bash
   python main.py
