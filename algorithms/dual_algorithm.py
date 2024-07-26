import random
from algorithms.algorithm_base import Algorithm

class DualAlgorithm(Algorithm):
    def __init__(self, network, alpha, step_size, rate_upper_bound):
        super().__init__(network, alpha, step_size)
        self.lambda_values = {link: 1 for link in self.network.links}
        self.rate_upper_bound = rate_upper_bound
        self.update_rates() # Initialize users rates according to initial lambda_values

    def update_rates(self):
        rates = self.calculate_rates()
        for user in self.network.users:
            user.update_rate(rates[user.user_id])

    def calculate_rates(self):
        rates = {}
        for user in self.network.users:
            lambda_sum = sum(self.lambda_values[link] for link in self.network.links if (link.node1, link.node2) in user.path or (link.node2, link.node1) in user.path)
            rates[user.user_id] = lambda_sum ** (-1 / self.alpha) if lambda_sum is not 0 else self.rate_upper_bound
        return rates
    
    def update(self, link):
        """ Update Lagrange multiplier and users rates in accordance with the dual algorithm update rule"""
        y_l = self.network.get_total_rate_on_link(link)
        c_l = link.capacity
        lambda_l = self.lambda_values[link]
        self.lambda_values[link] = max(lambda_l + self.step_size * (y_l-c_l),0)
        self.update_rates()

    def run(self, iterations):
        rate_history = {user.user_id: [] for user in self.network.users}

        for _ in range(iterations):
            link = random.choice(list(self.network.links))
            self.update(link)
            for user in self.network.users:
                rate_history[user.user_id].append(user.rate)

        return rate_history

