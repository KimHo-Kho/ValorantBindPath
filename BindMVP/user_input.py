import random

# Function to get the user's choice of site
def choose_site(num_sites):
    if num_sites == 2:
        sites = ["A Site", "B Site"]
        prompt = "Which site do you want to hit? (A/B)"
    elif num_sites == 3:
        sites = ["A Site", "B Site", "C Site"]
        prompt = "Which site do you want to hit? (A/B/C)"
    else:
        raise ValueError("Invalid number of sites. Must be 2 or 3.")

    # Ask the user to choose a site
    print(prompt)
    choice = input().strip().upper()

    if choice in ['A', 'B', 'C'][:num_sites]:
        print(f"You chose to hit {sites[ord(choice) - ord('A')]}.")
        return sites[ord(choice) - ord('A')]  # Return the chosen site
    else:
        # If no valid choice, randomly select a site
        random_site = random.choice(sites)
        print(f"No valid choice. Randomly selected to hit {random_site}.")
        return random_site  # Return the randomly selected site

def choose_map():
    print("Select the map:")
    print("1. Ascent")
    print("2. Bind")
    print("3. Breeze")
    print("4. Haven")
    print("5. Lotus")
    print("6. Split")
    print("7. Sunset")

    map_choice = input("Enter the number of the map or enter gg to exit: ").strip()

    if map_choice == "1":
        return "Ascent"
    elif map_choice == "2":
        return "Bind"
    elif map_choice == "3":
        return "Breeze"
    elif map_choice == "4":
        return "Haven"
    elif map_choice == "5":
        return "Lotus"
    elif map_choice == "6":
        return "Split"
    elif map_choice == "7":
        return "Sunset"
    elif map_choice == "gg":
        return "gg"
    else:
        print("Invalid choice. Please select a valid map.")
        return None
