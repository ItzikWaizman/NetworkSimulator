import networkx as nx
import heapq
from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self, network, alpha, step_size):
        self.network = network
        self.alpha = alpha
        self.step_size = step_size
        self.update_users_paths()
        self.print_users_paths()

    @abstractmethod
    def update(self, user):
        """Update the rates for the network based on the algorithm's logic."""
        pass

    @abstractmethod
    def run(self, iterations):
        """Run the algorithm for a specified number of iterations."""
        pass

    def update_users_paths(self):
        for user in self.network.users:
            if user.path is None:
                user.path = self.find_shortest_path(user, algo=self.network.shortest_path_algorithm)

    def print_users_paths(self):
        for user in self.network.users:
            path_str = " -> ".join(f"{u}->{v}" for u, v in user.path)
            print(f"User {user.user_id}: {path_str}")

    def find_shortest_path(self, user, algo):
        G = self.network.graph
 
        if algo == 'dijkstra':
            predecessors = self.dijkstra(user.source, G)

        elif algo == 'bellman_ford':
            predecessors = self.bellman_ford(user.source, G)

        else:
            raise ValueError(f"Unsupported algorithm type: {algo}")

        if predecessors[user.destination] is None:
            raise ValueError(f"There is not path to node {user.destination}")
        
        # Reconstruct the path from source to destination
        path = []
        current = user.destination
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
                weight = G[u][v]['weight']
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                elif distances[v] + weight < distances[u]:  # Considering undirected graph
                    distances[u] = distances[v] + weight
                    predecessors[u] = v

        # Check for negative weight cycles
        for u, v in G.edges:
            weight = G[u][v]['weight']
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
            if distances[v] + weight < distances[u]:  # Considering undirected graph
               raise ValueError("Graph contains a negative weight cycle")
                
            
        return predecessors
