from config import Parameters
from simulation import Simulator

def main():
    # Create an instance of Parameters
    Params = Parameters()
    
    # Create an instance of Simulator using the parameters
    simulator = Simulator(Params.params)
    
    # Print the simulation details
    simulator.print_simulation_details()
    
    # Visualize the network to check if it initializes correctly
    simulator.run_simulation()
    
    # Initialize and run the algorithm specified in the parameters
    simulator.post_iteration()
if __name__ == "__main__":
    main()