from map_graph import MapGraph
from user_input import choose_site
import random

# Function to generate a random path to a designated site
def generate_random_path_to_site(site, chosen, map_graph):
    path = map_graph.get_random_path_to_site(site, chosen)
    print("Random path to", site)
    print(" -> ".join(path))

def run_lotus_map():
    # Create the map graph for Lotus
    map_graph = MapGraph()

    # Add locations for Lotus
    locations = ["A Site", "B Site", "C Site",
                "A Lobby", "B Lobby", "C Lobby",
                "A Main", "B Main", "C Main",
                "Tree", "A Link", "C Link",
                "Defender Spawn", "Attacker Spawn"]
    for location in locations:
        map_graph.add_location(location)

        # Add connections with weight 1 and direction
    connections = [
        # These connections are bidirectional
        ("Attacker Spawn", "A Lobby", True, 1),
        ("Attacker Spawn", "B Lobby", True, 1),
        ("Attacker Spawn", "C Lobby", True, 1),

        ("A Lobby", "A Main", True, 1), ("A Main", "A Site", True, 1), 
        ("B Lobby", "B Main", True, 1), ("B Main", "B Site", True, 1), 
        ("C Lobby", "C Main", True, 1), ("C Main", "C Site", True, 1), 

        ("B Main", "C Main", True, 2),

        ("Tree", "A Main", True, 1), ("Tree", "A Site", True, 1),
        ("A Main", "A Link", True, 2), ("C Site", "C Link", True, 2),
        ("B Site", "A Link", True, 2), ("B Site", "C Link", True, 2)

        # ("Defender Spawn", "A Site", True, 1), 
        # ("Defender Spawn", "B Site", True, 1), 
        # ("Defender Spawn", "C Site", True, 1), 
        # ("Defender Spawn", "A Main", True, 1), 
        # ("Defender Spawn", "C Link", True, 1)
    ]

    for connection in connections:
        map_graph.add_connection(connection[0], connection[1], connection[2], connection[3])

    # Print the map for Lotus
    map_graph.print_map()

    cont = True
    while cont:
        # Call the function to get the chosen site
        chosen_site = choose_site(3)

        # Call the function to generate a random path to the chosen site
        starting_points = ["A Lobby", "B Lobby", "C Lobby"]
        chosen_starting_point = random.choice(starting_points)
        print(chosen_starting_point)
        generate_random_path_to_site(chosen_site, chosen_starting_point, map_graph)
        
        # Ask if the user wants to continue
        user_input = input("Do you want to generate another random path? Press Enter to continue, or type 'gg' to exit: ").strip().lower()
        cont = (user_input != 'gg')
