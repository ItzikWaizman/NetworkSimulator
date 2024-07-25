from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self, network, alpha, step_size):
        self.network = network
        self.alpha = alpha
        self.step_size = step_size

    @abstractmethod
    def calc_rate_update(self, user):
        """Update the rates for the network based on the algorithm's logic."""
        pass

    @abstractmethod
    def run(self, iterations):
        """Run the algorithm for a specified number of iterations."""
        pass
