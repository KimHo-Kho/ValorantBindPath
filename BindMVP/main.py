from map_graph import MapGraph
from user_input import choose_site
import random

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
