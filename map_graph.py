import random
from collections import deque

class MapGraph:
    def __init__(self):
        self.adj_list = {}

    def add_location(self, location):
        self.adj_list[location] = set()  # Use sets instead of lists for connections

    def add_connection(self, location1, location2, bidirectional, weight):
        self.adj_list[location1].add((location2, weight))
        if bidirectional:
            self.adj_list[location2].add((location1, weight))

    def print_map(self):
        for location, connections in self.adj_list.items():
            print(f"{location} is connected to: {', '.join([i[0] for i in connections])}")

    def bfs_shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_location, path = queue.popleft()
            visited.add(current_location)

            if current_location == end:
                return path

            for neighbor in self.adj_list[current_location]:
                if neighbor[0] not in visited:
                    queue.append((neighbor[0], path + [neighbor[0]]))

    # adding weights to this random choice
    def get_random_path_to_site(self, site, chosen_starting_point, max_random_steps=3):
        current_location = chosen_starting_point
        path = [current_location]

        # Perform random walk with a limit of max_random_steps
        for _ in range(max_random_steps):
            if current_location == site:
                return path

            connections = self.adj_list[current_location]
            available_paths = [connection for connection in connections if connection == site]

            if not available_paths:
                available_paths = list(connections)

            # when selecting the paths that needs to be weighted to make slightly more "random"
            # instead of avoiding TP
            next_location = random.choices(available_paths, weights=[i[1] for i in available_paths])
            current_location = next_location[0][0]
            path.append(current_location)

        # If max_random_steps reached, use BFS to find the shortest path to the site
        bfs_path = self.bfs_shortest_path(current_location, site)
        return path + bfs_path[1:]
