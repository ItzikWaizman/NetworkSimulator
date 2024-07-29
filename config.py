import random
import json

class Parameters:
    def __init__(self, config_path=None):
        self.params = dict()

        if config_path:
            self.load_params_from_file(config_path)
        else:
            self.set_default_params()

    def set_default_params(self):
        """ Network Topology Parameters """
        self.params['nodes'] = [0, 1, 2, 3, 4, 5]
        self.params['links'] = [{'node1': 0, 'node2': 1, 'capacity': 1},
                                {'node1': 1, 'node2': 2, 'capacity': 1},
                                {'node1': 2, 'node2': 3, 'capacity': 1},
                                {'node1': 3, 'node2': 4, 'capacity': 1},
                                {'node1': 4, 'node2': 5, 'capacity': 1}]
        self.params['users'] = [
            {'user_id': 0, 'source': 0, 'destination': 5, 'path': [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]},
            {'user_id': 1, 'source': 0, 'destination': 1, 'path': [(0, 1)]},
            {'user_id': 2, 'source': 1, 'destination': 2, 'path': [(1, 2)]},
            {'user_id': 3, 'source': 2, 'destination': 3, 'path': [(2, 3)]},
            {'user_id': 4, 'source': 3, 'destination': 4, 'path': [(3, 4)]},
            {'user_id': 5, 'source': 4, 'destination': 5, 'path': [(4, 5)]}
        ]
        self.params['shortest_path_algorithm'] = 'dijkstra'
        self.params['alpha'] = 1
        self.params['iterations'] = 200
        self.params['step_size'] = 5e-1
        self.params['algorithm'] = 'dual'
        self.params['normalization_factor'] = 4e-6
        self.params['beta'] = 20
        self.params['max_rate_update'] = 0.1
        self.params['rate_upper_bound'] = 100

    def load_params_from_file(self, config_path):
        with open(config_path, 'r') as file:
            self.params = json.load(file)

    def save_params_to_file(self, config_path):
        with open(config_path, 'w') as file:
            json.dump(self.params, file, indent=4)