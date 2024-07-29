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

        self.params['nodes'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.params['links'] = [{'node1': 0, 'node2': 1, 'capacity': 1/4},
                                {'node1': 0, 'node2': 7, 'capacity': 1/8},
                                {'node1': 1, 'node2': 2, 'capacity': 1/8},
                                {'node1': 1, 'node2': 7, 'capacity': 1/11},
                                {'node1': 2, 'node2': 3, 'capacity': 1/7},
                                {'node1': 2, 'node2': 8, 'capacity': 1/2},
                                {'node1': 2, 'node2': 5, 'capacity': 1/4},
                                {'node1': 3, 'node2': 4, 'capacity': 1/9},
                                {'node1': 3, 'node2': 5, 'capacity': 1/14},
                                {'node1': 4, 'node2': 5, 'capacity': 1/10},
                                {'node1': 5, 'node2': 6, 'capacity': 1/2},
                                {'node1': 6, 'node2': 8, 'capacity': 1/6},
                                {'node1': 6, 'node2': 7, 'capacity': 1},
                                {'node1': 7, 'node2': 8, 'capacity': 1/7}]
        
        self.params['users'] = [{'user_id': 0, 'source': 0, 'destination': 1, 'path': None},
                                {'user_id': 1, 'source': 0, 'destination': 2, 'path': None},
                                {'user_id': 2, 'source': 0, 'destination': 3, 'path': None},
                                {'user_id': 3, 'source': 0, 'destination': 4, 'path': None},
                                {'user_id': 4, 'source': 0, 'destination': 5, 'path': None},
                                {'user_id': 5, 'source': 0, 'destination': 6, 'path': None},
                                {'user_id': 6, 'source': 0, 'destination': 7, 'path': None},
                                {'user_id': 7, 'source': 0, 'destination': 8, 'path': None}]
        
        self.params['shortest_path_algorithm'] = 'bellman_ford'

        """ Simulation Parameters """

        self.params['alpha'] = 1
        self.params['iterations'] = 200
        self.params['step_size'] = 5e-1
        self.params['algorithm'] = 'dual'

        """ Primal Algorithm Parameters """

        self.params['normalization_factor'] = 4e-6
        self.params['beta'] = 20
        self.params['max_rate_update'] = 0.1

        """ Dual Algorithm Parameters """
        
        self.params['rate_upper_bound'] = 100

    def load_params_from_file(self, config_path):
        with open(config_path, 'r') as file:
            self.params = json.load(file)

    def save_params_to_file(self, config_path):
        with open(config_path, 'w') as file:
            json.dump(self.params, file, indent=4)