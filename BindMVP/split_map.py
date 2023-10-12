from map_graph import MapGraph
from user_input import choose_site
import random

# Function to generate a random path to a designated site
def generate_random_path_to_site(site, chosen, map_graph):
    path = map_graph.get_random_path_to_site(site, chosen)
    print("Random path to", site)
    print(" -> ".join(path))

def run_split_map():
    # Create the map graph for Split
    map_graph = MapGraph()

    # Add locations for Split
    locations = ["A Main", "B Main", "A Lobby", "B Lobby",
                "A Site", "B Site", "Market", "Sewers", "Mid",
                "B Heaven", "A Heaven", "Defender Spawn"]
    for location in locations:
        map_graph.add_location(location)

        # Add connections with weight 1 and direction
    connections = [
        # These connections are bidirectional
        ("B Lobby", "Market", True, 1), 
        ("B Lobby", "B Main", True, 1), 
        ("B Main", "B Heaven", True, 1), 
        ("B Site", "B Heaven", True, 1),

        ("Mid", "B Heaven", True, 1), 
        ("Mid", "A Heaven", True, 1), 
        ("Mid", "Market", True, 1), 
        ("Mid", "Sewers", True, 1), 

        ("A Lobby", "Sewers", True, 1),
        ("A Lobby", "A Main", True, 1),
        ("A Main", "A Heaven", True, 1),
        ("A Main", "A Site", True, 1),

        ("Defender Spawn", "A Heaven", True, 1), 
        ("Defender Spawn", "B Heaven", True, 1), 
        ("Defender Spawn", "B Site", True, 1), 
        ("Defender Spawn", "A Site", True, 1)
    ]

    for connection in connections:
        map_graph.add_connection(connection[0], connection[1], connection[2], connection[3])

    # Print the map for Split
    map_graph.print_map()

    cont = True
    while cont:
        # Call the function to get the chosen site
        chosen_site = choose_site(2)

        # Call the function to generate a random path to the chosen site
        starting_points = ["B Lobby", "A Lobby", "Mid"]
        chosen_starting_point = random.choice(starting_points)
        print(chosen_starting_point)
        generate_random_path_to_site(chosen_site, chosen_starting_point, map_graph)
        
        # Ask if the user wants to continue
        user_input = input("Do you want to generate another random path? Press Enter to continue, or type 'gg' to exit: ").strip().lower()
        cont = (user_input != 'gg')
