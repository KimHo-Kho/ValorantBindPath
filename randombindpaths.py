"""
Purely random path from spawn to designated site

Kim Ho
10/10/2023

"""

import random

class MapGraph:
    def __init__(self):
        self.adj_list = {}

    def add_location(self, location):
        self.adj_list[location] = set()  # Use sets instead of lists for connections

    def add_connection(self, location1, location2, bidirectional=True):
        self.adj_list[location1].add(location2)
        if bidirectional:
            self.adj_list[location2].add(location1)

    def print_map(self):
        for location, connections in self.adj_list.items():
            print(f"{location} is connected to: {', '.join(connections)}")

    def get_random_path_to_site(self, site):
        current_location = "Attacker Spawn"
        path = [current_location]

        while current_location != site:
            # Get available connections for the current location
            connections = self.adj_list[current_location]

            # Filter out connections that lead to the site
            available_paths = [connection for connection in connections if connection == site]

            # If no direct path to the site, choose a random path
            if not available_paths:
                available_paths = list(connections)

            # Choose a random connection
            next_location = random.choice(available_paths)

            # Move to the next location
            current_location = next_location
            path.append(current_location)

        return path


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

# Call the function to initiate the process
chosen_site = choose_site()

# Create the map graph
map_graph = MapGraph()

# B Exit means it leads to B Site, A Exit means that it leads to A Site
# B TP means that the tp is on B Long, A TP means the one on A Site
# Add locations
locations = ["A Short", "B Short", "A Tower", "A Lamps", "A Site",
             "B Site", "B Garden", "A Bath",
             "Market", "B Long", "Hookah", "A Lobby", "B Lobby",
             "B Elbow", "A TP", "B TP",
             "Attacker Spawn", "Defender Spawn"]
for location in locations:
    map_graph.add_location(location)

# Add connections
connections = [
    # one direction (TP)
    ("A Site", "A TP", False), 
    ("B Long", "B TP", False), 
    ("B TP", "A Lobby", False),
    ("A TP", "B Short", False),

    # These connections are bidirectional
    ("A Short", "Market"), ("A Short", "A Site"), ("A Short", "A Lobby"),
    ("B Short", "Hookah"), ("B Short", "B Lobby"), ("B Short", "Market"),  
    ("A Site", "A Tower"), ("A Site", "A Lamps"), ("A Site", "A Bath"),
    ("B Site", "B Elbow"), ("B Site", "B Garden"), ("B Site", "Hookah"), ("B Elbow", "B Site"),
    ("Market", "B Short"), ("Market", "A Short"), ("Attacker Spawn", "A Lobby"), 
    ("B Long", "B Garden"), ("B Garden", "B Site"),
    ("Attacker Spawn", "A Lobby"), ("Attacker Spawn", "Market"), 
    ("Attacker Spawn", "B Lobby"),
    ("Defender Spawn", "A Tower"), ("Defender Spawn", "B Site"), ("Defender Spawn", "B Elbow"), 
    ("A Tower", "A Site")
]

for connection in connections:
    map_graph.add_connection(connection[0], connection[1])

# Print the map
map_graph.print_map()

# Function to generate a random path to a designated site
def generate_random_path_to_site(site):
    path = map_graph.get_random_path_to_site(site)
    print("Random path to", site)
    print(" -> ".join(path))

# Call the function to generate a random path to the chosen site
generate_random_path_to_site(chosen_site)
