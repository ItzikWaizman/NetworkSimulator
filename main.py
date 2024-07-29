import argparse
import os
from config import Parameters
from simulation import Simulator

def main(config_path=None):
    # Create an instance of Parameters
    Params = Parameters(config_path)
    
    # Create an instance of Simulator using the parameters
    simulator = Simulator(Params.params)
    
    # Print the simulation details
    #simulator.print_simulation_details()
    
    # Visualize the network to check if it initializes correctly
    simulator.run_simulation()
    
    # Initialize and run the algorithm specified in the parameters
    simulator.post_simulation()

    Params.save_params_to_file('simulations_config_files/dual_alpha1.json')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Network Simulator')
    parser.add_argument('--config', type=str, help='Path to the config file')
    args = parser.parse_args()

    config_path = args.config if args.config else None
    main(config_path)