import random
from algorithms.algorithm_base import Algorithm
import numpy as np

class PrimalAlgorithm(Algorithm):
    def __init__(self, network, alpha, step_size, normalization_factor, beta, max_rate_update):
        super().__init__(network, alpha, step_size)
        self.normalization_factor = normalization_factor
        self.beta = beta
        self.max_rate_update = max_rate_update
        self.epsilon = 0.01 # Used for computation stability

    def calc_rate_update(self, user):
        grad = self.compute_gradient(user)
        rate_update = self.step_size * grad
        if np.abs(rate_update) > self.max_rate_update:
            rate_update = np.sign(rate_update) * self.max_rate_update
        rate = user.rate + rate_update
        if rate <= 0: 
            rate = 0 + self.epsilon
        if rate >= 1:
            rate = 1 - self.epsilon
        return rate

    def run(self, iterations):
        rate_history = {user.user_id: [] for user in self.network.users}
        self.W_values = []
        
        for _ in range(iterations):
            user = random.choice(self.network.users)
            rate = self.calc_rate_update(user)
            user.update_rate(rate)
            for user in self.network.users:
                rate_history[user.user_id].append(user.rate)

        return rate_history
    
    def compute_gradient(self, user):
        grad_utility = (user.rate + self.epsilon) ** (-self.alpha)
        grad_barrier = sum(self.barrier_derivative(self.network.get_total_rate_on_link(link), link.capacity) for link in self.network.links if (link.node1, link.node2) in user.path or (link.node2, link.node1) in user.path)
        return grad_utility - grad_barrier
    
    def barrier_derivative(self, rate_sum, capacity):
        return self.beta * self.normalization_factor * (np.exp(self.beta * (rate_sum - (capacity/2))) - np.exp(-self.beta * (rate_sum - (capacity/2))))
