import networkx as nx
import matplotlib.pyplot as plt
import random

class Link:
    def __init__(self, node1, node2, capacity):
        self.capacity = capacity
        self.node1 = node1
        self.node2 = node2


class User:
    def __init__(self, user_id, source, destination, path):
        self.user_id = user_id
        self.source = source
        self. destination = destination
        self.path = path
        self.rate = 0
    
    def update_rate(self, rate):
        self.rate = rate


class Network:
    def __init__(self, params):
        self.nodes = params['nodes']

        self.links = [Link(node1=link['node1'],
                           node2=link['node2'],
                           capacity=link['capacity']) for link in params['links']]
        
        self.users = [User(user_id=user['user_id'],
                           source=user['source'],
                           destination=user['destination'],
                           path=[tuple(p) for p in user['path']]) for user in params['users']]
        
        self.graph = self.build_graph()
        self.position = None  # To store positions for visualization
    
    def build_graph(self):
        G = nx.Graph()
        for link in self.links:
            G.add_edge(link.node1, link.node2, capacity=link.capacity)
        return G

    def visualize_network(self):
        if self.position is None:
            self.position = nx.spring_layout(self.graph)  # Spring layout for better visualization
        capacities = nx.get_edge_attributes(self.graph, 'capacity')
        nx.draw(self.graph, self.position, with_labels=True, node_size=700, node_color="lightblue", font_size=10)
        nx.draw_networkx_edge_labels(self.graph, self.position, edge_labels=capacities)
        plt.show()

    def get_total_rate_on_link(self, link):
        total_rate = 0
        for user in self.users:
            if (link.node1, link.node2) in user.path:
                total_rate += user.rate
        return total_rate