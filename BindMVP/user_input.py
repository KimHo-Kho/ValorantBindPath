import random

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
