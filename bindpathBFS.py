""" 
Choose starting and ending point
first 3 steps are random with weighted edges
then BFS to get to designated site

Kim Ho
10/10/2023

"""

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

# Function to get the user's choice of site
def choose_site():
    # List of available sites
    sites = ["A Site", "B Site"]

    # Ask the user to choose a site
    print("Which site do you want to hit? (A/B)")
    choice = input().strip().upper()

    if choice in ['A', 'B']:
        print(f"You chose to hit {sites[ord(choice) - ord('A')]}.")
        return sites[ord(choice) - ord('A')]  # Return the chosen site
    else:
        # If no valid choice, randomly select a site
        random_site = random.choice(sites)
        print(f"No valid choice. Randomly selected to hit {random_site}.")
        return random_site  # Return the randomly selected site

# Function to generate a random path to a designated site
def generate_random_path_to_site(site, chosen, map_graph):
    path = map_graph.get_random_path_to_site(site, chosen)
    print("Random path to", site)
    print(" -> ".join(path))

# Main function to set up the map and generate a random path to a site
def main():
    # Create the map graph
    map_graph = MapGraph()

    # Add locations
    locations = ["A Short", "B Short", "A Tower", "A Lamps", "A Site",
                "B Site", "B Garden", "A Bath",
                "Market", "B Long", "Hookah", "A Lobby", "B Lobby",
                "B Elbow", "A TP", "B TP",
                "Attacker Spawn", "Defender Spawn"]
    for location in locations:
        map_graph.add_location(location)

    # Add connections with weight 1 and direction
    connections = [
        ("A Short", "A TP", False, 2), 
        ("B Long", "B TP", False, 2), 
        ("B TP", "A Lobby", False, 1),
        ("A TP", "B Short", False, 1),
        ("Attacker Spawn", "A Lobby", False, 1), 
        ("Attacker Spawn", "Market", False, 1), 
        ("Attacker Spawn", "B Lobby", False, 1),

        # These connections are bidirectional
        ("B Lobby", "A Lobby", True, 1),
        ("A Short", "Market", True, 1), 
        ("A Short", "A Site", True, 1), 
        ("A Short", "A Lobby", True, 1),
        ("B Short", "Hookah", True, 1), 
        ("B Short", "B Lobby", True, 1), 
        ("B Short", "Market", True, 1),  
        ("A Site", "A Tower", True, 1), 
        ("A Site", "A Lamps", True, 1), 
        ("A Site", "A Bath", True, 1),
        ("B Site", "B Elbow", True, 1), 
        ("B Site", "B Garden", True, 1), 
        ("B Site", "Hookah", True, 1), 
        ("B Elbow", "B Site", True, 1),
        ("Market", "B Short", True, 1), 
        ("Market", "A Short", True, 1), 
        ("B Long", "B Garden", True, 1), 
        ("B Garden", "B Site", True, 1), 
        ("B Lobby", "B Long", True, 1),
        ("Defender Spawn", "A Tower", True, 1), 
        ("Defender Spawn", "B Site", True, 1), 
        ("Defender Spawn", "B Elbow", True, 1), 
        ("A Tower", "A Site", True, 1)
    ]

    for connection in connections:
        map_graph.add_connection(connection[0], connection[1], connection[2], connection[3])

    # Print the map
    map_graph.print_map()

    cont = True
    while cont:
        # Call the function to get the chosen site
        chosen_site = choose_site()

        # Call the function to generate a random path to the chosen site
        # starting_points = ["B Lobby", "A Lobby"]
        starting_points = ["B TP", "B Short", "B Long", "A TP", "A Short"]
        chosen_starting_point = random.choice(starting_points)
        print(chosen_starting_point)
        generate_random_path_to_site(chosen_site, chosen_starting_point, map_graph)
        
        # Ask if the user wants to continue
        user_input = input("Do you want to generate another random path? Press Enter to continue, or type 'gg' to exit: ").strip().lower()
        cont = (user_input != 'gg')


# Entry point
if __name__ == "__main__":
    main()
