import networkx as nx
import heapq
from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self, network, alpha, step_size):
        self.network = network
        self.alpha = alpha
        self.step_size = step_size

    @abstractmethod
    def update(self, user):
        """Update the rates for the network based on the algorithm's logic."""
        pass

    @abstractmethod
    def run(self, iterations):
        """Run the algorithm for a specified number of iterations."""
        pass

    def get_link_price(self, link):
        return self.network.get_total_rate_on_link(link)

    def find_shortest_path(self, user, algo='bellman_ford'):
        G = self.network.graph
        
        # Get the price for each link in the network
        link_prices = {edge: self.get_link_price(edge) for edge in G.edges}

        # Set the edge weights in the graph based on the link prices
        nx.set_edge_attributes(G, link_prices, 'weight')
 
        if algo is 'dijkstra':
            predecessors = self.dijkstra(user.source, G)

        elif algo is 'bellman_ford':
            predecessors = self.bellman_ford(user.source, G)

        else:
            raise ValueError(f"Unsupported algorithm type: {algo}")

        if predecessors[user.destination] is None:
            raise ValueError(f"There is not path to node {user.destination}")
        
        # Reconstruct the path from source to destination
        path = []
        current = user.destionation
        while predecessors[current] is not None:
            path.insert(0, (predecessors[current], current))
            current = predecessors[current]
        
        return path
    
    def dijkstra(self, source, G):
        # Initialize distances and predecessors
        distances = {node: float('inf') for node in G.nodes}
        distances[source] = 0
        predecessors = {node: None for node in G.nodes}

        # Priority queue for the nodes to visit
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in G.neighbors(current_node):
                price = G[current_node][neighbor]['weight']
                distance = current_distance + price

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return predecessors

    def bellman_ford(self, source, G):
        # Initialize distances and predecessors
        distances = {node: float('inf') for node in G.nodes}
        distances[source] = 0
        predecessors = {node: None for node in G.nodes}

        # Relax edges up to |V|-1 times
        for _ in range(len(G.nodes) - 1):
            for u, v in G.edges:
                price = G[u][v]['weight']
                if distances[u] + price < distances[v]:
                    distances[v] = distances[u] + price
                    predecessors[v] = u

        # Check for negative weight cycles
        for u, v in G.edges:
            price = G[u][v]['weight']
            if distances[u] + price < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
            
        return predecessors
