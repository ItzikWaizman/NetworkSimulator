import random

class Parameters:
    def __init__(self):     
        self.params = dict()

        """ Network Topology Parameters """

        # nodes - List of non negative integers, each represent a node id in the network.
        self.params['nodes'] = [0, 1, 2, 3, 4, 5]

        # links - Dictionary containing the nodes each link connects and the corresponding capacity.
        self.params['links'] = [{'node1': 0, 'node2': 1, 'capacity': 1},
                                {'node1': 1, 'node2': 2, 'capacity': 1},
                                {'node1': 2, 'node2': 3, 'capacity': 1},
                                {'node1': 3, 'node2': 4, 'capacity': 1},
                                {'node1': 4, 'node2': 5, 'capacity': 1}]
        
        # users - Dictionary containing each user id, source node, destination node, and the path between these nodes.
        # Note that a path cannot contain links that do not exists in params['links'].
        self.params['users'] = [
            {'user_id': 0, 'source': 0, 'destination': 5, 'path': [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]},
            {'user_id': 1, 'source': 0, 'destination': 1, 'path': [(0, 1)]},
            {'user_id': 2, 'source': 1, 'destination': 2, 'path': [(1, 2)]},
            {'user_id': 3, 'source': 2, 'destination': 3, 'path': [(2, 3)]},
            {'user_id': 4, 'source': 3, 'destination': 4, 'path': [(3, 4)]},
            {'user_id': 5, 'source': 4, 'destination': 5, 'path': [(4, 5)]}
        ]

        """ Simulation Parameters """

        # alpha - Nonegative number for the alpha-fairness criterion.
        self.params['alpha'] = 2

        # iterations - Integer describing the upper limit of the number of iterations.
        self.params['iterations'] = 20000

        # step_size - Float describing the step size in gradient descent/ascent algorithms.
        self.params['step_size'] = 5e-4

        # algorithm - String indicating the type of algorithm. Supported algorithms are 'primal' and 'dual'.
        self.params['algorithm'] = 'primal'

        self.params['max_rate_update'] = 0.3
 
        """" Barrier function parameters """
        # normalization_factor - Float. Constant to normalize barrier function values in the feasible region.
        self.params['normalization_factor'] = 4e-6
        self.params['beta'] = 20