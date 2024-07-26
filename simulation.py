from config import Parameters
from network import Network
from algorithms.primal_algorithm import PrimalAlgorithm
from algorithms.dual_algorithm import DualAlgorithm
import matplotlib.pyplot as plt

class Simulator:
    def __init__(self, params):
        self.params = params
        self.network = Network(params)
        self.algorithm = self.initialize_algorithm()
        self.rate_history = None

    def initialize_algorithm(self):
        alpha = self.params['alpha']
        beta = self.params['beta']
        step_size = self.params['step_size']
        normalization_factor = self.params['normalization_factor']
        max_rate_update = self.params['max_rate_update']
        rate_upper_bound = self.params['rate_upper_bound']
        algorithm_type = self.params['algorithm']
        
        if algorithm_type == 'primal':
            return PrimalAlgorithm(self.network, alpha, step_size, normalization_factor, beta, max_rate_update)
        elif algorithm_type == 'dual':
            return DualAlgorithm(self.network, alpha, step_size, rate_upper_bound)
        else:
            raise ValueError(f"Unsupported algorithm type: {algorithm_type}")

    def run_simulation(self):
        if not self.algorithm:
            raise ValueError("Algorithm not initialized. Call initialize_algorithm first.")

        self.rate_history = self.algorithm.run(self.params['iterations'])

    def print_simulation_details(self):
        print("Simulation Details:")
        print(f"Nodes: {self.params['nodes']}")
        print(f"Links: {self.params['links']}")
        print(f"Users: {self.params['users']}")
        print(f"Iterations: {self.params['iterations']}")
        print(f"Alpha: {self.params['alpha']}")
        print(f"Algorithm Type: {self.params['algorithm']}")
        self.network.visualize_network()

    def plot_rate_history(self, rate_history):
        plt.figure(figsize=(10, 6))
        for user_id, rates in rate_history.items():
            plt.plot(rates, label=f'User {user_id}')
        plt.xlabel('Iterations')
        plt.ylabel('Rate')
        plt.title(f'User Rates over Iterations (Alpha = {self.params['alpha']})')
        plt.legend()
        plt.grid(True)
        plt.show()

    def post_simulation(self):
        print("Final Rates:")
        for user in self.network.users:
            print(f"User {user.user_id}: Rate = {user.rate}")
        self.plot_rate_history(self.rate_history)
