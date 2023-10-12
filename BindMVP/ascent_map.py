from map_graph import MapGraph
from user_input import choose_site
import random

def generate_random_path_to_site(site, chosen, map_graph):
    path = map_graph.get_random_path_to_site(site, chosen)
    print("Random path to", site)
    print(" -> ".join(path))

def run_ascent_map():
    # Create the map graph for Ascent
    map_graph = MapGraph()

    # Add locations for Ascent
    locations = ["A Site", "B Site", "Catwalk", "Mid",
                "Market", "A Main", "B Main", "Tree"]
    for location in locations:
        map_graph.add_location(location)

    # Add connections with weight 1 and direction
    connections = [
        # Connections 
        ("A Site", "A Main", True, 1), 
        ("A Site", "Tree", True, 1), 
        ("Tree", "Catwalk", True, 1),
        ("Catwalk", "A Main", True, 1),
        ("B Site", "B Main", True, 1), 
        ("B Main", "A Main", True, 1),
        ("B Main", "Mid", True, 1), 
        ("Catwalk", "Mid", True, 1), 
        ("Market", "Mid", True, 1),
        ("B Site", "Market", True, 1), 
        ("Catwalk", "Mid", True, 1)
    ]

    for connection in connections:
        map_graph.add_connection(connection[0], connection[1], connection[2], connection[3])

    # Print the map for Ascent
    map_graph.print_map()

    cont = True
    while cont:
        # Call the function to get the chosen site
        chosen_site = choose_site(2)

        # Call the function to generate a random path to the chosen site
        starting_points = ["Catwalk", "Mid", "A Main", "B Main"]
        chosen_starting_point = random.choice(starting_points)
        print(chosen_starting_point)
        generate_random_path_to_site(chosen_site, chosen_starting_point, map_graph)
        
        # Ask if the user wants to continue
        user_input = input("Do you want to generate another random path? Press Enter to continue, or type 'gg' to exit: ").strip().lower()
        cont = (user_input != 'gg')
